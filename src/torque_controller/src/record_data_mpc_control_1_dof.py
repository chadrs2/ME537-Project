#!/usr/bin/env python

import rospy
import numpy as np
from numpy import pi
import scipy.io as sio
from rad_baxter_limb.rad_baxter_limb import RadBaxterLimb as RBL
from torque_controller.msg import q_cmd
from torque_controller.msg import k_cmd
from collections import deque
import time


def main():
    rospy.init_node('record_data')

    publ = rospy.Publisher('left/joint_q_goal', q_cmd, queue_size = 1)
    pubr = rospy.Publisher('right/joint_cmd', q_cmd,queue_size = 1)
    
    my_dict = dict()
    q_des_save = deque()
    record = True
    left = RBL('left', record)
    right = RBL('right', record)

    pubQ = rospy.Publisher('Q', k_cmd, queue_size = 1)
    pubR1 = rospy.Publisher('R1', k_cmd, queue_size = 1)
    pubR2 = rospy.Publisher('R2', k_cmd, queue_size = 1)

    Q = [0.3, 0.50]
    R1 = [0.0010, 15.0]
    R2 = [1.0, 20.0]
    pubQ.publish(k_cmd(Q))
    pubR1.publish(k_cmd(R1))
    pubR2.publish(k_cmd(R2))
    rate = rospy.Rate(500)
    
    for i in range(2):

        now = 0
        start = time.time()
        while now < 4:
            now = time.time() - start 
            if i == 0:
                l_cmd = [1.0,0,0,0,0,0,0]
                publ.publish(q_cmd(l_cmd))
                rospy.loginfo(l_cmd)
                q_des_save.append(l_cmd)
                #rospy.sleep(6)
            if i == 1:
                l_cmd = [0.0,0,0,0,0,0,0]
                publ.publish(q_cmd(l_cmd))
                rospy.loginfo(l_cmd)
                q_des_save.append(l_cmd)
                #rospy.sleep(6)
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
                
            rate.sleep()


    my_dict = {'q': left.q_history, 'qd': left.qd_history, 'time': left.time_history, 'q_des': q_des_save}

    sio.savemat('data_mpc_control_1_dof.mat', my_dict)

if __name__ == '__main__':
    main()

    
