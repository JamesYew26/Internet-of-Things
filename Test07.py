from time import*
from grovepi import*
from grove_rgb_lcd import*
from random import*
from urllib.request import*
from beebotte import*
import grovepi

led=3
soundsensor = 14
lightsensor = 15
dhtsensor = 16
pinMode(led, "OUTPUT")
pinMode(soundsensor, "INPUT")
pinMode(lightsensor, "INPUT")
pinMode(dhtsensor, "INPUT")
apikey = "J5348MFEN6I2HO2M"
i = 0


while True:
    try:
        sleep(5)
        [temp, hum] = dht(dhtsensor, 0)
        light = analogRead(lightsensor)
        sound = analogRead(soundsensor)
        print("Temp = %.2f, hum = %d, light = %d, sound = %d" %(temp, hum, light, sound))
        t = str(temp)
        h = str(hum)
        l = str(light)
        s = str(sound)
        setText("Temp = " + t + '\337' + "C    Hum = "+ h +" %"  )
        i = grovepi.analogRead(soundsensor)
        grovepi.analogWrite(led, i // 4)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        setRGB(r, g, b)
        content = urlopen("https://api.thingspeak.com/update?api_key=" + apikey + "&field3=" + t +"&field1=" + s  + "&field2=" + l + "&field4=" + h).read()
        if (content):
            print("Updated Thingspeak")
        
    except KeyboardInterrupt:
        setText("Program Exited")
        break
    except TypeError:
        print("Type Error occurs")
    except IOError:
        print("IO Error occurs")