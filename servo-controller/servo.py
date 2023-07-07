# Pit Droid servo
# Author: Goran Vuksic

import RPi.GPIO as GPIO
from time import sleep

# set mode to BOARD, pins are by numbers on board
GPIO.setmode(GPIO.BOARD)

# define output pin
output_pin = 33

# GPIO setup
GPIO.setup(output_pin, GPIO.OUT)

# start
servo=GPIO.PWM(33, 50)
servo.start(0)
sleep(1)

# move head left
servo.ChangeDutyCycle(5)
sleep(1)

# move head right
servo.ChangeDutyCycle(10)
sleep(1)

# stop and cleanup
servo.stop()
GPIO.cleanup()