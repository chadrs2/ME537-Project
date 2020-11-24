#system level imports
import sys, os
from collections import deque
import numpy as np
import scipy.io as sio
#!/usr/local/bin/python

from copy import deepcopy
from threading import RLock, Timer
import time
from math import pi
from baxter_interface.limb import Limb
from rad_baxter_limb import RadBaxterLimb
from baxter_pykdl import baxter_kinematics as b_kin
import rospy
import tf
import baxter_interface
# rospy.init_node('vac')




if __name__ == '__main__':
    rospy.init_node('me_537_lab')
    limb = RadBaxterLimb('right')
    limb.set_joint_position_speed(0.6)
    control_rate = rospy.Rate(500)
    

    right_gripper = baxter_interface.Gripper('right')

    right_gripper.open()
 
    time.sleep(3)

    right_gripper.close()







