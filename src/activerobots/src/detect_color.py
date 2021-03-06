#! /usr/bin/python

import numpy as np
import cv2
import argparse
import rospy
import tf
import math
from geometry_msgs.msg import Transform

rospy.init_node('my_stuff')

def color_detector(image,lower,upper):

    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    cv2.imwrite('camera_image_mod.jpeg', output)
    
    imgray  = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
    thresh,im_bw = cv2.threshold(imgray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    pixels = cv2.findNonZero(im_bw)
    loc_sum = 0
    for loc in pixels:
        loc_sum += loc
    pixel_avg = loc_sum/len(pixels)
    u = pixel_avg[0,0]
    v = pixel_avg[0,1]
    cv2.circle(im_bw,(u,v),5,(255,0,0),-1)
    #cv2.imshow("show me stuff",im_bw)
    #cv2.waitKey()
    cv2.imwrite('camera_image_bw.jpeg',im_bw)
    return u,v

def get_T_matrix(q,t):
    qw = q[0]
    qx = q[1]
    qy = q[2]
    qz = q[3]
    tx = t[0]
    ty = t[1]
    tz = t[2]
    
    T = np.matrix([[1-2*qy**2-2*qz**2,2*qx*qy-2*qz*qw,2*qx*qz+2*qy*qw,tx],[2*qx*qy+2*qz*qw,1-2*qx**2-2*qz**2,2*qy*qz-2*qx*qw,ty],[2*qx*qz-2*qy*qw,2*qy*qz+2*qx*qw,1-2*qx**2-2*qy**2,tz],[0,0,0,1]])
    return T

def find_object_position(u,v,z,focal_len,o_r,o_c):
    x = -(u-o_r)*z/focal_len
    y = -(v-o_c)*z/focal_len
    return x,y

def convert_to_base_frame(xp,yp,zp,T):
    P1 = np.array([[xp],[yp],[zp],[1]])
    P0 = T.dot(P1)
    return P0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help = "path to the image")
    args = vars(ap.parse_args())
    image = cv2.imread(args["image"])
    
    #From head to base
    #Quaternion = [0.457,0.449, 0.538,0.548]
    #Translation = [0.188,0.008, 0.75]
    
    #From head to left wrist
    Quaternion = [0.529, 0.556, -0.464,-0.443]
    #Quaternion = [-0.446, -0.459, 0.552,0.534]
    Translation = [.129,.703,.804]
    focal_len = 410
    o_r = 639.5
    o_c = 399.5
    z_meas = 2.8

    T = get_T_matrix(Quaternion,Translation)
    print(T)

    #Define RGB values you're looking for
    RGB_lower = [25,25, 70] #red
    RGB_upper = [75,50,100]
    u,v = color_detector(image,RGB_lower,RGB_upper)
    print((u,v))

    xp,yp = find_object_position(u,v,z_meas,focal_len,o_r,o_c)
    print((xp,yp))

    P = convert_to_base_frame(xp,yp,z_meas,T)
    print(P)

    #rospy.spin()

if __name__ == '__main__':
    main()
