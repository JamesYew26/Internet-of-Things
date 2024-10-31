import time
import grovepi

rotaryangle=14
led1= 6
led2= 5

grovepi.pinMode(rotaryangle,"INPUT")
grovepi.pinMode(led1,"OUTPUT")
grovepi.pinMode(led2,"OUTPUT")
i=0

while True:
    try:
        time.sleep(0)
        i = grovepi.analogRead(rotaryangle)
        print(i)
        grovepi.analogWrite(led1,255-(i//4))
        grovepi.analogWrite(led2,i//4)
    except IOError:
            print("IO Error occurs")
            