#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 50)
pwm.start(0)

cmd = input("Enter duty cycle: ")

while 0 <= cmd <= 100:
    pwm.ChangeDutyCycle(cmd)
    cmd = input()

GPIO.cleanup()
