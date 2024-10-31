import time
import grovepi

pir_sensor = 8
motion = 0
grovepi.pinMode(pir_sensor,"INPUT")

while True:
    try:
        #Sense motion, usually human, within the target range.
        motion=grovepi.digitalRead(pir_sensor)
        #check if reads were 0 or 1 it can be 255 also because of IO Errors so remove those value
        if motion ==0 or motion==1:
            if motion==1:
                print('Motion Deteced')
            else:
                print('-')
        #if your hold time is less than this, you might not see as many detections
        time.sleep(.2)
    except IOError:
        print("Error")