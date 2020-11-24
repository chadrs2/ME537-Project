#!/usr/local/bin/python

#system level imports
import sys, os
from collections import deque
import numpy as np
import scipy.io as sio


from copy import deepcopy
from threading import RLock, Timer
import time
from math import pi
from baxter_interface.limb import Limb
from rad_baxter_limb import RadBaxterLimb
from baxter_pykdl import baxter_kinematics as b_kin
import rospy
import tf
from std_msgs.msg import UInt16


if __name__ == '__main__':
    rospy.init_node('me_537_lab')
    limb = RadBaxterLimb('right')
    #limb = RadBaxterLimb('left')

    sonar_pub = rospy.Publisher("/robot/sonar/head_sonar/set_sonars_enabled",UInt16,queue_size=1)
    sonar_pub.publish(0)

