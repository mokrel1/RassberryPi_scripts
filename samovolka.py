import RPi.GPIO as GPIO
import time
DAC = [26, 19,13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)
for i in range(255):
    str = bin(i)
    print(str[2:(-1)])
    GPIO.output(DAC, int(str))
    time.sleep(0.5)
GPIO.output(DAC, 0)
GPIO.cleanup()