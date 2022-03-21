import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
1

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    period = float(input('Задайте период '))
    while True:
        for num in range(256):
            GPIO.output(dac,  decimal2binary(num))
            time.sleep(period/510)
        for num in range(255, 1, -1):
            GPIO.output(dac,  decimal2binary(num))
            time.sleep(period/510)

        

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()