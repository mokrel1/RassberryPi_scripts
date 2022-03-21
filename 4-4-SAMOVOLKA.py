import RPi.GPIO as GPIO
import time
leds = [21,20,16,12,7,8,25,24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
try:
    while True:
        PWM = GPIO.PWM(24, 1000)
        PWM.start(0)
        for k in range(1, 101):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        for k in reversed(range(1, 101)):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        PWM = GPIO.PWM(25, 1000)
        PWM.start(0)
        for k in range(1, 101):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        for k in reversed(range(1, 101)):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        PWM = GPIO.PWM(8, 1000)
        PWM.start(0)
        for k in range(1, 101):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        for k in reversed(range(1, 101)):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        PWM = GPIO.PWM(7, 1000)
        PWM.start(0)
        for k in range(1, 101):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        for k in reversed(range(1, 101)):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        PWM = GPIO.PWM(12, 1000)
        PWM.start(0)
        for k in range(1, 101):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        for k in reversed(range(1, 101)):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        PWM = GPIO.PWM(16, 1000)
        PWM.start(0)
        for k in range(1, 101):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        for k in reversed(range(1, 101)):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        PWM = GPIO.PWM(20, 1000)
        PWM.start(0)
        for k in range(1, 101):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        for k in reversed(range(1, 101)):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        PWM = GPIO.PWM(21, 1000)
        PWM.start(0)
        for k in range(1, 101):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
        for k in reversed(range(1, 101)):
            PWM.ChangeDutyCycle(k)
            time.sleep(0.005)
finally:
    GPIO.output(21,0)
    GPIO.cleanup()