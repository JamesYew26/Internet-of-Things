import serial
import grovepi
import time
from pyrebase import pyrebase

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

#rpiser1=serial.Serial('/dev/ttyAMA0',
rpiser1 = serial.Serial('/dev/ttyS0',
                        baudrate=9600, timeout=1,
                        bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        xonxoff=False, rtscts=False, dsrdtr=False)
rpiser1.flushInput()
rpiser1.flushOutput()

# try:
#     mypet=db.child("MyPet").get()
#     for pet in mypet.each():
#         time.sleep(1)
#         a = pet.val()
#         x = a['ID']
#         print(x)
    
try:
    print("Start")
    s = rpiser1.read(14)
    if len(s)!= 0:
        print(s.hex())
        data = {"ID":(s.hex())}
        upload = db.child("MyPet").child("Lulu").set(data)

# try:
#     data1 = {"ID":"0232333030413437313244444203"}
#     results = db.child("MyPet").set(data1, user['idToken'])
#     p_id=db.child("MyPet").get()
#     print(p_id.val())
       

except KeyboardInterrupt:
    setText("Program Exited")