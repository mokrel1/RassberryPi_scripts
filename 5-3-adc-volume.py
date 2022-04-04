import RPi.GPIO as GPIO
import time


def v_des(dac_value):
    return int(''.join(map(str, dac_value)), base = 2)


def ledsi(value):
    leds_values = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, ((v_des(adc())+8)//32)):
        leds_values[i] = 1
    return leds_values
        


def adc():
    dac_value = [0,0,0,0,0,0,0,0]
    for k in range(0, 8):
        dac_value[k] = 1
        GPIO.output(dac, dac_value)
        time.sleep(0.0007)
        if GPIO.input(comp) == 0:
            dac_value[k] = 0
    return dac_value
    


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.output(dac,  1)

try:
    while True:
        print(v_des(adc()), 3.3*(v_des(adc())/255))

        GPIO.output(leds, ledsi(v_des(adc())))
finally:
    GPIO.output(dac,0)
    GPIO.output(troyka,0)
    GPIO.cleanup()