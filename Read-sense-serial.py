import serial
def readSensors(x)
  with serial.Serial('/dev/ttyUSB0', 57600) as ser:
          x= ser.readline()
          l = x.rstrip()
          msgString = str(l)
          character = list(msgString)
          msg = ''.join(character[1:100])
          msg2 =  (msg.strip("'")).split(",")
          if msg2[0].strip("red: ") != "error":
              if msg2[1].strip("green: ") != "error":
                  if msg2[2].strip("yellow: ") != "error":
                      rawMsgRed =  float(msg2[0].strip("'red: "))
                      rawMsgGreen =  float(msg2[1].strip("green: "))
                      rawMsgYellow =  float(msg2[2].strip("yellow: "))
          else:
              print("error")
