import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

def v_des(dac_value):
    return int(''.join(map(str, dac_value)), base = 2)

def adc():
    dac_value = [0,0,0,0,0,0,0,0]
    for k in range(0, 8):
        dac_value[k] = 1
        GPIO.output(dac, dac_value)
        time.sleep(0.0007)
        if GPIO.input(comp) == 0:
            dac_value[k] = 0
    return dac_value


def leds_output(dac):
    GPIO.output(leds, dac)


leds = [21,20,16,12,7,8,25,24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.OUT)
try:
    measure_data = []
    voltage = [0,0,0,0,0,0,0,0]
    start = time.time()
    GPIO.output(17, 1)
    while v_des(voltage) < (255*0.97):
        voltage = adc()
        measure_data.append(v_des(voltage))
        GPIO.output(leds, voltage)
        time.sleep(0.1)
    GPIO.output(17, 0)
    while v_des(voltage) > (255*0.02):
        voltage = adc()
        measure_data.append(v_des(voltage))
        GPIO.output(leds, voltage)
        time.sleep(0.1)
    end = time.time()
    time_exp = end - start
    
finally:
    plt.plot(measure_data)
    plt.show()
    measure_data_str = [str(item) for item in measure_data]
    with open('data.txt', 'w') as f:
        f.write('\n'.join(measure_data_str))
    GPIO.output(4,0)
    GPIO.output(17,0)
    GPIO.cleanup()