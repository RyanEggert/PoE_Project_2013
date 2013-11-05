##Import Modules

import serial #Import PySerial module
import time

##Functions

def InitializeSerial(): ##Initialize the Pi<-->Arduino serial link. serial 								object called "slink"
 	# Opening the serial port resets the Arduino. This waits for the Arduino to print 'Ready' to indicate that it has started and is prepared to send/recieve data
 	global slink  #Saves us from passing serial link into each function
	ArduinoReady=2000	#Initialize variable used for confirming Arduino readiness
	
	slink=serial.Serial('COM5',9600) 
	print 'Port Opened'#Print confirmation that Pyserial has opened the serial port
		
	while ArduinoReady == 2000 :	
		print ArduinoReady
		AR=slink.readline() #Waits to see that the Arduino has outputted a value to the serial port. This indicates that the Arduino has reset and is ready to recieve data

		try:	#Checks to see that the Arduino has outputted digits. Not just 				whitespace
			float(AR)
			ArduinoReady=AR
		except ValueError:
			ArduinoReady=2000

		print ArduinoReady

	print 'Ready' #Print confirmation that the Arduino is ready to recieve data

def Pi2Ard(rs,ls,ld,rd):	##Pi to Arduino serial communications
	rightspeed=str(rs)
	leftspeed =str(ls)
	LeftDirection=str(ld)
	RightDirection=str(rd)

	RightSpeed=rightspeed.zfill(3) #Fills in leading zeros so speed is always 3 digits
	LeftSpeed=leftspeed.zfill(3)

	Transmission=RightSpeed+LeftSpeed+RightDirection+LeftDirection+chr(003)

	slink.write(Transmission) #Write the new message to the serial port
	#print "Transmission : " + Transmission #Print confirmation of sent message

def CloseSerial():  ##Close Pi<-->Arduino serial link
	slink.write(str(00000000)+chr(003)) #release the motors when finished
	slink.close() #After data collection, the serial port is closed.
	print 'Serial Link Closed' #'Serial Link Closed' is printed to verify a successful closing of the serial connection

##Code

InitializeSerial()

print "in between"

Pi2Ard(150,150,1,1)

time.sleep(5)

CloseSerial

print "AllDone"

