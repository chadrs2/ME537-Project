#!/usr/bin/env python

import rospy
import numpy as np
from numpy import pi
import scipy.io as sio
from rad_baxter_limb import RadBaxterLimb as RBL
from torque_controller.msg import q_cmd
from torque_controller.msg import k_cmd
from collections import deque


def main():
    rospy.init_node('record_data')

    publ = rospy.Publisher('left/joint_q_goal', q_cmd)
    pubr = rospy.Publisher('right/joint_cmd', q_cmd)
    
    my_dict = dict()
    q_des_save = deque()
    record = True
    left = RBL('left', record)
    right = RBL('right', record)

    pubQ = rospy.Publisher('Q', k_cmd)
    pubR1 = rospy.Publisher('R1', k_cmd)
    pubR2 = rospy.Publisher('R2', k_cmd)

    Q = [0.3, 0.50]
    R1 = [0.0010, 15.0]
    R2 = [1.0, 20.0]
    pubQ.publish(k_cmd(Q))
    pubR1.publish(k_cmd(R1))
    pubR2.publish(k_cmd(R2))

    for i in range(7):
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
            l_cmd = [pi/4,0,0,0,0,0,0]
            rospy.sleep(6)
            publ.publish(q_cmd(l_cmd))
            rospy.loginfo(l_cmd)
            q_des_save.append(l_cmd)
        if i == 5:
            l_cmd = [0,-pi/4,0,0,0,0,0]
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

    sio.savemat('data_mpc_control_2_dof.mat', my_dict)

if __name__ == '__main__':
    main()

    
