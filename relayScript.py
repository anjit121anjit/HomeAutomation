import time

import RPi.GPIO as GPIO
from firebase import firebase
from firebase import jsonutil
from time import sleep

# setup with firebase..\

firebase = firebase.FirebaseApplication('https://anjithome.firebaseio.com/anjithome/')
apiKey = "AIzaSyA0V3aTM0Sp6TInakCYH0IrOTKmJqr3SNg"


# setup with GPIO with set warning
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# I have used 4 channel module so 4 different pin with GPIO pin number
pin1 =26
pin2 =16
pin3 =20
pin4 =12

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

while True:
    try:

    #ledObject = {"value":GPIO.LOW} # to set value but this is commented and we can tested without posting its value into the firebase.
    #ledObject2 = {"value":GPIO.HIGH}
    
    #GPIO.output(pin, GPIO.HIGH):
    #GPIO.output(pin, GPIO.HIGH)
    # I ask to get my firebase address where i mention below its child and make if statement if there is value called on this light will be on.
        if firebase.get("/myhome/light1","status") == 'on':
            print('Light 1 is on')
            GPIO.output(pin1, GPIO.LOW)
          
       # Otherwise channel will be off and print on screen its off.
        else:
            #firebase.get("sensors/led/0","value")== '0':
            GPIO.output(pin1, GPIO.HIGH)
            print ('Light 1 is off')
            
        if firebase.get("/myhome/light2","status") == 'on':
            print('Light 2 is on')
            GPIO.output(pin2, GPIO.LOW)
          
       
        else:
            #firebase.get("sensors/led/0","value")== '0':
            GPIO.output(pin2, GPIO.HIGH)
            print ('Light 2 is off')
            
        if firebase.get("/myhome/light3","status") == 'on':
            print('Light 3 is on')
            GPIO.output(pin3, GPIO.LOW)
          
       
        else:
            #firebase.get("sensors/led/0","value")== '0':
            GPIO.output(pin3, GPIO.HIGH)
            print ('Light 3 is off')
            
        if firebase.get("/myhome/light4","status") == 'on':
            print('Light 4 is on')
            GPIO.output(pin4, GPIO.LOW)
          
       
        else:
            #firebase.get("sensors/led/0","value")== '0':
            GPIO.output(pin4, GPIO.HIGH)
            print ('Light 4 is off')
            
    except KeyboardInterrupt:	# Turning all the LED off before stopping
       GPIO.output(pin1,GPIO.HIGH)
       GPIO.output(pin2,GPIO.HIGH)
       GPIO.output(pin3,GPIO.HIGH)
       GPIO.output(pin4,GPIO.HIGH)
       break
    except IOError:				# Print "Error" if communication error encountered
        print ("Error")
          
  
  
