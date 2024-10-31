from time import *
from grovepi import *

ultrasonic = 7
relay = 6

pinMode (ultrasonic,"INPUT")
pinMode (relay,"OUTPUT")


while True:
    try:
        sleep(1)
        distance = ultrasonicRead(ultrasonic)
        print(distance, 'cm')
        if distance <= 10:
            digitalWrite(relay,1)
        else:
            digitalWrite(relay,0)
    except KeyboardInterrupt:
        digitalWrite(relay,0)
        break
    except TypeError:
        print("Type error occur")
    except IOError:
        print("IO Error occurs")
