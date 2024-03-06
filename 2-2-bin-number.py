import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0,0,0,0,0,0,0,0]
a = 5
i = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
if (a == 0):
    GPIO.output(dac, 0)
while (a > 0):
    number[7 - i] = a%2
    a//=2
    i = i+1

GPIO.output(dac, number)
time.sleep(20)

GPIO.output(dac, 0)
GPIO.cleanup()