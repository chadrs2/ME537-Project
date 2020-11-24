#!/usr/bin/env python

from torque_control_cor import torque_control
import rospy

def main():

    rospy.init_node("left_arm_controller")
    left = torque_control('left')
    left.run_torque_control()

if __name__ == '__main__':
    main()
