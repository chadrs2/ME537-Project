#!/usr/bin/env python
import rospy
import tf
import numpy as np
from rad_baxter_limb import RadBaxterLimb
import baxter_interface
import baxter_left_kinematics as blk
import baxter_right_kinematics as brk

class WaterBalancer(object):
    def __init__(self):
        self.r_limb = RadBaxterLimb('right')
        self.r_limb.set_joint_position_speed(0.5)
        self.l_limb = RadBaxterLimb('left')
        self.l_limb.set_joint_position_speed(0.5)
        
        self.r_gripper = baxter_interface.Gripper('right')
        self.r_gripper.calibrate()
        self.l_gripper = baxter_interface.Gripper('left')
        self.l_gripper.calibrate()
        
        self.control_rate = rospy.Rate(50)

        self.current_configuration = np.array([0,0,0,0,0,0,0])
        self.target_configuration = np.array([0,0,0,0,0,0,0])

    def base_configuration(self):
        for i in range(3000):
            self.r_limb.set_joint_positions_mod(self.target_configuration)
            self.control_rate.sleep()

def main():
    rospy.loginfo("Initializing node... ")
    rospy.init_node("baxter_butler")
    rospy.loginfo("Activating both right and left arms & grippers... ")
    baxter_butler = WaterBalancer()
    rospy.loginfo("Moving to starting configuration... ")
    baxter_butler.base_configuration()
    
    while not rospy.is_shutdown():
        rospy.spin()

if __name__ == "__main__":
    main()