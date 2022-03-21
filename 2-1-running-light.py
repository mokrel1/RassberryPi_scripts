import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

led_num = 0
for i in range(24):
    GPIO.output(leds[led_num],1)
    time.sleep(0.2)
    GPIO.output(leds[led_num],0)

    if led_num <= 6:
        led_num += 1
    else:
        led_num -= 7 

GPIO.output(leds,0)
GPIO.cleanup()