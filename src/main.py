"""
All pin numbers are based on on Raspberry Pi 4B+ GPIO Layput. You can change these to your liking, but make sure to wire it up accordingly.
"""

import RPi.GPIO as GPIO
from src.carcontroller import CarController

# These pins are to control the L298N module.
LA = 23
LB = 24
RA = 25
RB = 8


def main():
    # Initialize objects
    car_controller = CarController(LA, LB, RA, RB)

    # Setup GPIO
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    car_controller.setup()

    # Cleanup GPIO
    GPIO.cleanup()
