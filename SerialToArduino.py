##SerialToArduino.py

import serial #Import PySerial module
import time	  #Import time module

begin=2000	#Initialize variable used for confirming Arduino readiness


s=serial.Serial('COM5',9600) #Opening the serial port resets the Arduino. This waits for the Arduino to print 'Ready' to indicate that it has started and is prepared to send/recieve data.

print 'Port Opened'#Print confirmation that Pyserial has opened the serial port
	
while begin == 2000 :	
	begin=s.readline() #Waits to see that the Arduino has outputted a value to the serial port. This indicates that the Arduino has reset and is ready to recieve data

print 'Ready' #Print confirmation that the Arduino is ready to recieve data

for x in range(1,20):
	from random import randint
	rs=randint(0,255) #inclusive
	ls=randint(0,255)
	ld=randint(1,2)
	rd=randint(1,2)

	rightspeed=str(rs)
	leftspeed =str(ls)
	LeftDirection=str(ld)
	RightDirection=str(rd)

	RightSpeed=rightspeed.zfill(3)
	LeftSpeed=leftspeed.zfill(3)


	Transmission=RightSpeed+LeftSpeed+RightDirection+LeftDirection+chr(003)

	s.write(RightSpeed) #Write the new message to the serial port
	print "RightSpeed:" + RightSpeed #Print confirmation of sent message
	

	time.sleep(7)

s.close() #After data collection, the serial port is closed.
print 'Done' #"Done" is printed to verify a successful ending of the program.