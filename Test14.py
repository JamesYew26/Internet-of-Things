import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from gpiozero import LED
import time
buzzer = LED(18)
reader = SimpleMFRC522()
try:
    while True:
        print("Place your tag")
        # Write
        reader.write("===YewJC===")
        #print("Successfully written")
        # Readc
        iden, text = reader.read()
        print(iden, " ", text)
        if str(iden) == "1037837343907": 
            print ("MASUK lah")
            buzzer.on()
            time.sleep(0.08)
            buzzer.off()
            time.sleep(0.08)
            buzzer.on()
            time.sleep(0.08)
            buzzer.off()
        else:
            buzzer.on()
            time.sleep(1)
            buzzer.off()
except KeyboardInterrupt:
    print("Program ended")
finally:
    buzzer.off()
    GPIO.cleanup()
