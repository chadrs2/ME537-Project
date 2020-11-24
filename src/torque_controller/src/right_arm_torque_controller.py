#!/usr/bin/env python

from torque_control import torque_control
import rospy

def main():

    rospy.init_node("right_arm_controller")
    right = torque_control('right')
    right.run_torque_control()

if __name__ == '__main__':
    main()
