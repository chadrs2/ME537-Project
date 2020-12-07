#!/usr/bin/env python
from numpy.core.defchararray import join
from genpy.message import DeserializationError
import rospy
import tf
import numpy as np
from rad_baxter_limb import RadBaxterLimb
import baxter_interface
import baxter_left_kinematics as blk
import baxter_right_kinematics as brk
import time

class WaterBalancer(object):
    def __init__(self):
        self.r_limb = RadBaxterLimb('right')
        self.r_limb.set_joint_position_speed(.5)
        # self.l_limb = RadBaxterLimb('left')
        # self.l_limb.set_joint_position_speed(0.5)
        
        self.r_gripper = baxter_interface.Gripper('right')
        self.r_gripper.calibrate()
        # self.l_gripper = baxter_interface.Gripper('left')
        # self.l_gripper.calibrate()
        
        self.control_rate = rospy.Rate(50)
        self.step_size = 1
        self.total_steps = 50
        self.current_configuration = np.array([0,0,0,0,0,0,0])
        self.target_configuration = np.array([0,0,0,0,0,0,0])
        self.current_pose = np.identity(4)
        self.target_pose = np.identity(4)
        self.obst_loc = np.array([1.1, -.5, .05])
        self.obst_rad = 0.25
        self.safety = self.obst_rad * 0.3 #1.0

    def calc_line_const(self, X0, X1, total_steps):
        [x0, y0, z0] = X0[:]
        [x1, y1, z1] = X1[:]

        # Line Equations: x=x0+at; y=y0+bt; z=z0+ct
        # Solve for a,b,c to know equation of line in 3D space
        a = (x1 - x0) / total_steps
        b = (y1 - y0) / total_steps
        c = (z1 - z0) / total_steps
        const = [a,b,c]
        return const

    def get_trajectory(self, points, step_size):
        # start_pos = [[R, t][0, 0, 0, 1]]
        X = []

        self.current_configuration = self.r_limb.get_joint_angles()
        self.current_pose = brk.FK[6](self.current_configuration)
        start_position = self.current_pose[:3,3]
        
        for des_position in points:
            if des_position == 'pause':
                X.append('pause')
                continue

            consts = self.calc_line_const(start_position, des_position, self.total_steps)

            for i in range(self.total_steps + 1):
                curr_row = []
                for j in range(len(consts)):
                    curr_row.append(start_position[j]+consts[j]*i*step_size)
                X.append(curr_row)

            start_position = des_position
        return X

    def find_corrected_position(self, next_position):
        corrected_position = next_position
        while (np.linalg.norm(np.subtract(corrected_position, self.obst_loc)) <= (self.obst_rad + self.safety)):
            corrected_position[2] = corrected_position[2] + 0.001

        return corrected_position

    def get_trajectory_w_obst_avoidance(self, points, step_size):
        # start_pos = [[R, t][0, 0, 0, 1]]
        X = []

        self.current_configuration = self.r_limb.get_joint_angles()
        self.current_pose = brk.FK[6](self.current_configuration)
        start_position = self.current_pose[:3,3]
        
        for des_position in points:
            if des_position == 'pause':
                X.append('pause')
                continue

            total_steps = self.total_steps
            t = 1            
            for counter in range(self.total_steps + 1):
                consts = self.calc_line_const(start_position, des_position, total_steps)
                next_position = []
                for j in range(len(consts)):
                    next_position.append(start_position[j] + consts[j] * t * step_size)

                if (np.linalg.norm(np.subtract(next_position, self.obst_loc)) > (self.obst_rad + self.safety)):
                    X.append(next_position)
                else: # if next position will cause the end effector to intercept with the object
                    corrected_position = self.find_corrected_position(next_position)
                    X.append(corrected_position)
                    # Reset parameters
                    start_position = corrected_position
                    total_steps = self.total_steps - (t - 1)
                    t = 1
                t = t +1
            
            start_position = des_position
        return X

    def move_to_configuration(self):
        curr_pose = self.r_limb.get_joint_angles()

        error = np.abs(np.subtract(self.target_configuration,curr_pose))
        counter = 0
        while np.max(error) > .1 and counter < 200:
            counter += 1
            self.r_limb.set_joint_positions_mod(self.target_configuration)
            self.control_rate.sleep()

            curr_pose = self.r_limb.get_joint_angles()
            error = np.abs(np.subtract(self.target_configuration,curr_pose))
            # print(error)
            # print(self.target_configuration)
            # print(curr_pose)
    
    def vex(self,S):
        if S.shape == (3,3):
            v = [S[2,1]-S[1,2], S[0,2]-S[2,0], S[1,0]-S[0,1]]
            v = [x * .5 for x in v]
            return v     
    
    def get_ikine(self,X):
        
        K_inv = .5*np.eye(6)
        
        q_prev = self.r_limb.get_joint_angles()
        joint_commands = []
        i = 0

        #for point in X:
        #    print(point)

        for point in X:
            if point == 'pause':
                joint_commands.append('pause')
                continue
            print("calculating: {} / {}".format(i,len(X)))
            i += 1
            T_des = np.array([[0,np.sin(np.pi/4),np.cos(np.pi/4),point[0]],[0,np.cos(np.pi/4),np.sin(np.pi/4),point[1]],[-1,0,0,point[2]],[0,0,0,1]])  
            q = q_prev
            T_curr = brk.FK[6](q)

            counter = 0
            while ((np.linalg.norm(T_des[0:3,3]- T_curr[0:3,3]) > 0.0001) 
                and np.linalg.norm(T_des[0:3,2] - T_curr[0:3,2]) > 0.0001 
                and (counter < 1000)):
                counter += 1  

                T_curr = brk.FK[6](q)
                J = brk.J[6](q)

                TD = np.matmul(np.linalg.inv(T_curr), T_des)
    
                delta = np.append(TD[0:3,3],self.vex(TD[0:3,0:3] - np.eye(3)) * np.array([0, 1, 1]))
                R2base = T_curr[0:3,0:3]

                top = np.append(R2base, np.zeros((3,3)),axis=1)
                bottom = np.append(np.zeros((3,3)), R2base,axis=1)
                together = np.append(top,bottom,axis=0)
                delta_base = np.matmul(together, delta)
                
                q = q + np.matmul(J.transpose(), np.matmul(np.linalg.inv(np.matmul(J, J.transpose()) + (.1**2)*np.eye(6)), np.matmul(K_inv, delta_base)))
                
                # q[0] = np.clip(q[0], -141*np.pi/180, 51*np.pi/180)
                # q[1] = np.clip(q[1], -123*np.pi/180, 60*np.pi/180)
                # q[2] = np.clip(q[2], -173*np.pi/180, 173*np.pi/180)
                # q[3] = np.clip(q[3], -3*np.pi/180, 150*np.pi/180)
                # q[4] = np.clip(q[4], -175*np.pi/180, 175*np.pi/180)
                # q[5] = np.clip(q[5], -90*np.pi/180, 120*np.pi/180)
                # q[6] = np.clip(q[6], -175*np.pi/180, 175*np.pi/180) 

                q[0] = np.clip(q[0], -90*np.pi/180, 100*np.pi/180)
                q[1] = np.clip(q[1], -65*np.pi/180, 60*np.pi/180)
                q[2] = np.clip(q[2], -170*np.pi/180, 170*np.pi/180)
                q[3] = np.clip(q[3], -0*np.pi/180, 140*np.pi/180)
                q[4] = np.clip(q[4], -175*np.pi/180, 175*np.pi/180)
                q[5] = np.clip(q[5], -90*np.pi/180, 120*np.pi/180)
                q[6] = np.clip(q[6], -175*np.pi/180, 175*np.pi/180) 

            joint_commands.append(q)
            q_prev = q
        return joint_commands

def main():
    rospy.loginfo("Initializing node... ")
    rospy.init_node("baxter_butler")
    rospy.loginfo("Activating both right and left arms & grippers... ")
    baxter_butler = WaterBalancer()
    
    rospy.loginfo("Moving to starting configuration... ")
    baxter_butler.move_to_configuration()
    
    points = []
    ## On Physical System
    # points.append([1.0, -.6, .8])
    #points.append([1.0, -.6, .3])
    points.append([1.0, -0.2, .2])
    points.append([1.1,0,.3])
    points.append([1.1,.21,-.2])
    points.append('pause')
    points.append([1.0,.15,.3])
    points.append([1.0,.15,.6])
    points.append([.9, -.5, .6])
    points.append([.8,-.8,.3])

    ## On Simulation
    #points.append([1.0, -.6, .3])
    #points.append([1.0,0,.3])
    #points.append([1.0,0,-.30]) # was -0.2; this is the location of the block in baxter's frame
    #points.append('pause')
    #points.append([1.0,0,.3])
    #points.append([1.0,.15,.6])
    #points.append([.9, -.5, .6])
    #points.append([.8,-.8,.3])
            
    X = baxter_butler.get_trajectory_w_obst_avoidance(points, baxter_butler.step_size)
    joint_commands = baxter_butler.get_ikine(X)  
    i = 0
    baxter_butler.r_gripper.open()
    for config in joint_commands:
        if config == 'pause':
            time.sleep(1)
            baxter_butler.r_gripper.close()
            time.sleep(1)
            continue
        i += 1
        baxter_butler.target_configuration = config
        baxter_butler.move_to_configuration()
        print("moving: {} / {}".format(i,len(joint_commands)))
    
    # Save X position matrix to later post-process a graph
    robot_pos = []
    real_robot_pos = []
    for configuration in joint_commands:
        if (configuration != 'pause'):
            robot_pos.append(brk.FK[6](configuration)[:3,3])
            #real_robot_pos.append(r_limb.get_kdl_forward_kinematics())
        
    X = np.array(X)
    np.save('baxter_position_data_w_object', X)
    #np.save('baxter_position_data_no_object', X)
    robot_pos = np.array(robot_pos)
    np.save('baxter_fk_position_data_w_object', robot_pos)
    #np.save('baxter_fk_position_data_no_object', robot_pos)

if __name__ == "__main__":
    main()