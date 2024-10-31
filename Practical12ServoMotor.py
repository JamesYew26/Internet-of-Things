#Set up Libraries and overall settings
import RPi.GPIO as GPIO #Imports the standard Raspberry Pi GPIO library
from time import sleep #Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) #Sets the pin numbering system to use the physical layout

#Set up pin 32(GPIO12) for PWM
GPIO.setup(32, GPIO.OUT) # Sets up pin 11 to an output (instead of an input)
p = GPIO.PWM(32, 50) #Sets up pin 11 as a PWM Pin
p.start(0) #starts running PWM on the pin and sets it to 0

#Move the servo back and forth
p.ChangeDutyCycle(3) #changes the pulse width 3 (so move the servo)
sleep(1)  #wait 1 second
p.ChangeDutyCycle(12) #changes the pulse width to 12 (so moves the servo)
sleep(1)

#clean up everything
p.stop()   #At the end of the program, stop the PWM
GPIO.cleanup() #reset the GPIO pins back to defaults.