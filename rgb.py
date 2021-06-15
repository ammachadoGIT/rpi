import RPi.GPIO as gpio
import distutils, sys

def lights(r,g,b):
    p2 = 2
    p3 = 3
    p4 = 4
    
    gpio.setmode(gpio.BCM)
    gpio.setup(p2, gpio.OUT)
    gpio.setup(p3, gpio.OUT)
    gpio.setup(p4, gpio.OUT)
    
    gpio.output(p2, bool(distutils.util.strtobool(r)))
    gpio.output(p3, bool(distutils.util.strtobool(g)))
    gpio.output(p4, bool(distutils.util.strtobool(b)))
		
if __name__ == "__main__":
    lights(sys.argv[0], sys.argv[1], sys.argv[2])