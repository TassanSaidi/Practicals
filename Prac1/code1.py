#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: 
Student Number: 
Prac: 
Date: <03/08/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import itertools
#setting the numbering system to be used
GPIO.setmode(GPIO.BOARD)

#setting up GPIO pins for led and push buttons 
chan =[36,38,40]
#settung initial conditions for led pins
GPIO.setup(chan,GPIO.OUT, initial =GPIO.LOW)

#push buttons  will be conncted to pins 7 and 11 which will be pulled down to ground
GPIO.setup(7, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#declaring and intialising counting variable and the  list of possible led values
counter =0
outputV= list(itertools.product([0,1],repeat=3))

#definning function that will transverse through the outputV array depending on which button is pressed
def ledStream(channel):
#cheching to see if the up button is pressed
	if(GPIO.input(7)):
#counting up
		if(counter<7):
			counter+=1
			GPIO.output(chan,outputV[counter])
		else:
			counter=0
			GPIO.output(chan,outputV[counter])
	else:
#counting down
		if(counter>0):
			counter-=1
			GPIO.output(chan,outputV[counter])
		else:
			counter= 7
			GPIO.outout(chan, outputV[counter])
		
#defing function with the call baacks to handle the interrupt
def ledInterrupt():
#since pins 7 and 11 have been pulled down to ground, we are goung to be looking for risng edges when they are pressed
	GPIO.add_event_detect(7,GPIO.RISING, callback=ledStream,bouncetime=300)
	GPIO.add_event_detect(11,GPIO.RISING, callback=ledStream,bouncetime=300)
# Logic that you write
def main():
   # print("write your logic here")


# Only run the functions if 
if __name__ == "__main__":    
    try:
	ledInterrupt()
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)


