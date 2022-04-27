#include "HX711.h"
#include "sensor_info.h"
// HX711 circuit wiring
const int LOADCELL_DOUT_PIN_RED = 13;
const int LOADCELL_SCK_PIN_RED = 6;
const int LOADCELL_DOUT_PIN_green = 5;
const int LOADCELL_SCK_PIN_green = 4;
const int LOADCELL_DOUT_PIN_yellow = 3;
const int LOADCELL_SCK_PIN_yellow = 2;
int red_zero2 = 0;
int green_zero2 = 0;
int yellow_zero2 = 0;

HX711 redscale;
HX711 greenscale;
HX711 yellowscale;

float Rcalibration_factor = 2230;
float Gcalibration_factor = 2230;
float Ycalibration_factor = 2230;

const int red = 12;      // the number of the LED pin
const int redLow = 11;
const int green = 10;
const int greenLow = 9;
const int yellow = 8;
const int yellowLow = 7;
float commander = 0;

void setup() {
  Serial.begin(57600);//57600
  redscale.begin(LOADCELL_DOUT_PIN_RED, LOADCELL_SCK_PIN_RED);
  greenscale.begin(LOADCELL_DOUT_PIN_green, LOADCELL_SCK_PIN_green);
  yellowscale.begin(LOADCELL_DOUT_PIN_yellow, LOADCELL_SCK_PIN_yellow);
  redscale.set_scale();
  greenscale.set_scale();
  yellowscale.set_scale();
  redscale.tare();
  greenscale.tare();
  yellowscale.tare();
  long Rzero_factor = redscale.read_average(); //Get a baseline reading
  long Gzero_factor = greenscale.read_average(); //Get a baseline reading
  long Yzero_factor = yellowscale.read_average(); //Get a baseline reading
  
  pinMode(red, OUTPUT);
  pinMode(redLow, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(greenLow, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(yellowLow, OUTPUT);
}

void loop() {
  //if (greenscale.is_ready()) {
    redscale.set_scale(Rcalibration_factor);
    greenscale.set_scale(Gcalibration_factor);
    yellowscale.set_scale(Ycalibration_factor);
    float redreading = redscale.get_units();
    float greenreading = greenscale.get_units();
    float yellowreading = yellowscale.get_units();
    Serial.print(redreading/2);
    Serial.print(",");
    Serial.print(greenreading/2);
    Serial.print(",");
    Serial.println(yellowreading/2);
    Serial.println(lockCheck(redreading));
    digitalWrite(red, lockCheck(redreading/2));
    digitalWrite(green, lockCheck(greenreading/2));
    digitalWrite(yellow, lockCheck(yellowreading/2));
  //}
  delay(111);
/*  
if(Serial.available()){
  char command = Serial.read();
  if(command == 'p')
    commander = 1;
   if(command == 'o')
    commander = 0;
} */
}
