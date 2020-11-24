#!/usr/bin/env python

import rospy
import roslib

import math
import tf
import baxter_interface
import os
import sys
import time
from moveit_commander import conversions
from geometry_msgs.msg import ( PoseStamped,
                                Pose,
                                Point,
                                Quaternion )
from std_msgs.msg import Header
# import std_srvs.srv
from baxter_core_msgs.srv import ( SolvePositionIK,
                                   SolvePositionIKRequest )

# golf setup class
class golf_setup():
    "Golf setup program"
    def __init__(self, arm):
        # initialise ros node
        rospy.init_node("Locate", anonymous = True)

        # load the package manifest
        roslib.load_manifest("activerobots")

        # arm ("left" or "right")
        self.limb           = arm
        self.limb_interface = baxter_interface.Limb(self.limb)

        # image directory
        self.image_dir = os.getenv("HOME") + "/Golf/"

        # distance to table
        self.distance = 0.0

    # save setup values
    def save(self):
        # open setup file
        f = open(self.image_dir + "setup.dat", "w")
        s = 'limb = %s\n' % self.limb
        f.write(s)
        s = 'distance = %s\n' % self.distance
        f.write(s)

def main():
    limb  = "left"
    setup = golf_setup(limb)

    print("distance = ", setup.distance)

    setup.save()
    print("finished fools")
if __name__ == "__main__":
    main()

# rospy.spin()

