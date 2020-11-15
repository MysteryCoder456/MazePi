import RPi.GPIO as GPIO


class CarController:
    def __init__(self, left_a, left_b, right_a, right_b):
        self.left_a = left_a
        self.left_b = left_b
        self.right_a = right_a
        self.right_b = right_b

    def setup(self):
        GPIO.setup(self.left_a, GPIO.OUT)
        GPIO.setup(self.left_b, GPIO.OUT)
        GPIO.setup(self.right_a, GPIO.OUT)
        GPIO.setup(self.right_b, GPIO.OUT)

    def left_forward(self):
        pass

    def right_forward(self):
        pass

    def left_backward(self):
        pass

    def right_backward(self):
        pass
