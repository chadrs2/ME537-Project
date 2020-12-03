#!/usr/bin/env python3
import rospy
import tf
import numpy as np
from rad_baxter_limb import RadBaxterLimb
import baxter_interface
import baxter_left_kinematics as blk
import baxter_right_kinematics as brk

rospy.init_node('Aaron_Node')
r_limb = RadBaxterLimb('right')
l_limb = RadBaxterLimb('left')

joint_commands = []
joint_commands.append(np.array([0, 0, 0, 0, 0, 0, 0]))
joint_commands.append(np.array([0, -np.pi/4, 0, 0, 0, 0, 0]))

control_rate = rospy.Rate(500)
r_limb.set_joint_position_speed(0.5)

# step = 
for command in joint_commands:
    curr_pose = r_limb.get_joint_angles()

    error = np.abs(np.subtract(command,curr_pose))
    
    while np.max(error) > .1:
        r_limb.set_joint_positions_mod(command)
        control_rate.sleep()

        curr_pose = r_limb.get_joint_angles()
        error = np.abs(np.subtract(command,curr_pose))

