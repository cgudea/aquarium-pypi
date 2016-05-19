#!/bin/usr/env python
import RPi.GPIO as GPIO
import time
import os, sys

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
    print "Motion Detected!"
    with open("/sys/class/backlight/rpi_backlight/bl_power", 'w') as backlight:
        backlight.write("0")
        print "SCREEN ON SMARTIE"

    time.sleep(10)

    with open("/sys/class/backlight/rpi_backlight/bl_power", 'w') as backlight:
        backlight.write("1")
        print "SCREEN OFF DUMMY"

print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"
with open("/sys/class/backlight/rpi_backlight/bl_power", 'w') as backlight:
    backlight.write("1")
    print "SCREEN OFF DUMMY"

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print "Keyboard quit"
finally:
    GPIO.cleanup()
    with open("/sys/class/backlight/rpi_backlight/bl_power", 'w') as backlight:
        backlight.write("0")
        print "SCREEN ON SMARTIE"
