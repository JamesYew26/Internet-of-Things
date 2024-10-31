from time import *
from grovepi import *
from pyrebase import pyrebase
import datetime

ultrasonic = 7
pinMode (ultrasonic,"INPUT")

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
        sleep(1)
        distance = ultrasonicRead(ultrasonic)
        print(distance, 'cm')
        data = {"Distance":distance}
        time = str(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"))
        t = {"Timestamp":time}
        print(t)
        db.child("Test06Part3").push(data, user['idToken'])
        db.child("Test06Part3").push(t, user['idToken'])
    except KeyboardInterrupt:
        setText("Program Exited")
        break
    except TypeError:
        print("Type error occur")
    except IOError:
        print("IO Error occurs")

