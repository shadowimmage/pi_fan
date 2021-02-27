#! /usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys
import os

# Configuration
DEBUG = True
FAN_PIN = 12   # BOARD Pin that drives the transistor base
WAIT_TIME = 5  # Seconds - Time to wait between refreshes
FAN_MIN = 40   # % - Duty cycle (valid 0-100)
PWM_FREQ = 60  # Hz - Change this value if the fan has strange behavior (default 25)
FAN_CURVE = [[50, 50], [60, 80], [70.0, 100]]  # Temp(C):Speed(%)

# Fan speed will change only if the difference in temperature is more than hysteresis setting
hyst = 2

# Setup GPIO Pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)
fan = GPIO.PWM(FAN_PIN, PWM_FREQ)
fan.start(0)


def getCpuTemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp_str = res.replace('temp=', '').replace('\'C\n', '')
    # debugging: print temp
    if DEBUG:
        print(f'Temp: {temp_str}c')
    return float(temp_str)


# Operational variables
cpu_temp = 0
cpu_last_temp = 0
fan_pwm = 0
fan_last_pwm = 0

try:
    while True:
        # Read the current CPU temperature
        cpu_temp = getCpuTemperature()
        # Make change to fan speed if temperature change is greater than hysteresis setting
        if abs(cpu_temp - cpu_last_temp) > hyst:
            # Calculate the desired fan speed
            #CASE below min temp
            if cpu_temp < FAN_CURVE[0][0]:
                fan_pwm = 0 #FAN OFF
            #CASE Max temp
            elif cpu_temp > FAN_CURVE[-1][0]:
                fan_pwm = FAN_CURVE[-1][1]
            #CASE Temp is between min and max
            else:
                # calculate using linear interpolation
                for i in range(len(FAN_CURVE)-1):
                    if cpu_temp >= FAN_CURVE[i][0] and cpu_temp <= FAN_CURVE[i+1][0]:
                        lo_temp = FAN_CURVE[i][0]
                        hi_temp = FAN_CURVE[i+1][0]
                        lo_pct = FAN_CURVE[i][1]
                        hi_pct = FAN_CURVE[i+1][1]

                        # calculate the percentage between lo and hi the cpu_temp is
                        step_temp_pct = round((cpu_temp - lo_temp) / (hi_temp - lo_temp), 1)
                        step_fan_pct = round((hi_pct - lo_pct) * step_temp_pct, 1)
                        fan_pwm = step_fan_pct + lo_pct
            # update cpu_temp_old for hysteresis
            cpu_last_temp = cpu_temp
        # Update pwm
        if fan_pwm != fan_last_pwm:
            fan.ChangeDutyCycle(fan_pwm)
            if DEBUG:
                print(f'Changed pwm from {fan_last_pwm} to {fan_pwm}')
            fan_last_pwm = fan_pwm
        else:
            if DEBUG:
                print('No change to pwm')
            
        # Wait until next refresh
        time.sleep(WAIT_TIME)

except KeyboardInterrupt:
    print('fan_ctrl.py interrupted. Cleaning up')
    GPIO.cleanup()
    sys.exit()
