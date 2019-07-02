#!/usr/bin/env python

import rospy
from geomtery_msgs.msg import Twist
from std_msgs.msg import Int64

class TwistConverter():
    def __init__(self):
        self.right = Int64()
        self.left = Int64()
        self.received = None

        rospy.init_node('TwistConverter')
        rospy.Subscriber('motor/twist/cmd_vel', Twist, self.callback)

        self.rightPub = rospy.Publisher('left_motor/cmd_vel', Int64, queue_size=10)
        self.leftPub = rospy.Publisher('right_motor/cmd_vel', Int64, queue_size=10)

    def main_twistConverter(self):
        rospy.spin()

    def callback(self, message):
        self.received = message
        self.right, self.left = self.convert(self.received)

        self.rightPub.publish(self.right)
        self.leftPub.publish(self.left)

    def convert(self, data):
        wheelSize = 0.075
        axleLength = 0.35

        v = data.linear.x
        omega = received_data.angular.z

        v_r = (omega * axleLength + 2 * v) / 2
        v_l = (omega * axleLength - 2 * v) / (-2)

        v_r /= (wheelSize * 2 * 3.14)
        v_l /= (wheelSize * 2 * 3.14)

        r_rpm = 60 * v_r
        l_rpm = 60 * v_l

        return r_rpm, l_rpm

Converter = TwistConverter()
Converter.main_TwistConverter()
