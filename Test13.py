import serial
import grovepi
import time

buzzer = 2
grovepi.pinMode(buzzer, "OUTPUT")
#rpiser1=serial.Serial('/dev/ttyAMA0',
rpiser1 = serial.Serial('/dev/ttyS0',
                        baudrate=9600, timeout=1,
                        bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        xonxoff=False, rtscts=False, dsrdtr=False)
rpiser1.flushInput()
rpiser1.flushOutput()


try:
    print("Start")
    while True:
        s = rpiser1.read(14)
        if len(s) == "0232343030363344423541433603":
            print("Authorised access")
            grovepi.digitalWrite(buzzer,1)
            time.sleep(0.08)
            grovepi.digitalWrite(buzzer,0)
            time.sleep(0.08)
            grovepi.digitalWrite(buzzer,1)
            time.sleep(0.08)
            grovepi.digitalWrite(buzzer,0)
        #break
except KeyboardInterrupt:
    print("Program ended")
finally:
    grovepi.digitalWrite(buzzer, 0)