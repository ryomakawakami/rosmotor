#!/usr/bin/env python

import math
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

        self.right_pub = rospy.Publisher('left_motor/cmd_vel', Int64, queue_size=10)
        self.left_pub = rospy.Publisher('right_motor/cmd_vel', Int64, queue_size=10)

    def main_TwistConverter(self):
        rospy.spin()

    def callback(self, message):
        self.received = message
        self.right, self.left = self.convert(self.received)

        self.right_pub.publish(self.right)
        self.left_pub.publish(self.left)

    def convert(self, data):
        wheel_size = 0.075
        axle_length = 0.35

        v = data.linear.x
        omega = received_data.angular.z

        v_r = (omega * axle_length + 2 * v) / 2
        v_l = (omega * axle_length - 2 * v) / (-2)

        v_r /= (wheel_size * 2 * math.pi)
        v_l /= (wheel_size * 2 * math.pi)

        rpm_r = 60 * v_r
        rpm_l = 60 * v_l

        return rpm_r, rpm_l

Converter = TwistConverter()
Converter.main_TwistConverter()
