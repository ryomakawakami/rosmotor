#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

GPIO.output(38, 1)
GPIO.output(40, 0)

pwm = GPIO.PWM(12, 50)
pwm.start(0)

cmd = input("Enter duty cycle: ")

dir = True

while -100 <= cmd <= 100:

    if dir and cmd < 0:
        dir = False
        GPIO.output(38, 0)
        GPIO.output(40, 1)

    elif not dir and cmd > 0:
        dir = True
        GPIO.output(38, 1)
        GPIO.output(40, 0)

    if dir:
        pwm.ChangeDutyCycle(cmd)
    else:
        pwm.ChangeDutyCycle(-cmd)

    cmd = input()

GPIO.cleanup()
