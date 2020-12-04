#!/usr/bin/env python
import rospy
import tf
import numpy as np
from rad_baxter_limb import RadBaxterLimb
import baxter_interface
import baxter_left_kinematics as blk
import baxter_right_kinematics as brk

#From From Lab 1 Start_robot
rospy.init_node('Seth_Freeman_Node')
print("made it!")
r_limb = RadBaxterLimb('right')
l_limb = RadBaxterLimb('left')
print("made it even further")
#From Lab 1 Part 1
pose = r_limb.get_kdl_forward_position_kinematics()
R = tf.transformations.quaternion_matrix(pose[3:])[0:3,0:3]
position = pose[0:3]

#From Lab 1 Part 2
joint_command_start = np.array([0, 0, 0, 0, 0, 0, 0])
control_rate = rospy.Rate(50)
r_limb.set_joint_position_speed(0.5)
joint_command = r_limb.get_joint_angles()
step = 1
while step < 2500:
    r_limb.set_joint_positions_mod(joint_command_start)
    control_rate.sleep()
    step = step + 1

# From My Past Code
right_gripper = baxter_interface.Gripper('right')
right_gripper.calibrate()
right_gripper.close()
right_gripper.open()

r_limb.get_kdl_jacobian()
brk.FK[6]([0, 0, 0, 0, 0, 0, 0])
brk.J[6]([0, 0, 0, 0, 0, 0, 0])


#Stuff I didn't use
r_limb.get_kdl_jacobian_transpose()
r_limb.get_kdl_jacobian_pseudo_inverse()
r_limb.get_kdl_jacobian_transpose()
print(r_limb.kin_kdl.inverse_kinematics(np.array([0.3, 0.3, 0.3])))
np.pi

#while not rospy.is_shutdown():
#    rospy.spin()

