# Import Modules

import serial  # Import PySerial module
import time
from random import randint
# Functions

# Initialize the Pi<-->Arduino serial link. serial
# object called "slink"


def InitializeSerial(sp):
    # Opening the serial port resets the Arduino. This waits for the Arduino
    # to print 'Ready' to indicate that it has started and is prepared to
    # send/recieve data
    global slink  # Saves us from passing serial link into each function
    # Initialize variable used for confirming Arduino readiness
    ArduinoReady = 2000

    slink = serial.Serial(sp, 9600)
    # Print confirmation that Pyserial has opened the serial port
    print 'Port Opened'

    while ArduinoReady == 2000:
        print ArduinoReady
        # Waits to see that the Arduino has outputted a value to the serial
        # port. This indicates that the Arduino has reset and is ready to
        # recieve data
        AR = slink.readline()

        # Checks to see that the Arduino has outputted digits. Not just
        # whitespace
        try:
            float(AR)
            ArduinoReady = AR
        except ValueError:
            ArduinoReady = 2000

        print ArduinoReady

    # Print confirmation that the Arduino is ready to recieve data
    print 'Ready'


def Pi2Ard(rs, ls, ld, rd):  # Pi to Arduino serial communications
    rightspeed = str(rs)
    leftspeed = str(ls)
    LeftDirection = str(ld)
    RightDirection = str(rd)

    # Fills in leading zeros so speed is always 3 digits
    RightSpeed = rightspeed.zfill(3)
    LeftSpeed = leftspeed.zfill(3)

    Transmission = RightSpeed + LeftSpeed + RightDirection + LeftDirection + chr(003)

    slink.write(Transmission)  # Write the new message to the serial port
    # Print confirmation of sent message
    print "Transmission : " + Transmission


def CloseSerial():  # Stop drive motors & close Pi<-->Arduino serial link
    slink.write(str(00000000) + chr(003))  # release the motors when finished
    slink.close()  # After data collection, the serial port is closed.
    #'Serial Link Closed' is printed to verify a successful closing of the
    # serial connection
    print 'Serial Link Closed'

# Variable Declaration

SerialPort = 'COM6'

# Code

InitializeSerial(SerialPort)

for x in range(1,10):
	Pi2Ard(randint(100,255), randint(100,255), 2, 2)
	time.sleep(3)



CloseSerial()

print "All Done"
