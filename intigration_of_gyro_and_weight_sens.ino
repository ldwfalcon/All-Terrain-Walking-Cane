
// This sketch shows how to configure the outp

#include <basicMPU6050.h>
#include "HX711.h"
#include <millisDelay.h>

//-- Input parameters:

// Gyro settings:
#define         LP_FILTER   3           // Low pass filter.           Value from 0 to 6
#define         GYRO_SENS   0           // Gyro sensitivity.          Value from 0 to 3
#define         ACCEL_SENS  3           // Accelerometer sensitivity. Value from 0 to 3

// Accelerometer offset:
constexpr int   AX_OFFSET =  552;       // Use these values to calibrate the accelerometer. The sensor should output 1.0g if held level.
constexpr int   AY_OFFSET = -241;       // These values are unlikely to be zero.
constexpr int   AZ_OFFSET = -3185;

// Output scale:
constexpr float AX_SCALE = 1;     // Multiplier for accelerometer outputs. Use this to calibrate the sensor. If unknown set to 1.
constexpr float AY_SCALE = 1;
constexpr float AZ_SCALE = 1;

constexpr float GX_SCALE = 0.99764;     // Multiplier to gyro outputs. Use this to calibrate the sensor. If unknown set to 1.
constexpr float GY_SCALE = 1.0;
constexpr float GZ_SCALE = 1.01037;

// Bias estimate:
#define         GYRO_BAND   35          // Standard deviation of the gyro signal. Gyro signals within this band (relative to the mean) are suppresed.   
#define         BIAS_COUNT  5000        // Samples of the mean of the gyro signal. Larger values provide better calibration but delay suppression response. 

//-- Set the template parameters:

basicMPU6050<LP_FILTER,  GYRO_SENS,  ACCEL_SENS,
             AX_OFFSET,  AY_OFFSET,  AZ_OFFSET,
             &AX_SCALE,  &AY_SCALE,  &AZ_SCALE,
             &GX_SCALE,  &GY_SCALE,  &GZ_SCALE,
             GYRO_BAND,  BIAS_COUNT
             >imu;

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
int r = 1; //rounding number
int i = 1;
const int red = 12;      // the number of the LED pin
const int redLow = 11;
const int black = 10;
const int blackLow = 9;
const int blue = 8;
const int blueLow = 7;
millisDelay realDelay;
int loopcountkeeper = 0;
int haslifted = 0; // var that keeps track of whether or not the cane has been lifted
class solenoidControl {
  public:
    void high() { //activate solenoids
      digitalWrite(red, HIGH);
      digitalWrite(black, HIGH);
      digitalWrite(blue, HIGH);
      digitalWrite(redLow, LOW);
      digitalWrite(blackLow, LOW);
      digitalWrite(blueLow, LOW);
    }
    void low() { //turn on "low power mode"
      digitalWrite(redLow, HIGH);
      digitalWrite(blackLow, HIGH);
      digitalWrite(blueLow, HIGH);
      digitalWrite(red, LOW);
      digitalWrite(black, LOW);
      digitalWrite(blue, LOW);
    }
    void off() { //turn off
      digitalWrite(red, LOW);
      digitalWrite(black, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(redLow, LOW);
      digitalWrite(blackLow, LOW);
      digitalWrite(blueLow, LOW);
    }
};
solenoidControl solCon;

class dataRead {
  public:
    void sol() {
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
        if (redreading > 2 && greenreading > 2) {
          haslifted = 1;
        }
        else if ((redreading > 2 or greenreading > 2) && (redreading < 2 or greenreading < 2) && haslifted == 1) {
          //can be used by storing data and names in a dictionary and array, then using that to now what solenoids to control.
          if (redreading < 2) {
            Serial.print(realDelay.justFinished());
            if (realDelay.remaining() == 0 && loopcountkeeper == 0) {
              digitalWrite(red, HIGH);
              realDelay.start(1000);
              loopcountkeeper = 1;
            }
            else if (realDelay.remaining() == 0 && loopcountkeeper == 1) {
             digitalWrite(redLow, HIGH);
             digitalWrite(red,LOW);

            }
          }
          if (greenreading < 2) {
            Serial.print(realDelay.justFinished());
            if (realDelay.remaining() == 0 && loopcountkeeper == 0) {
              digitalWrite(black, HIGH);
              realDelay.start(1000);
              loopcountkeeper = 1;
            }
            else if (realDelay.remaining() == 0 && loopcountkeeper == 1) {
             digitalWrite(blackLow, HIGH);
             digitalWrite(black,LOW);

            }
          }
        }
        else if (redreading < 2 && greenreading < 2) {
          solCon.off();
          if (realDelay.remaining() != 0) {
            realDelay.stop();
          }
          loopcountkeeper = 0;
          haslifted = 0;
        }

      }
    }
    void weight() {
      // Update gyro calibration
      if (redscale.is_ready()) {
        int a = i++;
        redscale.set_scale(Rcalibration_factor);
        greenscale.set_scale(Gcalibration_factor);
        yellowscale.set_scale(Ycalibration_factor);
        //int redreading = (((round((redscale.read()/r)))*r - red_zero2)); //for being dymb and calibrating HX711 without using the HX711 calibration from the HX711 library
        //int greenreading = (((round((greenscale.read()/r)))*r - green_zero2)*1);
        //int yellowreading = (((round((yellowscale.read()/r)))*r - yellow_zero2)*1);
        float redreading = redscale.get_units();
        float greenreading = greenscale.get_units();
        float yellowreading = yellowscale.get_units();
        //Serial.print(a);
        //Serial.print(" ");
        Serial.print(redreading / 2);
        Serial.print(" ");
        Serial.print(greenreading / 2);
        Serial.print(" ");
          Serial.println(yellowreading / 2);

      }
    }
    void gyro() {

      imu.updateBias();

      //-- Scaled and calibrated output:
      // Accel
      Serial.print(" ");
      Serial.print( imu.ax() );
      Serial.print( " " );
      Serial.print( imu.ay() );
      Serial.print( " " );
      Serial.print( imu.az() );
      Serial.print( " " );

      // Gyro
      Serial.print( imu.gx() );
      Serial.print( " " );
      Serial.print( imu.gy() );
      Serial.print( " " );
      Serial.print( imu.gz() );
      Serial.println();

    }
};
}
void setup() {
  // Set registers - Always required
  imu.setup();

  // Initial calibration of gyro
  imu.setBias();

  // Start console
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
  pinMode(red, OUTPUT);
  pinMode(redLow, OUTPUT);
  pinMode(black, OUTPUT);
  pinMode(blackLow, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(blueLow, OUTPUT);
}
dataRead dtr;
void loop() {

  dtr.weight();
  
  dtr.sol();

}
