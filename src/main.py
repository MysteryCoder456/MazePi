"""
All pin numbers are based on on Raspberry Pi 4B+ GPIO Layput. You can change these to your liking, but make sure to wire it up accordingly.
"""

import time
import RPi.GPIO as GPIO
from src.carcontroller import CarController
from src.sensor import Sensor

# This LED will be used to signal whether there is an error in the program during execution.
DEBUG_LED = 7

# These pins are to control the L298N module.
LA = 23
LB = 24
RA = 25
RB = 8

FRONT_TRIG = 17
FRONT_ECHO = 27


def main():
    # Initialize objects
    car_controller = CarController(LA, LB, RA, RB)
    sensor = Sensor(FRONT_TRIG, FRONT_ECHO)

    # Setup GPIO
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DEBUG_LED, GPIO.OUT)
    car_controller.setup()
    sensor.setup()

    # Start up sequence
    print("Starting...")
    for i in range(3):
        GPIO.output(DEBUG_LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(DEBUG_LED, GPIO.LOW)
        time.sleep(0.5)

    dist = sensor.distance()
    print(dist)

    # Cleanup GPIO
    GPIO.cleanup()
