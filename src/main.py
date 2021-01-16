"""
All pin numbers are based on on Raspberry Pi 4B+ GPIO Layput. You can change these to your liking, but make sure to wire it up accordingly.
"""

import time
import RPi.GPIO as GPIO
from src.carcontroller import CarController
from src.sensor import Sensor

# This LED will be used to signal whether there is an error in the program during execution.
DEBUG_LED = 16

# These pins are to control the L298N module.
LA = 23
LB = 24
RA = 25
RB = 8

LEFT_TRIG = 17
LEFT_ECHO = 27

FRONT_TRIG = 22
FRONT_ECHO = 10

RIGHT_TRIG = 9
RIGHT_ECHO = 11

# Initialize objects
car_controller = CarController(LA, LB, RA, RB)
left_sensor = Sensor(LEFT_TRIG, LEFT_ECHO)
front_sensor = Sensor(FRONT_TRIG, FRONT_ECHO)
right_sensor = Sensor(RIGHT_TRIG, RIGHT_ECHO)


def main():
    # Setup GPIO
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DEBUG_LED, GPIO.OUT)
    car_controller.setup()
    left_sensor.setup()
    front_sensor.setup()
    right_sensor.setup()

    # Start up sequence
    print("Starting...")
    for _ in range(3):
        GPIO.output(DEBUG_LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(DEBUG_LED, GPIO.LOW)
        time.sleep(0.5)

    while True:
        time.sleep(0.05)
        left_dist = left_sensor.distance()
        front_dist = front_sensor.distance()
        right_dist = right_sensor.distance()
        print(left_dist, front_dist, right_dist)

