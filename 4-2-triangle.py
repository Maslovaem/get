import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]

GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

temp = 1
out = 0

try:
    T = float(input("Enter period"))
    while 1:
        GPIO.output(dac, decimal2binary(out))

        v = (out/256)*3.3
        print(f"Volt: {v:.4}v")
        if out == 0: temp = 1
        elif out == 255: temp = 0

        if temp == 1:
            out = out + 1
        else: out = out - 1

        time.sleep(T/1000)

except ValueError:
    print("Enter another T value")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()





