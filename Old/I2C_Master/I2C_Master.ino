// Wire Master Writer
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Writes data to an I2C/TWI slave device
// Refer to the "Wire Slave Receiver" example for use with this

// Created 29 March 2006

// This example code is in the public domain.


#include <Wire.h>

int ping=2; //value to send to other Arduino to verify communications ability
int MesRec=0; //Used to make the Arduino wait until initial data exchange has taken place

void setup()
{
  Wire.begin(3); // join i2c bus (address optional for master)
  Wire.onReceive(receiveEvent); // register event 
  Wire.onRequest(dataRequested); 
  
  while (MesRec==0)
  {
    Wire.beginTransmission(4);
    Wire.write(ping);
    Wire.endTransmission();
  }
}

byte x = 0;

void loop()
{
  while 
  
  Wire.beginTransmission(4); // transmit to device #4
  Wire.write("x is ");        // sends five bytes
  Wire.write(x);              // sends one byte  
  Wire.endTransmission();    // stop transmitting

  x++;
  delay(500);
}


// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany)
{
  while(1 < Wire.available()) // loop through all but the last
  {
    char c = Wire.read(); // receive byte as a character
    Serial.print(c);         // print the character
  }
  int x = Wire.read();    // receive byte as an integer
  Serial.println(x);         // print the integer
  MesRec++
}


//function which is executed when the other Arduino requests data.
//registered in Wire.onRequest()

void dataRequested(ReqVar,)