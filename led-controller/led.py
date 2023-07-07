# Pit Droid LED
# Author: Goran Vuksic

import RPi.GPIO as GPIO
from time import sleep

# set mode to BCM
GPIO.setmode(GPIO.BCM)

# define output pin
output_pin = 18

# GPIO setup
GPIO.setup(output_pin, GPIO.OUT)

# turn LED on
GPIO.output(output_pin, 1)
sleep(2)

# turn LED off
GPIO.output(output_pin, 0)
sleep(2)

# cleanup
GPIO.cleanup()