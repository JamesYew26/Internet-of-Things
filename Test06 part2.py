from pyrebase import pyrebase
import time
import math
from grovepi import*

button = 4
pinMode(button, "INPUT")

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
        time.sleep(0.5)
        b = digitalRead(button)
        if b:
            data = {"respond":"1"}
            db.child("Responses").push(data)
        else:
            print("0")
            data = {"respond":"0"}
            db.child("Responses").push(data)
    except KeyboardInterrupt:
        setText("Program Exited")
        break
    except IOError:
        print("IO Error occurs")
