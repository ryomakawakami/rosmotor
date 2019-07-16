#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Int64

class motor_control():
  def __init__(self):
    # Initialize
    self.dir = True
    self.pin_pwm = 12
    self.pin_input1 = 38
    self.pin_input2 = 40
    self.frequency = 50

    # Set up node
    rospy.init_node('motor_test')
    rospy.Subscriber('left_motor/cmd_vel', Int64, self.callback)
    rospy.loginfo('Ready')

    # Set up GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.pin_pwm, GPIO.OUT)
    GPIO.setup(self.pin_input1, GPIO.OUT)
    GPIO.setup(self.pin_input2, GPIO.OUT)

    GPIO.output(self.pin_input1, 0)
    GPIO.output(self.pin_input2, 0)

    self.pwm = GPIO.PWM(self.pin_pwm, self.frequency)
    self.pwm.start(0)

  def motor_main(self):
    rospy.spin()
    GPIO.cleanup()
    self.pwm.stop()

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
      GPIO.output(self.pin_input1, 1)
      GPIO.output(self.pin_input2, 0)
    else:
      GPIO.output(self.pin_input1, 0)
      GPIO.output(self.pin_input2, 1)

    # Set PWM
    rospy.loginfo('Updating motor speed')
    self.pwm.ChangeDutyCycle(duty)

  # TODO: Add min speed
  def rpm2duty(self, rpm):
    d = rpm / 2.38
    if abs(d) > 100:
      if d > 0: d = 100
      else: d = -100
    return d

if __name__ == '__main__':
  Motor_Control = motor_control()
  Motor_Control.motor_main()
