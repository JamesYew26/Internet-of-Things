from time import *
from grovepi import *
from grove_rgb_lcd import *

dhtsensor = 7

pinMode(dhtsensor, "INPUT")

while True:
    try:
        sleep(0.5)
        [temp, hum] = dht(dhtsensor, 0)
        print("Temp = ",temp, '\u00b0C', " Hum = ", hum, " %")
        t = str(temp)
        h = str(hum)
        setRGB(218, 247, 166)
        setText("Temp = " + t + '\337' + "C    Hum = "+ h +" %")
    except KeyboardInterrupt:
        setText("Program Exited")
        break
    except TypeError:
        print("Type Error occurs")
    except IOError:
        print("IO Error occurs")
