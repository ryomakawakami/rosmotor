#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

def callback(data):
  twist = Twist()
  twist.linear.x = data.axes[1]
  twist.angular.x = data.axes[2]
  pub.publish(twist)

def joy2twist_main():
  global pub
  pub = rospy.Publisher('motor/twist/cmd_vel', Twist)
  rospy.Subscriber('joy', Joy, callback)
  rospy.init_node('joy2twist')
  rospy.spin()

if __name__ == '__main__':
  joy2twist_main()
