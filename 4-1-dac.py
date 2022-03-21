import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
try:
    while True:
        num = (input())
        if num != "q":
            GPIO.output(dac,  decimal2binary((int(num))))
            print(round(3.3*(int(num)/255), 2), 'B')
        else:
            break
except RuntimeError:
    print('Вы превысили возможности 8-битового ЦАП')
except ValueError:
    print('Вы ввели не числовое значение')
except NameError:
    print('Вы ввели не целое значение')
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()