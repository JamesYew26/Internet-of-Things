from time import*
from grovepi import*
from grove_rgb_lcd import*
from random import*
from urllib.request import*
from beebotte import*

led=3
soundsensor = 14
lightsensor = 15
dhtsensor = 16
pinMode(led, "OUTPUT")
pinMode(soundsensor, "INPUT")
pinMode(lightsensor, "INPUT")
pinMode(dhtsensor, "INPUT")
apikey = "oShjiZBBESYYUYckL4WkYFrR"
secretkey = "DoVnZaL6P4mfQnqQkzyEuKvqnipqzBgH"
bclient = BBT(apikey, secretkey)



while True:
    try:
        sleep(5)
        [temp, hum] = dht(dhtsensor, 0)
        light = analogRead(lightsensor)
        sound = analogRead(soundsensor)
        if temp is not "NaN" and hum is not "NaN" and light is not "NaN" and sound is not "NaN"
            print("Temp = %.2f, hum = %d, light = %d, sound = %d" %(temp, hum, light, sound))
            t = str(temp)
            h = str(hum)
            l = str(light)
            s = str(sound)
            setText("Temp = " + t + '\337' + "C    GAY = "+ h +" %"  )
            bclient.write('IoT_Test07', 'Temperature', temp)
            bclient.write('IoT_Test07', 'Humidity', hum)
            bclient.write('IoT_Test07', 'Light', light)
            bclient.write('IoT_Test07', 'Sound', sound)           
    except KeyboardInterrupt:
        setText("Program Exited")
        break
    except TypeError:
        print("Type Error occurs")
    except IOError:
        print("IO Error occurs")
