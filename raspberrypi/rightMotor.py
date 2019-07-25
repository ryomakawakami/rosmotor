#!/usr/bin/env python

import motorLib as motor
import rospy
from std_msgs.msg import Int64

class RightMotorControl():
    def __init__(self, motor):
        self.motor = motor

        # Set up node
        rospy.init_node('right_motor_test')
        rospy.Subscriber('right_motor/cmd_vel', Int64, self.callback)
        rospy.loginfo('Ready')

    def control_main(self):
        rospy.spin()
        self.motor.stop()

    def callback(self, data):
        self.rpm = data.data
        self.duty = self.motor.setRPM(self.rpm)
        rospy.loginfo('RPM: ' + str(self.rpm))
        rospy.loginfo('Duty: ' + str(self.duty))

if __name__ == '__main__':
    right_motor = motor.Motor(port = [13, 19, 26])
    right_motor_control = RightMotorControl(right_motor)
    right_motor_control.control_main()
