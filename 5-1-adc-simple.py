import RPi.GPIO as GPIO
import time

dac = [8,11,7,1,0,5,12,6]

comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for i in range (256):
        val = decimal2binary(i)
        GPIO.output(dac, val)
        comp_val = GPIO.input(comp)

        time.sleep(0.1)

        if (comp_val == 1):
            return i

    return 0

try:
    while 1:

        i = adc()
        voltage = (i/256) * 3.3
        if i: print(f"Volt: {voltage:.4}v")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()




