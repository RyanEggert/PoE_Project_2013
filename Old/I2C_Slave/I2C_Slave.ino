// Wire Slave Receiver
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Receives data as an I2C/TWI slave device
// Refer to the "Wire Master Writer" example for use with this

// Created 29 March 2006

// This example code is in the public domain.


#include <Wire.h>

char Message[15];
int MesRec=0; //Used to make the Arduino wait until initial data exchange has taken place


void setup()
{
  Wire.begin(4);                // join i2c bus with address #4
  Wire.onReceive(receiveEvent); // register event
  Serial.begin(9600);           // start serial for output

}

void loop()
{
  delay(100);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany)
{
  while(Wire.available()) // loop through all chars/numbers
  {
    char c = Wire.read(); // receive byte as a character
    Message += c; //Appends last received character to message
  }
  Serial.println(Message); //Prints received Message to serial port.
  Message=""; //Clears Message in anticipation of next data reception
  MesRec++
}
