#!/usr/bin/env python

import rospy
import numpy as np
from numpy import pi
import scipy.io as sio
from rad_baxter_limb.rad_baxter_limb import RadBaxterLimb as RBL
from torque_controller.msg import q_cmd
from collections import deque
import time
import sys


def main():
    rospy.init_node('record_data')

    publ = rospy.Publisher('left/joint_cmd', q_cmd, queue_size = 10)
    pubr = rospy.Publisher('right/joint_cmd', q_cmd, queue_size = 10)
    
    my_dict = dict()
    q_des_save = deque()
    x = deque()
    t_x = deque()
    record = True
    left = RBL('left', record)
    right = RBL('right', record)

    start = time.time()
    q = left.get_joint_angles()
    


    pause = False

    for i in range(2):
        
        if i == 1:
            pause == True
        if pause == True:
            print('Move arm, then press enter key')
            input()
            pause = False
            
        start = time.time()
        now = 0
        while now < 15:
            now = time.time() - start        
            t_x.append(now)
        #l_cmd_1 = [0.0460, -0.4809, -0.8640, 1.6490, 1.0983, 0.7118, -0.4989]
        #l_cmd_2 = [0.8590, -0.5944, -2.3435, 0.5772, 1.8327, 0.7225, -0.4997]
            
        #long test commands test 1 and 2
        #l_cmd_1 = [0.62663115, -0.93917974, -0.07363108 ,  1.13706326, -0.17027187, 1.93665074, -0.14687866]
        #l_cmd_2 = [-0.4467719, 0.29490781, -0.71943699, 1.26476716, -0.20928838, -0.08398545, -1.46993709]
            
            
        #short angles test 5
            l_cmd_1 = [0.62663115, -0.93917974, -0.07363108 ,  1.13706326, -0.17027187, 1.93665074, -0.14687866]

            l_cmd_2 = [ 0.53037386, -0.76852437, -0.21360682,  1.47799049, -0.20363595,  1.87145656, -0.14956313]
            
        #short angles test 6
            l_cmd_3 = [-0.4467719, 0.29490781, -0.71943699, 1.26476716, -0.20928838, -0.08398545, -1.46993709]
            l_cmd_4 = [-0.1514806, -0.07593205, -0.5510826, 1.50483515, -0.20516993, 0.65002436, -1.47914097]
            
        #l_cmd = np.matrix(q) + np.ones([1,7])*10*pi/180
        #l_cmd = l_cmd.flatten('F').A1.tolist()
            if i ==  0:
                if now < 7.5:
                    publ.publish(q_cmd(l_cmd_1))
                    rospy.loginfo(l_cmd_1)
                    q_des_save.append(l_cmd_1)
                
                else:
                    publ.publish(q_cmd(l_cmd_2))
                    rospy.loginfo(l_cmd_2)
                    q_des_save.append(l_cmd_2)
            else:
                if now < 7.5:

                    publ.publish(q_cmd(l_cmd_3))
                    rospy.loginfo(l_cmd_3)
                    q_des_save.append(l_cmd_3)
                else:
                    publ.publish(q_cmd(l_cmd_4))
                    rospy.loginfo(l_cmd_4)
                    q_des_save.append(l_cmd_4)
            
            print(left.get_kdl_forward_position_kinematics())
            x.append(left.get_kdl_forward_position_kinematics())

            rospy.sleep(.01)


    my_dict = {'q': left.q_history, 'qd': left.qd_history, 'time': left.time_history, 'q_des': q_des_save, 'x': x, 't_x': t_x}

    sio.savemat('impedance_compare_3.mat', my_dict)

if __name__ == '__main__':
    main()

    
