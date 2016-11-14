#!/bin/python  
# Simple script for shutting down the raspberry Pi at the press of a button.  
# by Inderpreet Singh
# enhanced by droid41
#
# GPIO 23 Trigger for Shutdown
# GPIO 24 LED for acknowledge of trigger (please note that the led will
#         go out again before raspberry shutdown is completed.
#
# Add to startup:
# sudo nano /etc/rc.local
# >>
# sudo python /home/pi/Scripts/shutdown_pi.py &
# <<
  
import RPi.GPIO as GPIO  
import time  
import os  

inputPin = 23
outputPin = 24
 
# Use the Broadcom SOC Pin numbers  
# Setup the Pin with Internal pullups enabled and PIN in reading mode.  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(inputPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
GPIO.setup(outputPin, GPIO.OUT)

# Our function on what to do when the button is pressed  
def Shutdown(channel):  
    GPIO.output(outputPin, GPIO.HIGH)
    print("Shutting down!")
    os.system("sudo shutdown -h now")  
 
# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(inputPin, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  
GPIO.output(outputPin, GPIO.LOW)
 
# Now wait!  
while 1:  
    time.sleep(1)  
