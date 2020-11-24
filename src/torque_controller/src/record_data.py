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
    record = True
    left = RBL('left', record)
    right = RBL('right', record)

    start = time.time()
    q = left.get_joint_angles()

    while not rospy.is_shutdown():
        

        l_cmd = np.matrix(q) + np.ones([1,7])*10*pi/180
        l_cmd = l_cmd.flatten('F').A1.tolist()
        publ.publish(q_cmd(l_cmd))
        rospy.loginfo(l_cmd)
        q_des_save.append(l_cmd)
        now = time.time() - start
        if now > 10:
            break
        rospy.sleep(.01)


    my_dict = {'q': left.q_history, 'qd': left.qd_history, 'time': left.time_history, 'q_des': q_des_save}

    sio.savemat('data_record_test.mat', my_dict)

if __name__ == '__main__':
    main()

    
