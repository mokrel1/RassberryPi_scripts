import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0,0,0,0,0,0,1,0]

numbers = [[1,1,1,1,1,1,1,1], [0,1,1,1,1,1,1,1], [0,1,0,0,0,0,0,0], [0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,1], [0,0,0,0,0,0,0,0]]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for i in numbers:
    GPIO.output(dac,i)
    time.sleep(15)

GPIO.output(dac,0)
GPIO.cleanup()