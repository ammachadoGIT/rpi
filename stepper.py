#!/usr/bin/python
# --------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#    Stepper Motor Test
#
# A simple script to control
# a stepper motor.
#
# Author : Matt Hawkins
# Date   : 28/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
# --------------------------------------

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [17, 22, 23, 24]

for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

Seq = [[1, 0, 0, 1],
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1]]

StepCount = len(Seq)
StepDir = 2  # Set to 1 or 2 for clockwise, Set to -1 or -2 for anti-clockwise

StepCounter = 0

while True:

    for pin in range(0, 4):
        xpin = StepPins[pin]
        GPIO.output(xpin, Seq[StepCounter][pin] != 0)

    StepCounter += StepDir

    # If we reach the end of the sequence
    # start again
    if (StepCounter >= StepCount):
        StepCounter = 0
    if (StepCounter < 0):
        StepCounter = StepCount+StepDir

    # Wait before moving on
    time.sleep(float(sys.argv[1]))
