#!/usr/bin/env python3
from numpy import linalg
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

def vex(S):
    if S.shape == (3,3):
        v = [S[2,1]-S[1,2], S[0,2]-S[2,0], S[1,0]-S[0,1]]
        v = [x * .5 for x in v]
        return v

K_inv = .5*np.eye(6)
des_position = [.9, -1.1, .3]
T_des = np.array([[0,np.sin(np.pi/4),np.cos(np.pi/4),des_position[0]],[0,np.cos(np.pi/4),-np.sin(np.pi/4),des_position[1]],[-1,0,0,des_position[2]],[0,0,0,1]]) 
q = r_limb.get_joint_angles()
# q = np.zeros(7)
T_curr = brk.FK[6](q)
# pose = r_limb.get_kdl_forward_position_kinematics()
# R = tf.transformations.quaternion_matrix(pose[3:])[0:3,0:3]
# position = pose[0:3]
# T_curr = np.append(R,position.reshape((3,1)) ,axis=1)
# T_curr = np.append(T_curr,[[0,0,0,1]],axis=0)

# q = r_limb.get_joint_angles()
# q = np.zeros(7)
counter = 0
while ((np.linalg.norm(T_des[0:3,3]- T_curr[0:3,3]) > 0.0001) 
    and np.linalg.norm(T_des[0:3,0] - T_curr[0:3,2]) > 0.0001 
    and (counter < 1000)):
    
    # get current pose
    # pose = r_limb.get_kdl_forward_position_kinematics()
    T_curr = brk.FK[6](q)
    # R = tf.transformations.quaternion_matrix(pose[3:])[0:3,0:3]
    # position = pose[0:3]
    # T_curr = np.append(R,position.reshape((3,1)) ,axis=1)
    # T_curr = np.append(T_curr,[[0,0,0,1]],axis=0)
    
    # J = r_limb.get_kdl_jacobian()
    J = brk.J[6](q)
    eye = np.zeros((3,3))
    eye[2,2] = 1
    TD = np.linalg.inv(T_curr) @ T_des
    # delta = np.append(TD[0:3,3],vex(TD[0:3,0:3] - np.eye(3)))
    delta = np.append(TD[0:3,3],vex(TD[0:3,0:3] - np.eye(3)) * np.array([0, 1, 1]))

    R2base = T_curr[0:3,0:3]

    # transform back to base
    top = np.append(R2base, np.zeros((3,3)),axis=1)
    bottom = np.append(np.zeros((3,3)), R2base,axis=1)
    together = np.append(top,bottom,axis=0)
    delta_base = together @ delta

    q = q + J.transpose() @ np.linalg.inv(J @ J.transpose() + (.07**2)*np.eye(6)) @ K_inv @ delta_base
    
    counter += 1
    print(counter)

joint_commands = []
# joint_commands.append(np.array([0, 0, 0, 0, 0, 0, 0]))
# joint_commands.append(np.array([0, -np.pi/4, 0, 0, 0, 0, 0]))
joint_commands.append(q)

control_rate = rospy.Rate(500)
r_limb.set_joint_position_speed(0.5)
 
for command in joint_commands:
    curr_pose = r_limb.get_joint_angles()

    error = np.abs(np.subtract(command,curr_pose))
    counter = 0
    while np.max(error) > .1:
        if counter > 3000:
            break
        counter += 1
        r_limb.set_joint_positions_mod(command)
        control_rate.sleep()

        curr_pose = r_limb.get_joint_angles()
        error = np.abs(np.subtract(command,curr_pose))
        # print(error)

