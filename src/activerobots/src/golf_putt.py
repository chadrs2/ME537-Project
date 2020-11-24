#!/usr/bin/env python

#####################################################################################
#                                                                                   #
# Copyright (c) 2014, Active Robots Ltd.                                            #
# All rights reserved.                                                              #
#                                                                                   #
# Redistribution and use in source and binary forms, with or without                #
# modification, are permitted provided that the following conditions are met:       #
#                                                                                   #
# 1. Redistributions of source code must retain the above copyright notice,         #
#    this list of conditions and the following disclaimer.                          #
# 2. Redistributions in binary form must reproduce the above copyright              #
#    notice, this list of conditions and the following disclaimer in the            #
#    documentation and/or other materials provided with the distribution.           #
# 3. Neither the name of the Active Robots nor the names of its contributors        #
#    may be used to endorse or promote products derived from this software          #
#    without specific prior written permission.                                     #
#                                                                                   #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"       #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE         #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE        #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE          #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR               #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF              #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS          #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN           #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)           #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE        #
# POSSIBILITY OF SUCH DAMAGE.                                                       #
#                                                                                   #
#####################################################################################

import rospy
import roslib

#import cv;
import cv2 as cv;
import cv_bridge

import numpy
import math
import os
import sys
import string
import time
import random
import tf
from sensor_msgs.msg import Image
import baxter_interface
from moveit_commander import conversions
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from std_msgs.msg import Header
import std_srvs.srv
from baxter_core_msgs.srv import SolvePositionIK, SolvePositionIKRequest

# load the package manifest
roslib.load_manifest("activerobots")

# initialise ros node
rospy.init_node("pick_and_place", anonymous = True)

# directory used to save analysis images
image_directory = os.getenv("HOME") + "/Golf/"

# locate class
class locate():
    def __init__(self, camera, distance):
        global image_directory

        # image directory
        self.image_dir = image_directory

        # flag to control saving of analysis images
        self.save_images = True

        # required position accuracy in metres
        self.tray_tolerance = 0.05

        # start positions
        self.ball_tray_z = 0.15                        # z     = up down

        # camera parameters (NB. other parameters in open_camera)
        self.cam_calib    = 0.0025                     # meters per pixel at 1 meter
        self.width        = 960                        # Camera resolution
        self.height       = 600

        # Hough circle accumulator threshold and minimum radius.
        self.hough_accumulator = 35
        self.hough_min_radius  = 15
        self.hough_max_radius  = 35

        # canny image
        self.canny = cv.CreateImage((self.width, self.height), 8, 1)

        # Canny transform parameters
        self.canny_low  = 45
        self.canny_high = 150

        # minimum ball tray area
        self.min_area = 20000

        # callback image
        self.cv_image = cv.CreateImage((self.width, self.height), 8, 3)

        # colours
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        # ball tray corners
        self.ball_tray_corner = [(0.0,0.0),(0.0,0.0),(0.0,0.0),(0.0,0.0)]

        # ball tray places
        self.ball_tray_place = [(0.0,0.0),(0.0,0.0),(0.0,0.0),(0.0,0.0),
                                (0.0,0.0),(0.0,0.0),(0.0,0.0),(0.0,0.0),
                                (0.0,0.0),(0.0,0.0),(0.0,0.0),(0.0,0.0)]

        # create image publisher to head monitor
        self.pub = rospy.Publisher('/robot/xdisplay', Image, latch=True)

        # display the start splash screen
        self.splash_screen("Visual Servoing", "Pick and Place")

        # reset cameras
        self.reset_cameras()

        # close all cameras
        self.close_camera("left")
        self.close_camera("right")
        self.close_camera("head")

        # open required camera
        self.open_camera(self.camera, self.width, self.height)

        # subscribe to required camera
        self.subscribe_to_camera(self.camera)

        # distance of arm to table and ball tray
        self.distance      = distance
        self.tray_distance = distance - 0.075

    # reset all cameras (incase cameras fail to be recognised on boot)
    def reset_cameras(self):
        reset_srv = rospy.ServiceProxy('cameras/reset', std_srvs.srv.Empty)
        rospy.wait_for_service('cameras/reset', timeout=10)
        reset_srv()

    # open a camera and set camera parameters
    def open_camera(self, camera, x_res, y_res):
        if camera == "left":
            cam = baxter_interface.camera.CameraController("left_hand_camera")
        elif camera == "right":
            cam = baxter_interface.camera.CameraController("right_hand_camera")
        elif camera == "head":
            cam = baxter_interface.camera.CameraController("head_camera")
        else:
            sys.exit("ERROR - open_camera - Invalid camera")

        # close camera
        cam.close()

        # set camera parameters
        cam.resolution          = (int(x_res), int(y_res))
        cam.exposure            = -1             # range, 0-100 auto = -1
        cam.gain                = -1             # range, 0-79 auto = -1
        cam.white_balance_blue  = -1             # range 0-4095, auto = -1
        cam.white_balance_green = -1             # range 0-4095, auto = -1
        cam.white_balance_red   = -1             # range 0-4095, auto = -1

        # open camera
        cam.open()

    # close a camera
    def close_camera(self, camera):
        if camera == "left":
            cam = baxter_interface.camera.CameraController("left_hand_camera")
        elif camera == "right":
            cam = baxter_interface.camera.CameraController("right_hand_camera")
        elif camera == "head":
            cam = baxter_interface.camera.CameraController("head_camera")
        else:
            sys.exit("ERROR - close_camera - Invalid camera")

        # set camera parameters to automatic
        cam.exposure            = -1             # range, 0-100 auto = -1
        cam.gain                = -1             # range, 0-79 auto = -1
        cam.white_balance_blue  = -1             # range 0-4095, auto = -1
        cam.white_balance_green = -1             # range 0-4095, auto = -1
        cam.white_balance_red   = -1             # range 0-4095, auto = -1

        # close camera
        cam.close()

    # convert Baxter point to image pixel
    def baxter_to_pixel(self, pt, dist):
        x = (self.width / 2)                                                         \
          + int((pt[1] - (self.pose[1] + self.cam_y_offset)) / (self.cam_calib * dist))
        y = (self.height / 2)                                                        \
          + int((pt[0] - (self.pose[0] + self.cam_x_offset)) / (self.cam_calib * dist))

        return (x, y)

    # convert image pixel to Baxter point
    def pixel_to_baxter(self, px, dist):
        x = ((px[1] - (self.height / 2)) * self.cam_calib * dist)                \
          + self.pose[0] + self.cam_x_offset
        y = ((px[0] - (self.width / 2)) * self.cam_calib * dist)                 \
          + self.pose[1] + self.cam_y_offset

        return (x, y)

    # Not a tree walk due to python recursion limit
    def tree_walk(self, image, x_in, y_in):
        almost_black = (1, 1, 1)

        pixel_list = [(x_in, y_in)]                   # first pixel is black save position
        cv.Set2D(image, y_in, x_in, almost_black)     # set pixel to almost black
        to_do = [(x_in, y_in - 1)]                    # add neighbours to to do list
        to_do.append([x_in, y_in + 1])
        to_do.append([x_in - 1, y_in])
        to_do.append([x_in + 1, y_in])

        while len(to_do) > 0:
            x, y = to_do.pop()                             # get next pixel to test
            if cv.Get2D(image, y, x)[0] == self.black[0]:  # if black pixel found
                pixel_list.append([x, y])                  # save pixel position
                cv.Set2D(image, y, x, almost_black)        # set pixel to almost black
                to_do.append([x, y - 1])                   # add neighbours to to do list
                to_do.append([x, y + 1])
                to_do.append([x - 1, y])
                to_do.append([x + 1, y])

        return pixel_list

    # Remove artifacts and find largest object
    def look_for_ball_tray(self, canny):
        width, height = cv.GetSize(canny)

        centre   = (0, 0)
        max_area = 0

        # for all but edge pixels
        for x in range(1, width - 2):
            for y in range(1, height - 2):
                if cv.Get2D(canny, y, x)[0] == self.black[0]:       # black pixel found
                    pixel_list = self.tree_walk(canny, x, y)        # tree walk pixel
                    if len(pixel_list) < self.min_area:             # if object too small
                        for l in pixel_list:
                            cv.Set2D(canny, l[1], l[0], self.white) # set pixel to white
                    else:                                           # if object found
                        n = len(pixel_list)
                        if n > max_area:                            # if largest object found
                            sum_x  = 0                              # find centre of object
                            sum_y  = 0
                            for p in pixel_list:
                                sum_x  = sum_x + p[0]
                                sum_y  = sum_y + p[1]

                            centre = sum_x / n, sum_y / n           # save centre of object
                            max_area = n                            # save area of object

        if max_area > 0:                                            # in tray found
            cv.Circle(canny, (centre), 9, (250, 250, 250), -1)      # mark tray centre

        # display the modified canny
        cv.ShowImage("Modified Canny", canny)

        # 3ms wait
        cv.WaitKey(3)

        return centre                                        # return centre of object

    # flood fill edge of image to leave objects
    def flood_fill_edge(self, canny):
        width, height = cv.GetSize(canny)

        # set boarder pixels to white
        for x in range(width):
            cv.Set2D(canny, 0, x, self.white)
            cv.Set2D(canny, height - 1, x, self.white)

        for y in range(height):
            cv.Set2D(canny, y, 0, self.white)
            cv.Set2D(canny, y, width - 1, self.white)

        # prime to do list
        to_do = [(2, 2)]
        to_do.append([2, height - 3])
        to_do.append([width - 3, height - 3])
        to_do.append([width - 3, 2])

        while len(to_do) > 0:
            x, y = to_do.pop()                               # get next pixel to test
            if cv.Get2D(canny, y, x)[0] == self.black[0]:    # if black pixel found
                cv.Set2D(canny, y, x, self.white)            # set pixel to white
                to_do.append([x, y - 1])                     # add neighbours to to do list
                to_do.append([x, y + 1])
                to_do.append([x - 1, y])
                to_do.append([x + 1, y])

    # camera call back function
    def camera_callback(self, data, camera_name):
        # Convert image from a ROS image message to a CV image
        try:
            self.cv_image = cv_bridge.CvBridge().imgmsg_to_cv(data, "bgr8")
        except cv_bridge.CvBridgeError as e:
            print(e)

        # 3ms wait
        cv.WaitKey(3)

    # left camera call back function
    def left_camera_callback(self, data):
        self.camera_callback(data, "Left Hand Camera")

    # right camera call back function
    def right_camera_callback(self, data):
        self.camera_callback(data, "Right Hand Camera")

    # head camera call back function
    def head_camera_callback(self, data):
        self.camera_callback(data, "Head Camera")

    # create subscriber to the required camera
    def subscribe_to_camera(self, camera):
        if camera == "left":
            callback = self.left_camera_callback
            camera_str = "/cameras/left_hand_camera/image"
        elif camera == "right":
            callback = self.right_camera_callback
            camera_str = "/cameras/right_hand_camera/image"
        elif camera == "head":
            callback = self.head_camera_callback
            camera_str = "/cameras/head_camera/image"
        else:
            sys.exit("ERROR - subscribe_to_camera - Invalid camera")

        camera_sub = rospy.Subscriber(camera_str, Image, callback)

    # Convert cv image to a numpy array
    def cv2array(self, im):
        depth2dtype = {cv.IPL_DEPTH_8U: 'uint8',
                       cv.IPL_DEPTH_8S: 'int8',
                       cv.IPL_DEPTH_16U: 'uint16',
                       cv.IPL_DEPTH_16S: 'int16',
                       cv.IPL_DEPTH_32S: 'int32',
                       cv.IPL_DEPTH_32F: 'float32',
                       cv.IPL_DEPTH_64F: 'float64'}
  
        arrdtype=im.depth
        a = numpy.fromstring(im.tostring(),
                             dtype = depth2dtype[im.depth],
                             count = im.width * im.height * im.nChannels)
        a.shape = (im.height, im.width, im.nChannels)

        return a

    # Use Hough circles to find ball centres (Only works with round objects)
    def hough_it(self, n_ball, iteration):
        # create gray scale image of balls
        gray_image = cv.CreateImage((self.width, self.height), 8, 1)
        cv.CvtColor(self.cv_image, gray_image, cv.CV_BGR2GRAY)

        # create gray scale array of balls
        gray_array = self.cv2array(gray_image)

        # find Hough circles
        circles = cv2.HoughCircles(gray_array, cv.CV_HOUGH_GRADIENT, 1, 40, param1=50,  \
                  param2=self.hough_accumulator, minRadius=self.hough_min_radius,       \
                  maxRadius=self.hough_max_radius)

        # Check for at least one ball found
        if circles is None:
            # display no balls found message on head display
            self.splash_screen("no balls", "found")
            # no point in continuing so exit with error message
            sys.exit("ERROR - hough_it - No golf balls found")

        circles = numpy.uint16(numpy.around(circles))

        ball_data = {}
        n_balls   = 0

        circle_array = numpy.asarray(self.cv_image)

        # check if golf ball is in ball tray
        for i in circles[0,:]:
            # convert to baxter coordinates
            ball = self.pixel_to_baxter((i[0], i[1]), self.tray_distance)

            if self.is_near_ball_tray(ball):
                # draw the outer circle in red
                cv2.circle(circle_array, (i[0], i[1]), i[2], (0, 0, 255), 2)
                # draw the center of the circle in red
                cv2.circle(circle_array, (i[0], i[1]), 2, (0, 0, 255), 3)
            elif i[1] > 800:
                # draw the outer circle in red
                cv2.circle(circle_array, (i[0], i[1]), i[2], (0, 0, 255), 2)
                # draw the center of the circle in red
                cv2.circle(circle_array, (i[0], i[1]), 2, (0, 0, 255), 3)
            else:
                # draw the outer circle in green
                cv2.circle(circle_array, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # draw the center of the circle in green
                cv2.circle(circle_array, (i[0], i[1]), 2, (0, 255, 0), 3)

                ball_data[n_balls]  = (i[0], i[1], i[2])
                n_balls            += 1

        circle_image = cv.fromarray(circle_array)

        cv.ShowImage("Hough Circle", circle_image)

        # 3ms wait
        cv.WaitKey(3)

        # display image on head monitor
        font     = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1.0, 1.0, 1)
        position = (30, 60)
        s = "Searching for golf balls"
        cv.PutText(circle_image, s, position, font, self.white)
        msg = cv_bridge.CvBridge().cv_to_imgmsg(circle_image, encoding="bgr8")
        self.pub.publish(msg)

        if self.save_images:
            # save image of Hough circles on raw image
            file_name = self.image_dir                                                 \
                      + "hough_circle_" + str(n_ball) + "_" + str(iteration) + ".jpg"
            cv.SaveImage(file_name, circle_image)

        # Check for at least one ball found
        if n_balls == 0:                    # no balls found
            # display no balls found message on head display
            self.splash_screen("no balls", "found")
            # less than 12 balls found, no point in continuing, exit with error message
            sys.exit("ERROR - hough_it - No golf balls found")

        # select next ball and find it's position
        next_ball = self.find_next_golf_ball(ball_data, iteration)

        # find best gripper angle to avoid touching neighbouring ball
        angle = self.find_gripper_angle(next_ball, ball_data)

        # return next golf ball position and pickup angle
        return next_ball, angle

    # find distance of limb from nearest line of sight object
    def get_distance(self, limb):
        if limb == "left":
            dist = baxter_interface.analog_io.AnalogIO('left_hand_range').state()
        elif limb == "right":
            dist = baxter_interface.analog_io.AnalogIO('right_hand_range').state()
        else:
            sys.exit("ERROR - get_distance - Invalid limb")

        # convert mm to m and return distance
        return float(dist / 1000.0)

    # find the ball tray
    def canny_it(self, iteration):
        if self.save_images:
            # save raw image of ball tray
            file_name = self.image_dir + "ball_tray_" + str(iteration) + ".jpg"
            cv.SaveImage(file_name, self.cv_image)

        # create an empty image variable, the same dimensions as our camera feed.
        gray = cv.CreateImage((cv.GetSize(self.cv_image)), 8, 1)

        # convert the image to a grayscale image
        cv.CvtColor(self.cv_image, gray, cv.CV_BGR2GRAY)

        # display image on head monitor
        font     = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1.0, 1.0, 1)
        position = (30, 60)
        cv.PutText(self.cv_image, "Looking for ball tray", position, font, self.white)
        msg = cv_bridge.CvBridge().cv_to_imgmsg(self.cv_image, encoding="bgr8")
        self.pub.publish(msg)

        # create a canny edge detection map of the greyscale image
        cv.Canny(gray, self.canny, self.canny_low, self.canny_high, 3)

        # display the canny transformation
        cv.ShowImage("Canny Edge Detection", self.canny)

        if self.save_images:
            # save Canny image of ball tray
            file_name = self.image_dir + "canny_tray_" + str(iteration) + ".jpg"
            cv.SaveImage(file_name, self.canny)

        # flood fill edge of image to leave only objects
        self.flood_fill_edge(self.canny)
        ball_tray_centre = self.look_for_ball_tray(self.canny)

        # 3ms wait
        cv.WaitKey(3)

        while ball_tray_centre[0] == 0:
            if random.random() > 0.6:
                self.baxter_ik_move(self.limb, self.dither())

            ball_tray_centre = self.canny_it(iteration)

        return ball_tray_centre

    # find four corners of the ball tray
    def find_corners(self, centre):
        # find bottom corner
        max_x  = 0
        max_y  = 0

        for x in range(100, self.width - 100):
            y = self.height - 20
            while y > 0 and cv.Get2D(self.canny, y, x)[0] > 100:
                y = y - 1
            if y > 20:
                cv.Set2D(self.cv_image, y, x, (0, 0, 255))
                if y > max_y:
                    max_x = x
                    max_y = y

        corner_1 = (max_x, max_y)

        # find left corner
        min_x  = self.width
        min_y  = 0

        for y in range(100, self.height - 100):
            x = 20
            while x < self.width - 1 and cv.Get2D(self.canny, y, x)[0] > 100:
                x = x + 1
            if x < self.width - 20:
                cv.Set2D(self.cv_image, y, x, (0, 255, 0, 0))
                if x < min_x:
                    min_x = x
                    min_y = y

        corner_2 = (min_x, min_y)

        # display corner image
        cv.ShowImage("Corner", self.cv_image)

        if self.save_images:
            # save Canny image
            file_name = self.image_dir + "egg_tray_canny.jpg"
            cv.SaveImage(file_name, self.canny)

            # mark corners and save corner image
            cv.Circle(self.cv_image, corner_1, 9, (0, 250, 0), -1)
            cv.Circle(self.cv_image, corner_2, 9, (0, 250, 0), -1)
            file_name = self.image_dir + "corner.jpg"
            cv.SaveImage(file_name, self.cv_image)

        # 3ms wait
        cv.WaitKey(3)

        # two corners found and centre known find other two corners
        corner_3 = ((2 * centre[0]) - corner_1[0], (2 * centre[1]) - corner_1[1])
        corner_4 = ((2 * centre[0]) - corner_2[0], (2 * centre[1]) - corner_2[1])

        # draw ball tray boundry
        c1 = (int(corner_1[0]), int(corner_1[1]))
        c2 = (int(corner_2[0]), int(corner_2[1]))
        c3 = (int(corner_3[0]), int(corner_3[1]))
        c4 = (int(corner_4[0]), int(corner_4[1]))

        cv.Line(self.cv_image, c1, c2, (255, 0, 0), thickness=3)
        cv.Line(self.cv_image, c2, c3, (255, 0, 0), thickness=3)
        cv.Line(self.cv_image, c3, c4, (255, 0, 0), thickness=3)
        cv.Line(self.cv_image, c4, c1, (255, 0, 0), thickness=3)

        return True, (corner_1, corner_2, corner_3, corner_4)

    # find the ball tray
    def find_ball_tray(self):
        ok = False
        while not ok:
            ball_tray_centre = self.canny_it(0)

            error     = 2 * self.tray_tolerance
            iteration = 1

            # iterate until arm over centre of tray
            while error > self.tray_tolerance:
                ball_tray_centre, error = self.ball_tray_iterate(iteration,       \
                                          ball_tray_centre)
                iteration              += 1

            # find ball tray corners in pixel units
            (ok, corners) = self.find_corners(ball_tray_centre)

        self.find_places(corners)

    
    # display message on head display
    def splash_screen(self, s1, s2):
        splash_array = numpy.zeros((self.height, self.width, 3), numpy.uint8)
        font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 3.0, 3.0, 9)

        ((text_x, text_y), baseline) = cv.GetTextSize(s1, font)
        org = ((self.width - text_x) / 2, (self.height / 3) + (text_y / 2))
        cv2.putText(splash_array, s1, org, cv.CV_FONT_HERSHEY_SIMPLEX, 3.0,          \
                    self.white, thickness = 7)

        ((text_x, text_y), baseline) = cv.GetTextSize(s2, font)
        org = ((self.width - text_x) / 2, ((2 * self.height) / 3) + (text_y / 2))
        cv2.putText(splash_array, s2, org, cv.CV_FONT_HERSHEY_SIMPLEX, 3.0,          \
                    self.white, thickness = 7)

        splash_image = cv.fromarray(splash_array)

        # 3ms wait
        cv2.waitKey(3)

        msg = cv_bridge.CvBridge().cv_to_imgmsg(splash_image, encoding="bgr8")
        self.pub.publish(msg)

def main():
    camera = "head"
    distance = 1
    # create locate class instance
    locator = locate(camera, distance)

    input("Press Enter to start: ")

    # find the ball tray
    #locator.find_ball_tray()

if __name__ == "__main__":
    main()

