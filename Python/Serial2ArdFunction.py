##Import Modules


import serial #Import PySerial module

##Functions


def InitializeSerial(): ##Initialize the Pi<-->Arduino serial link. serial object called "slink"
 	# Opening the serial port resets the Arduino. This waits for the Arduino to print 'Ready' to indicate that it has started and is prepared to send/recieve data

	ArduinoReady=2000	#Initialize variable used for confirming Arduino readiness

	print 'Port Opened'#Print confirmation that Pyserial has opened the serial port
		
	while ArduinoReady == 2000 :	
		ArduinoReady=slink.readline() #Waits to see that the Arduino has outputted a value to the serial port. This indicates that the Arduino has reset and is ready to recieve data

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
	print "Transmission : " + Transmission #Print confirmation of sent message

def CloseSerial():  ##Close Pi<-->Arduino serial link
	slink.write(str(00000000)+chr(003)) #release the motors when finished
	slink.close() #After data collection, the serial port is closed.
	print 'Done' #"Done" is printed to verify a successful ending of the program.

##Code


global slink  #Saves us from passing serial link into each function
slink=serial.Serial('COM5',9600) #Follow immediately with InitializeSerial()
InitializeSerial()

Pi2Ard()

CloseSerial



