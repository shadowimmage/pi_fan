#!/usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

FAN_PIN = 12
WAIT_TIME = 1
PWM_FREQ = 25

GPIO.setmode(GPIO.BOARD)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)

fan = GPIO.PWM(FAN_PIN, PWM_FREQ)
fan.start(0)


try:
  while 1:
    fan_speed = float(input('Fan Speed: '))
    fan.ChangeDutyCycle(fan_speed)

except(KeyboardInterrupt):
  print('interrupted')
  GPIO.cleanup()
  sys.exit()

