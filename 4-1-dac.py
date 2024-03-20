import RPi.GPIO as GPIO

dac = [8,11,7,1,0,5,12,6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while 1:
        value = input("Enter a number x, 0 <= x < 256")
        try:
            value = int(value)
            if 0 <= value < 256:
                GPIO.output(dac, decimal2binary(value))
                v = ((float)(value)/256.0) * 3.3
                print(f"Volt: {v:.4}v")
            else:
                if value < 0:
                    print("Enter a positive number")
                elif value > 255:
                    print("Input value is out of range")
                elif type(value) == float:
                    print("Enter an integer number")


        except Exception:

            if (value == "q"): break

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()



