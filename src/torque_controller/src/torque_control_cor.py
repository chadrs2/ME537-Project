#!/usr/bin/env python

# Copyright (c) 2014, Brigham Young University
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Brigham Young University nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY BRIGHAM YOUNG UNIVERSITY ''AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL BYU BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# \authors: Levi Rupert (Robotics and Dynamics Lab, BYU)
# \adviser: Marc Killpack (Robotics and Dynamics Lab, BYU)


import math
from collections import deque
from copy import deepcopy
import numpy as np
import time
import rospy
from std_msgs.msg import Empty
from std_msgs.msg import UInt16
from torque_controller.msg import q_cmd
from torque_controller.msg import k_cmd
from torque_controller.msg import imp_cmd


from  rad_baxter_limb.rad_baxter_limb import RadBaxterLimb
import baxter_interface


# Class torque_control requires the argument 'left' or 'right' to instanciate a left
# or right arm. It then will publish a torque command to the arm and subcribe to
# any thing published on three different topics.
# The first is  '<limb name>/joint_cmd' with type torque_controller.msg.q_cmd.q_array
# this is the desired joint angles given as an array of floats
# i.e. [s0, s1, e0, e1, w0, w1, w2]. 
# The second topic is 'kp' with type torque_controller.msg.k_cmd.k_array. This is an 
# array that is 49 varables long that is then reshaped into a 7x7 matrix. These
# are the stiffness gains for the "springs" of the arm. 
# The last topic is 'kd' with type torque_controller.msg.k_cmd.k_array. This is an
# array that is 49 varialbe long that is then reshaped into a 7x7 matrix. These
# are the damping gains for the "dampers" of the arm.
class torque_control():
    
    def __init__(self, limb_name, record = False, debug = False):
        self.name = limb_name 
        self.record = record
        self.debug = debug
        self.rate = 500 # hz rate of publishing torque commands
        self.missed_cmds = 20.0 # missed cycles before triggering timeout
        
# disable the cuff
        cuff_name = 'robot/limb/' + limb_name +'/suppress_cuff_interaction'
        self._pub_cuff_disable = rospy.Publisher(cuff_name, Empty)
        self.pub_joint_rate = rospy.Publisher('robot/joint_state_publish_rate', UInt16)

        self.limb = RadBaxterLimb(limb_name) #instanciate a limb
        self.joint_keys = self.limb.joint_names() #get the joint names 
        self.joint_names = { 0: 's0', 1: 's1', 2: 'e0', 3: 'e1', 4: 'w0', 5: 'w1', 6: 'w2'} 

# verify that the robot is enabled
        self.rs = baxter_interface.RobotEnable()
        self.init_state = self.rs.state().enabled
        self.start_up()
# need lock for q and qdot? or use q_buf = [] and q_key     joint_keys 
        self.q = None # will contain the joint angles
        self.tau_cor = [0,0,0,0,0,0,0]
        while self.q == None:
            self.update() #if no joint angles are know for the arm get the updated states
        self.kp = np.array(np.diag([80, 60, 20, 28, 8, 10, 6])) # define initial kp gains
        self.kd = np.array(np.diag([7.0, 8.0, 4.0, 7.0, 1.5, 1.5, 1.0])) #define intial kd gains
      #                             13.0 10.0
        self.cmd_ang = deepcopy(self.q) # set initial command angles to the current joint angles
        rospy.Subscriber(self.name+'/joint_cmd', q_cmd, self.qcallback) # subscribe to a joint angle publisher
        rospy.Subscriber('kp', k_cmd, self.kpcallback) # subscribe to a 'kp' gain publisher 
        rospy.Subscriber('kd', k_cmd, self.kdcallback) # subscribe to a 'kd' gain publisher 
        rospy.Subscriber(self.name + '/imp_cmd', imp_cmd, self.impcallback) # subscribe to a 'kd' gain publisher 
        
# callback for joint angle subscriber
    def qcallback(self, angles):
        self.cmd_ang = np.array(angles.q_array)

# callback for kp subscriber
    def kpcallback(self, kvals):
        self.kp = np.reshape(kvals.k_array, (7,7))

# callback for kd subscriber
    def kdcallback(self, kvals):
        self.kd = np.reshape(kvals.k_array, (7,7))

# callback for imp subscriber
    def impcallback(self, imp_vals):
        self.cmd_ang = np.array(imp_vals.q_array)
        self.tau_cor = np.array(imp_vals.tau_comp)

# start and enable the robot
    def start_up(self):
        print("enable robot...")    
        self.rs.enable()
        print ("done.")
        
    # this is used if position control is desired.
    def goto_pos(self):

        self.limb.set_joint_positions_mod(self.cmd_ang)
    
    #  exit torque control mode
    def clean_shutdown(self):
        self.limb.exit_control_mode()
      
    # method for moving arms to a neutral position
    def neutral(self):
        print("moiving arms to neutral postition")
        self.limb.move_to_neutral()

    # update the robots states   
    def update(self):

        # copy the joint angles
        #and
        # copy the joint velocities
 
        self.q = self.limb.get_joint_angles()
        self.q_dot = self.limb.get_filtered_joint_velocities()
        
    # calculate the torques to send
    def calc_torque(self):
        self.cmd_torque = np.dot(self.kp,(self.cmd_ang-self.q))-np.dot(self.kd, self.q_dot)

        print('Coriolis torque :\n', self.tau_cor, '\n\n')

        self.cmd_torque = self.cmd_torque #+ self.tau_cor

        print('Torques :\n', self.cmd_torque, '\n\n')

        if self.debug == True:
# Debugging Code: This prints out the intermediate and final calculations of the torque commands

            print("kp :")
            print((self.kp))
            print("\n")
            print("q :")
            print((self.q))
            print("\n")
            print("q_dot :")
            print((self.q_dot))
            print("\n")
            print("cmd_ang :")
            print((self.cmd_ang))
            print("\n")
            print("q-cmd ang :")
            print((self.q-self.cmd_ang))
            print("np.dot(self.kp,(self.q-self.cmd_ang))\n", np.dot(self.kp,(self.q-self.cmd_ang)))
            print("np.dot(self.kd, self.q_dot)\n", np.dot(self.kd, self.q_dot))
            print("result:\n", self.cmd_torque)

# send the torques
    def send_torque_cmd(self):
#        self.send_torque = self.cmd_torque.tolist()
 #       self.send_torques = dict()
  #      for indx, key in enumerate(self.joint_keys):
   #         self.send_torques[key] = self.send_torque[indx]
            
        self.limb.set_joint_torques(self.cmd_torque)
   
# run torque control untill an exit command is recieved
    def run_torque_control(self):
        control_rate = rospy.Rate(self.rate)
        # set a time out limit
        self.limb.set_command_timeout((1.0 / self.rate) * self.missed_cmds)  

        size = self.rate 
        rate_buf = deque()
        cur_time_old = time.time()
        while not rospy.is_shutdown():
            start = time.time()

            self.pub_joint_rate.publish(UInt16(self.rate))
            # make sure the publisher is working at an expected rate
            if not self.rs.state().enabled:
                rospy.logerr("Joint torque example failed to meet "
                             "specified control rate timeout.")
                break
            self.update()
            self.calc_torque()
            self.send_torque_cmd()

            control_rate.sleep()

            cur_time = time.time()
            cur_rate = 1/(cur_time - cur_time_old)
            if len(rate_buf) >= size:
                rate_buf.appendleft(cur_rate)
                rate_buf.pop()
            else:
                rate_buf.appendleft(cur_rate)
            #print len(rate_buf), '\n\n\n'  
            #print rate_buf, '\n\n\n'
            #print 'Rate :\n', cur_rate, '\n\n\n\n\n'
            #print 'Min Rate :\n', np.min(rate_buf), '\n\n\n\n\n'
            print('Mean Rate :\n', np.mean(rate_buf), '\n\n\n\n\n')
            cur_time_old = cur_time

        self.limb.exit_control_mode()
 
# run a position controller
    def run_pos_control(self):
        while not rospy.is_shutdown():
            control_rate = rospy.Rate(self.rate)
            self.update()
            self.goto_pos()

            # Debugging code
           # print("q :")
           # print(self.q)
           # print("\n")
           # print("cmd_ang :")
           # print(self.cmd_ang)
           # print("\n")
           # print("joint efforts :")
           # print(self.joint_efforts)
           # print("\n")
            
            control_rate.sleep()
            
        

def main():
 
    print("initializing node..")
    rospy.init_node("torque_control_keyboard")
    print("getting robot state...")

    left_controller = torque_control('left')
    right_controller = torque_control('right')
    #left_controller.run_pos_control()
    right_controller.run_pos_control()
    #left_controller.run_torque_control()
    
        
    
    
if __name__=='__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    
    
    
    
