// MotorShieldTest.ino

#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

//Variables

char Incoming = 0; 	//Used to store the incoming character from the serial port
String IncDat;	//Used to store the incoming data from the serial port as a string 

long MotorSpeed = 0;

//Motor Shield

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *B08 = AFMS.getMotor(1); 	//Right Drive
Adafruit_DCMotor *B02 = AFMS.getMotor(2);	//Left Drive
Adafruit_DCMotor *B029 = AFMS.getMotor(3); 	//Domino Motor


//Functions

void RunMotors(long Speed) //Run two drive motors
{
	if (Speed==0)
	{
		B08->run(RELEASE);
		B02->run(RELEASE);
	}
	else
	{
		B08->setSpeed(Speed);
		B08->run(FORWARD);
		B02->setSpeed(Speed);
		B02->run(FORWARD);
	}

}





void setup() 
{	 
	AFMS.begin();	//Start motor shield
	Serial.begin(9600);	 //Open serial port

	IncDat.reserve(200); //Reserve 200 bytes for the incoming serial data

	B08->setSpeed(150); //Start both motors
	B08->run(FORWARD);
	B08->run(RELEASE);

	B02->setSpeed(150);
	B02->run(FORWARD);
	B02->run(RELEASE);

	B029->setSpeed(150);
	B029->run(FORWARD);
	B029->run(RELEASE);

	Serial.println("1500"); //Indicates to python that the Arduino is ready
						 //Windows Only?
}

void loop() 
{
	if (Serial.available())
	{
		while (Serial.available())
		{
			Incoming=Serial.read();

			if (Incoming==char(003))
			{
				MotorSpeed=IncDat.toInt(); //Converts IncDat to a long (if integers)
				IncDat=""; //Clear IncDat for next serial transmission
			}
			else
			{
				IncDat += Incoming; //Append most recent character to IncDat string
			}
		}
	}
	RunMotors(MotorSpeed);
}

//Look into serialEvent
//Would it make more sense to have serial checking in the void_loop 
//or would it make more sense to have it occur at the end of the void loop
//if serial data is detected? Will there be a difference?



