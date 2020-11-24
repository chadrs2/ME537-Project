#!/usr/bin/env python

import rospy
import time
import numpy as np
import angle_test_cmd as acmd
from math import pi
from torque_controller.msg import q_cmd
from torque_controller.msg import k_cmd
from torque_controller.msg import imp_cmd

def ang_k_pub():
    publ = rospy.Publisher('left/joint_cmd', q_cmd)
    pubr = rospy.Publisher('right/joint_cmd', q_cmd)
    pubimp = rospy.Publisher('left/imp_cmd', imp_cmd)
    pub_goal = rospy.Publisher('left/joint_q_goal', q_cmd)
    pubkp = rospy.Publisher('kp', k_cmd)
    pubkd = rospy.Publisher('kd', k_cmd)
    rospy.init_node('joint_cmd')

    this_time = time.time()
    last_time = time.time()
    case = 0

    while not rospy.is_shutdown():
        #lcmd = acmd.langles()
        #rcmd = acmd.rangles()
#        rospy.loginfo(lcmd)
#        rospy.loginfo(rcmd)
        #l_goal = [pi/4]
#        rospy.loginfo(l_goal)
       # publ.publish(q_cmd(lcmd))
#        pubr.publish(q_cmd(rcmd))
        #pub_goal.publish(q_cmd(l_goal))
        this_time = time.time()
        change = 3 #sec

        if this_time - last_time > change:
            case = case + 1
            last_time = this_time

        if case == 4:
            case = 0

        case = 1
        if case == 0:
            l_goal = [pi/4, -pi/4]
        elif case == 1:
            l_goal = [0.0, 0.0]
        elif case == 2:
            l_goal = [pi/4, 0.0]
        elif case == 3:
            l_goal = [0.0, -pi/4]

       # publ.publish(q_cmd([l_goal[0], l_goal[1], 0,0,0,0,0]))
        pubimp.publish(imp_cmd([l_goal[0], l_goal[1], 0,0,0,0,0], [0,0,0,0,0,0,0]))
        rospy.loginfo(l_goal)
        kp = [80, 0, 0, 0, 0, 0, 0,   # 80 or 60 // 50
              0, 60, 0, 0, 0, 0, 0,   # 60  // 40
              0, 0, 150, 0, 0, 0, 0,   # // 20
              0, 0, 0, 28, 0, 0, 0,   # // 28
              0, 0, 0, 0, 8, 0, 0,   # // 8
              0, 0, 0, 0, 0, 10, 0,   # // 10
              0, 0, 0, 0, 0, 0, 6]   # // 6
        kd = [10, 0, 0, 0, 0, 0, 0,   # 7.0 // 9
              0, 8.0, 0, 0, 0, 0, 0,  # 8.0 // 12
              0, 0, 0.1, 0, 0, 0, 0,   # // 4
              0, 0, 0, 7, 0, 0, 0,   # // 7
              0, 0, 0, 0, 1.5, 0, 0,   # // 1.5
              0, 0, 0, 0, 0, 1.5, 0,   # // 1.5
              0, 0, 0, 0, 0, 0, 1.0]   # // 1.0
        #    kp = kp.tolist()
        #   kd = kd.tolist()
#        rospy.loginfo(kp)
#        rospy.loginfo(kd)
        pubkp.publish(k_cmd(kp))
        pubkd.publish(k_cmd(kd))
        rospy.sleep(.10)

if __name__ == '__main__':
    try:
        ang_k_pub()
    except rospy.ROSInterruptException:
        pass
