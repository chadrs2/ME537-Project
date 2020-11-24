import rospy
import scipy.io as sio
from copy import deepcopy
from collections import deque
from baxter_interface.limb import Limb
import numpy as np
import time
from torque_controller.msg import q_cmd
import sys
from threading import RLock, Timer
from baxter_pykdl import baxter_kinematics as b_kin
#Old Parameters
# from baxter_left_dyn_params  import params as params_left
# from baxter_left_dynamics import M as M_left#, c_mat
# from baxter_left_dynamics import c as c_left#, c_mat
#New Parameters
# from new_baxter_left_dyn_params  import params as params_left
# from new_baxter_left_dyn_params  import fv as fv_left
# from new_baxter_left_dyn_params  import fc as fc_left
# from new_baxter_left_dynamics import M as M_left#, c_mat
# from new_baxter_left_dynamics import c as c_left#, c_mat
# from new_baxter_left_dynamics import f as f_left#, c_mat
# print('Loaded new Parameters for left arm')
# print "Left Arm Parameters:\n\n",params_left
# from baxter_right_dyn_params  import params as params_right
#from baxter_right_dynamics import M as M_right#, c_mat
# from baxter_right_dynamics import c as c_right#, c_mat
from std_msgs.msg import UInt16

class RadBaxterLimb(Limb):
    def __init__(self, limb_name, record = False, rate = 700):
        self.pub_joint_rate = rospy.Publisher('robot/joint_state_publish_rate', UInt16, queue_size = 100)    #hz rate that joint states publish at
        self.rate = rate
        self.pub_joint_rate.publish(UInt16(self.rate))
        # if limb_name == 'left':
        #     self.Mb = M_left
        #     self.c = c_left
        #     self.f = f_left
        #     self.params = params_left
        #     self.fv = fv_left
        #     try:
        #         self.fc = fc_left
        #     except NameError:
        #         pass
        # else:
        #     self.M = M_right
        #     self.c = c_right
        #     self.params = params_right
        self.kin_kdl = b_kin(limb_name)
        self.joint_keys = { 0: 's0', 1: 's1', 2: 'e0', 3: 'e1', 4: 'w0', 5: 'w1', 6: 'w2'}
        self.n_jts = 7 #number of joints for baxter
        self.limb_name = limb_name
        self.q_cur = None
        self.qd_cur = None
        self.record = record
        self.q_history = deque()
        self.qd_history = deque()
        self.time_history = deque()
        self.qd_part_hist = deque()

        self.w = deque()
        self.w.append(np.array([0,0,0,0,0,0,0]))
        self.w.append(np.array([0,0,0,0,0,0,0]))
        self.w.append(np.array([0,0,0,0,0,0,0]))

        self.pos = deque()
        self.pos.append(np.array([0,0,0,0,0,0,0]))
        self.pos.append(np.array([0,0,0,0,0,0,0]))
        self.pos.append(np.array([0,0,0,0,0,0,0]))
        self.count = 0
             
        self.s1 = 0.003621681514929
        self.s2 = 1
        self.b1 = 1
        self.b2 = 2
        self.b3 = 1
        self.a1 = 1
        self.a2 = -1.822694925196308
        self.a3 = 0.837181651256023

        self.i = 0;

        self.pub_filt_vel = rospy.Publisher(self.limb_name + '/filterd_qd', q_cmd, queue_size = 100) 

        Limb.__init__(self, limb_name)


    def get_joint_angles(self):
        
        #self.joint_angles() is a method of Limb
        self.q_dict_buf_cur = deepcopy(self.joint_angles())
            
        self.q_cur = np.array(self.joint_dict_to_list(self.q_dict_buf_cur))

        return self.q_cur

    def get_joint_velocities(self):
        
        #self.joint_velocities() is a method of Limb
        self.qd_dict_buf_cur = deepcopy(self.joint_velocities())
        

        self.qd_cur = np.array(self.joint_dict_to_list(self.qd_dict_buf_cur))

        return self.qd_cur
        
    def get_joint_efforts(self):

        #self.joint_efforts() is a method of Limb
        self.effort_dict_buf_cur = deepcopy(self.joint_efforts())

        self.effort_cur = np.array(self.joint_dict_to_list(self.effort_dict_buf_cur))

        return self.effort_cur


    def set_joint_positions_mod(self,positions,raw=False):
        # this will take a list of joint angles and turn it into a dictionary and the send it to the regular limb funtion
        positions_dict = dict()
        positions_dict = self.joint_list_to_dict(positions)
        #print 'Positions_dict :\n', positions_dict, '\n\n'

        self.set_joint_positions(positions_dict, raw)

    def set_joint_velocities_mod(self,velocities):
        # this will take a list of joint angles and turn it into a dictionary and the send it to the regular limb funtion
        velocities_dict = dict()
        velocities_dict = self.joint_list_to_dict(velocities)

        self.set_joint_velocites(velocities_dict)

    def set_joint_torques_mod(self, torques):
        # this will take a list of joint torques and turn it into a dictionary and the send it to the regular limb funtion
        """
        Commands the joints of this limb to the specified torques.

        B{IMPORTANT}: set_joint_torques must be commanded at a rate great than
        the timeout specified by set_command_timeout. If the timeout is
        exceeded before a new set_joint_torques command is received, the
        controller will switch modes back to position mode for safety purposes.


        """
        torques_dict = dict()
        torques_dict = self.joint_list_to_dict(torques)

        self.set_joint_torques(torques_dict)

        
    def joint_dict_to_list(self,data):
        buffer = []
        for i in list(self.joint_keys.keys()):
            buffer.append(data[self.limb_name + '_' + self.joint_keys[i]])

        
        return buffer
        
    def joint_list_to_dict(self,data):
        buffer = dict()
        for i in list(self.joint_keys.keys()):
            buffer[self.limb_name + '_' + self.joint_keys[i]] = data[i]

        return buffer

    def get_filtered_joint_angles(self):
       
        if self.count <= 3:
            self.count = self.count + 1
            self.q_dict_buf_cur = deepcopy(self.joint_angles())
            self.q_cur = np.array(self.joint_dict_to_list(self.q_dict_buf_cur))
            return self.q_cur
        else:

            q_filtered = (self.b1 * self.pos[2] + self.b2 * self.pos[1] + self.b3 * self.pos[0]) * self.s2

            return q_filtered

    def get_filtered_joint_velocities(self):
        qd_filtered = (self.b1 * self.w[2] + self.b2 * self.w[1] + self.b3 * self.w[0]) * self.s2
        
        return qd_filtered

    # def get_Mass(self):
    #     self.Mass = np.matrix(self.M(self.params, self.get_joint_angles())).reshape(self.n_jts, self.n_jts) # mass from sympybotics
        
    #     return self.Mass

    # def get_cor(self):
    #     self.coriolis = np.array(self.c(self.params, self.get_joint_angles().tolist(), self.get_filtered_joint_velocities().tolist()))
    #     return self.coriolis

    # def get_sympybotic_friction(self):
    #     self.friction = np.array(self.f(self.params, self.get_joint_angles().tolist(), self.get_filtered_joint_velocities().tolist()))
    #     return self.friction

    # def get_friction(self):
    #     try:
    #         self.friction = self.get_filtered_joint_velocities()*self.fv + self.fc*np.tanh(self.get_filtered_joint_velocities())
    #         return self.friction
    #     except NameError:
    #         self.friction = np.array(self.f(self.params, self.get_joint_angles().tolist(), self.get_filtered_joint_velocities().tolist()))
    #         return self.friction

    def get_kdl_car_inertia(self):
        return self.kin_kdl.cart_inertia()

    def get_kdl_forward_position_kinematics(self):
        return self.kin_kdl.forward_position_kinematics()

    def get_kdl_forward_velocity_kinematics(self):
        return self.kin_kdl.forward_velocity_kinematics()

    def get_kdl_inertia(self):
        return self.kin_kdl.inertia()

    def get_kdl_inverse_kinematics(self):
        return self.kin_kdl.inverse_kinematics()

    def get_kdl_jacobian(self):
        return self.kin_kdl.jacobian()

    def get_kdl_jacobian_pseudo_inverse(self):
        return self.kin_kdl.jacobian_pseudo_inverse()

    def get_kdl_jacobian_transpose(self):
        return self.kin_kdl.jacobian_transpose()

    def get_kdl_joints_to_kdl(self):
        return self.kin_kdl.joints_to_kdl()

    def get_kdl_kdl_to_mat(self):
        return self.kin_kdl.kdl_to_mat()

    def get_kdl_print_kdl_chain(self):
        return self.kin_kdl.print_kdl_chain()

    def get_kdl_print_robot_description(self):
        return self.kin_kdl.print_robot_description()


    def _on_joint_states(self, msg):
        self.pub_joint_rate.publish(UInt16(self.rate))
        for idx, name in enumerate(msg.name):
            if self.name in name:
                self._joint_angle[name] = msg.position[idx]
                self._joint_velocity[name] = msg.velocity[idx]
                self._joint_effort[name] = msg.effort[idx]

        if self.record == True:
            self.q_history.append(self.joint_dict_to_list(self._joint_angle))
            self.qd_history.append(self.joint_dict_to_list(self._joint_velocity))
            self.time_history.append(time.time())
              

        self.w.append((np.array([self._joint_velocity[self.limb_name + '_s0'], self._joint_velocity[self.limb_name + '_s1'], self._joint_velocity[self.limb_name + '_e0'], self._joint_velocity[self.limb_name + '_e1'], self._joint_velocity[self.limb_name + '_w0'], self._joint_velocity[self.limb_name + '_w1'], self._joint_velocity[self.limb_name + '_w2']]) *self.s1 - self.a2*self.w[2] - self.a3 * self.w[1]) * (1/self.a1))
        self.w.popleft()

        self.pos.append((np.array([self._joint_angle[self.limb_name + '_s0'], self._joint_angle[self.limb_name + '_s1'], self._joint_angle[self.limb_name + '_e0'], self._joint_angle[self.limb_name + '_e1'], self._joint_angle[self.limb_name + '_w0'], self._joint_angle[self.limb_name + '_w1'], self._joint_angle[self.limb_name + '_w2']]) * self.s1 - self.a2*self.pos[2] - self.a3 * self.pos[1]) * (1/self.a1))
        self.pos.popleft()
