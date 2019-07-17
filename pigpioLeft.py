#!/usr/bin/env python

import pigpio
import time
import rospy
from std_msgs.msg import Int64

class LeftMotorControl():
  def __init__(self):
    # Initialize
    self.dir = True
    self.pin_pwm = 18
    self.pin_input1 = 20
    self.pin_input2 = 21

    # Set up node
    rospy.init_node('motor_test')
    rospy.Subscriber('left_motor/cmd_vel', Int64, self.callback)
    rospy.loginfo('Ready')

    # Set up GPIO
    pi.write(self.pin_input1, 0)
    pi.write(self.pin_input2, 0)

  def motor_main(self):
    rospy.spin()
    pi.stop()

  def callback(self, data):
    # Find duty
    self.rpm = data.data
    duty = self.rpm2duty(self.rpm)
    rospy.loginfo('RPM: ' + str(self.rpm))
    rospy.loginfo('Duty: ' + str(duty))

    # Set up direction
    if duty >= 0:
      self.dir = True
    else:
      self.dir = False
      duty = -duty

    if self.dir:
      pi.write(self.pin_input1, 1)
      pi.write(self.pin_input2, 0)
    else:
      pi.write(self.pin_input1, 0)
      pi.write(self.pin_input2, 1)

    # Set PWM
    rospy.loginfo('Updating motor speed')
    pi.set_PWM_dutycycle(self.pin_pwm, duty)

  # TODO: Add min speed
  def rpm2duty(self, rpm):
    d = rpm * 2.55 / 2.38
    if abs(d) > 100:
      if d > 0: d = 100
      else: d = -100
    return d

if __name__ == '__main__':
  pi = pigpio.pi()
  left = LeftMotorControl()
  left.motor_main()
