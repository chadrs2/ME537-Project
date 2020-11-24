#!/usr/bin/env python

import rospy
import numpy as np
from numpy import pi
import scipy.io as sio
from rad_baxter_limb import RadBaxterLimb as RBL
from torque_controller.msg import q_cmd
from collections import deque


def main():
    rospy.init_node('record_data')

    publ = rospy.Publisher('left/joint_cmd', q_cmd)
    pubr = rospy.Publisher('right/joint_cmd', q_cmd)
    
    my_dict = dict()
    q_des_save = deque()
    record = True
    left = RBL('left', record)
    right = RBL('right', record)
    for i in range(6):
        if i == 1:
            l_cmd = [0,0,0,0,0,0,0]
            publ.publish(q_cmd(l_cmd))
            rospy.loginfo(l_cmd)
            q_des_save.append(l_cmd)
        if i == 2:
            l_cmd = [pi/4,-pi/4,0,0,0,0,0]
            rospy.sleep(6)
            publ.publish(q_cmd(l_cmd))
            rospy.loginfo(l_cmd)
            q_des_save.append(l_cmd)
        if i == 3:
            l_cmd = [0,0,0,0,0,0,0]
            rospy.sleep(6)
            publ.publish(q_cmd(l_cmd))
            rospy.loginfo(l_cmd)
            q_des_save.append(l_cmd)
        if i == 4:
            l_cmd = [-pi/4,pi/4-.3,0,0,0,0,0]
            rospy.sleep(6)
            publ.publish(q_cmd(l_cmd))
            rospy.loginfo(l_cmd)
            q_des_save.append(l_cmd)
        if i == 5:
            l_cmd = [0,0,0,0,0,0,0]
            rospy.sleep(6)
            publ.publish(q_cmd(l_cmd))
            rospy.loginfo(l_cmd)
            q_des_save.append(l_cmd)
        if i == 6:
            l_cmd = [0,0,0,0,0,0,0]
            rospy.sleep(6)
            publ.publish(q_cmd(l_cmd))
            rospy.loginfo(l_cmd)
            q_des_save.append(l_cmd)


    my_dict = {'q': left.q_history, 'qd': left.qd_history, 'time': left.time_history, 'q_des': q_des_save}

    sio.savemat('data_no_control_2_dof_02_record.mat', my_dict)

if __name__ == '__main__':
    main()

    
