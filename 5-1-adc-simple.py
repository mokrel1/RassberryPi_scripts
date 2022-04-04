import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():
    value = 0
    for i in range(256):
        GPIO.output(dac,  decimal2binary(i))
        value = i
        time.sleep(0.0007)
        if GPIO.input(comp) == 0:
            return value

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.output(dac,  1)

try:
    while True:
        print(adc(), 3.3*(adc()/255))
finally:
    GPIO.output(dac,0)
    GPIO.output(troyka,0)
    GPIO.cleanup()