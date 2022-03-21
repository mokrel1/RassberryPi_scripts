import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
PWM = GPIO.PWM(22, 1000)
PWM.start(0)
try:
    while True:
        num = int(input('Dute cycle '))
        PWM.ChangeDutyCycle(num)
        print(round(3.3*(int(num)/100), 2), 'B')

finally:
    GPIO.output(22,0)
    GPIO.cleanup()