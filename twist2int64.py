#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int64

class Twist2int64():
  def __init__(self):
    self.command_left = Int64()
    self.command_right = Int64()
    self.received_twist = None
    rospy.init_node('Twist2int64')
    rospy.Subscriber('motor/twist/cmd_vel', Twist, self.callback)
    self.pub_right = rospy.Publisher('right_motor/cmd_vel', Int64, queue_size=10)
    self.pub_left = rospy.Publisher('left_motor/cmd_vel', Int64, queue_size=10)

  def twist2int64_main(self):
    rospy.spin()

  def callback(self, message):
    self.received_twist = message
    self.command_right, self.command_left = self.twist2rpm(self.received_twist)
    self.pub_right.publish(self.command_right)
    self.pub_left.publish(self.command_left)

  def twist2rpm(self, received_data):
    wheel_size = 0.04
    axle_length = 0.04

    v = received_data.linear.x
    omega = received_data.angular.z

    v_r = (omega*axle_length + 2*v)/2
    v_l = (omega*axle_length - 2*v)/(-2)

    v_r = v_r/(wheel_size * 2 * 3.14)
    v_l = v_l/(wheel_size * 2 * 3.14)

    rpm_r = 60 * v_r
    rpm_l = 60 * v_l

    return rpm_r, rpm_l

if __name__ == '__main__':
  twist2int64 = Twist2int64()
  twist2int64.twist2int64_main()
