import serial
def readSensors():
  with serial.Serial('/dev/ttyUSB0', 57600) as ser:
          x= ser.readline()
          l = x.rstrip()
          msgString = str(l)
          character = list(msgString)
          msg = ''.join(character[1:100])
          msg2 =  (msg.strip("'")).split(",")
          redRawSensVal = msg2[0].strip("'red: ")
          greenRawSensVal
          yellowRawSensVal
          #read red
          
          if redSense != "error":
              rawMsgRed =  float(redSens)#remove 'red: ' from string and co
          else:
              print("Error with Red. ")
              
              #read green 
          if msg2[1].strip("green: ") != "error":
              rawMsgGreen =  float(msg2[1].strip("green: "))
          else:
              print("Error with Green. ")
              
              #read yellow 
          if msg2[2].strip("yellow: ") != "error":
              rawMsgYellow =  float(msg2[2].strip("yellow: "))
          else:
              print("Error with Yellow. ")
readSensors()
