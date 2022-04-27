#include "sensor_info.h"
int lockCheck(int a)
{
  if(a > 2 or a < -2)
    return HIGH;
  else
    return LOW;
}
