#include "HX711.h"

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
int r =1; //rounding number 
int i = 1;
void setup() {
  Serial.begin(57600);
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

}

void loop() {
  
  if (redscale.is_ready()) {
    int a = i++;
    redscale.set_scale(Rcalibration_factor);
    greenscale.set_scale(Gcalibration_factor);
    yellowscale.set_scale(Ycalibration_factor);
    //int redreading = (((round((redscale.read()/r)))*r - red_zero2));
    //int greenreading = (((round((greenscale.read()/r)))*r - green_zero2)*1);
    //int yellowreading = (((round((yellowscale.read()/r)))*r - yellow_zero2)*1);
    float redreading = redscale.get_units();
    float greenreading = greenscale.get_units();
    float yellowreading = yellowscale.get_units();
    //Serial.print(a);
    //Serial.print(",");
    Serial.print(redreading/2);
    Serial.print(",");
    Serial.print(greenreading/2);
    Serial.print(",");
    Serial.println(yellowreading/2);

  }
  delay(111);

}
