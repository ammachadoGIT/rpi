import RPi.GPIO as gpio
import time

def distance(measure='cm'):
    try:

        pin = 36
        pout = 32

        gpio.setmode(gpio.BOARD)
        gpio.setup(pout, gpio.OUT)
        gpio.setup(pin, gpio.IN)
        
        gpio.output(pout, True)
        
        while gpio.input(pin) == 0:
            nosig = time.time()

        while gpio.input(pin) == 1:
            print('reading...') 
            sig = time.time()

        tl = sig - nosig

        if measure == 'cm':
            distance = tl / 0.000058
        elif measure == 'in':
            distance = tl / 0.000148
        else:
            print('improper choice of measurement: in or cm')
            distance = None

        gpio.cleanup()
        return distance
    except:
        distance = 100
        gpio.cleanup()
        return distance

		
if __name__ == "__main__":
    print(distance('cm'))