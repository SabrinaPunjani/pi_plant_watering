#import libraries
import time
import RPi.GPIO as GPIO


#Relay 1: GPIO 37, Relay 2: GPIO 38
GPIO.setmode(GPIO.BOARD)

GPIO.setup(37,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)



#Set up variables: internal in minutes, water in seconds
interval = 15
water = 3 #not much water needed for my plant 
 #watering
def watering():
    GPIO.output(37,True)
    time.sleep(water)
    GPIO.output(37,False)
try:
    while True:
        
        time.sleep(604800) #604800 seconds = 1 week
       
            
        
        watering()

finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()