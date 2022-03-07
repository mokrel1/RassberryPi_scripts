import RPi.GPIO as GPIO
import time
DAC = [26, 19,13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)
GPIO.output(DAC, number)
time.sleep(15)
GPIO.output(DAC, 0)
GPIO.cleanup()