from time import*
from grovepi import*
from grove_rgb_lcd import*
from pyrebase import pyrebase

dhtsensor = 7

pinMode(dhtsensor, "INPUT")


config={
    "apiKey": "AIzaSyDSVKWrU1Eqn0-C8BoJOXIKZGm11UcuFsQ",
    "authDomain": "iot-firebase-df0be.firebaseapp.com",
    "databaseURL": "https://iot-firebase-df0be-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "iot-firebase-df0be.appspot.com"
    }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("junchee0206@gmail.com", "JunChee26_")
db = firebase.database()

while True:
    try:
        sleep(5)
        [temp, hum] = dht(dhtsensor,0)
        print("Temp = ",temp, '\u00b0C', " Hum = ", hum, " %")
        t = str(temp)
        h = str(hum)
        setRGB(218, 247, 166)
        
        data1 = {"temperature":t}
        data2 = {"humidity":h}
        results = db.child("PI_001").update(data1, user['idToken'])
        results = db.child("PI_001").update(data2, user['idToken'])
        break
    except KeyboardInterrupt:
        setText("Program Exited")
        break
    except TypeError:
        print("Type Error occurs")
    except IOError:
        print("IO Error occurs")