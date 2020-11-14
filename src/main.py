import RPi.GPIO as GPIO


def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()


def main():
    setup_gpio()
