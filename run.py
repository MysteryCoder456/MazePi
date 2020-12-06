import RPi.GPIO as GPIO
import src.main as run

if __name__ == "__main__":
    try:
        run.main()
    except KeyboardInterrupt:
        GPIO.cleanup()
