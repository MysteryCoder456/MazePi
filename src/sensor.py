import RPi.GPIO as GPIO
import time


class Sensor:
    def __init__(self, trig_pin, echo_pin):
        self.trig = trig_pin
        self.echo = echo_pin

    def setup(self):
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def distance(self):
        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(0.0005)
        GPIO.output(self.trig, GPIO.LOW)

        while not GPIO.input(self.echo):
            start = time.time()

        while GPIO.input(self.echo):
            end = time.time()

        sig_time = end - start
        dist = sig_time / 0.000058
        return dist
