import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
rang = range(255, 0, -1)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN) 

def dec2bin(val):
    return[int(elem) for elem in bin(val)[2:].zfill(8)]

def adc():
    i = 255
    val = 0
    while i > 1:
        GPIO.output(dac, dec2bin(val+i))
        time.sleep(0.1)
        if GPIO.input(comp) == GPIO.LOW:
            val += i
        i//=2
    return(val)

try:
    while True:
        vall = adc()/256*3.3
        

        print(f"Volt: {vall:.4}v")

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    
    GPIO.cleanup()

