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
int r =10000; //rounding number 

void setup() {
  Serial.begin(57600);
  redscale.begin(LOADCELL_DOUT_PIN_RED, LOADCELL_SCK_PIN_RED);
  greenscale.begin(LOADCELL_DOUT_PIN_green, LOADCELL_SCK_PIN_green);
  yellowscale.begin(LOADCELL_DOUT_PIN_yellow, LOADCELL_SCK_PIN_yellow);

}

void loop() {


  if (Serial.read() == 't') {
    delay(100);
     red_zero2 = redscale.read()/r*r;
     green_zero2 = greenscale.read()/r*r;
     yellow_zero2 = yellowscale.read()/r*r;
    Serial.println("taring");
    delay(100);
  }

  if (redscale.is_ready()) {
    int redreading = redscale.read()/r*r - red_zero2;
    Serial.print("red: ");
    Serial.print(redreading);
  } else {
    Serial.print("red: error");
  }
  if (greenscale.is_ready()) {
    int greenreading = greenscale.read()/r*r - green_zero2;
    Serial.print(", green: ");
    Serial.print(greenreading );
  } else {
    Serial.print(",green: error");
  }
  if (yellowscale.is_ready()) {
    int yellowreading = yellowscale.read()/r*r - yellow_zero2;
    Serial.print(", yellow: ");
    Serial.println(yellowreading);

  } else {
    Serial.println(",yellow: error");
  }
  delay(75);

}
