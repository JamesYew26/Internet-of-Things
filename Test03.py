import time
import math
import grovepi
from grovepi import *

buzzer = 6
button = 8
pinMode (buzzer,"OUTPUT")
pinMode (button,"INPUT")

while True:
    try:
        time.sleep(0.25)
        b = digitalRead(button)
        if b:
            grovepi.analogWrite(buzzer,80)
            time.sleep(0.5)
            grovepi.analogWrite(buzzer,50)
            time.sleep(0.25)
            grovepi.analogWrite(buzzer,30)
            time.sleep(0.25)
            grovepi.analogWrite(buzzer,10)
            time.sleep(0.25)
        else:
            digitalWrite(buzzer,0)
    except KeyboardInterrupt:
        digitalWrite(buzzer,0)
        break
    except IOError:
        print("IO Error occurs")
