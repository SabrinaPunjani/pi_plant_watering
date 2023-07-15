#import libraries
import time
import RPi.GPIO as GPIO
from picamera import PiCamera

#Relay 1: GPIO 37, Relay 2: GPIO 38
GPIO.setmode(GPIO.BOARD)

GPIO.setup(37,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)



#Set up variables: internal in minutes, water in seconds
interval = 15
water = 10
 #watering
def watering():
    GPIO.output(37,True)
    time.sleep(water)
    GPIO.output(37,False)
try:
    while True:
        
        time.sleep(5)
       
            
        
        watering()

finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()