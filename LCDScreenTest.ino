// LCD_Display.ino

#include <LiquidCrystal.h>
LiquidCrystal lcd(7,8,9,10,11,12); //Initialize LCD. Give data pin locations
int brightness = 255; //Enables changing the overall backlight brightness
int blRed=3;  //Red backlight pin
int blGrn=5;  //Green backlight pin
int blBlu=6;  //Blue backlight pin
int r=1; //Used to set 0-255 value for backlight red LED
int g=1; //Used to set 0-255 value for backlight green LED
int b=1; //Used to set 0-255 value for backlight blue LED

int rs=200;
int ls=145;


void setup() 
{
  Serial.begin(9600);
  Serial.println("I work");
  Serial.println(2+5);
}


void loop() 
{
}
