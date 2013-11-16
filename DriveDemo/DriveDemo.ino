// DriveDemo.ino


#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *LEFT = AFMS.getMotor(1);
Adafruit_DCMotor *RIGHT = AFMS.getMotor(4);


void LRSpeed(byte LeftSpeed,byte RightSpeed)
{
    LEFT->setSpeed(LeftSpeed);
    RIGHT->setSpeed(RightSpeed);
}

void DriveMotors(byte LeftDirection, byte RightDirection)
{
    LEFT->run(LeftDirection);
    RIGHT->run(RightDirection);
}

void setup()
{
    AFMS.begin();
    LRSpeed(150,150);
    DriveMotors(1,1);
    DriveMotors(0,0);    
}

void loop() 
{
    // Go straight for 5 seconds
    LRSpeed(100,100);
    DriveMotors(2,2);
    delay(5000);
    // Make 90 degree turn
    LRSpeed(250,30); 
    delay(3930);
    LRSpeed(255,255);
    delay(2000);
    DriveMotors(1,2);
    delay(3500);
}

