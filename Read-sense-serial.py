import serial
def readSensors():
  with serial.Serial('/dev/ttyUSB0', 57600) as ser:
          x= ser.readline()
          l = x.rstrip()
          msgString = str(l)
          character = list(msgString)
          msg = ''.join(character[1:100])
          msg2 =  (msg.strip("'")).split(",")
          
          #ref read
          if msg2[0].strip("red: ") != "error":
              rawMsgRed =  float(msg2[0].strip("'red: "))#remove 'red: ' from string and co
          else:
              print("error")
              
              #green read
          if msg2[0].strip("red: ") != "error":
              rawMsgRed =  float(msg2[0].strip("'red: "))
          else:
              print("error")
              
              # yellow read
          if msg2[0].strip("red: ") != "error":
              rawMsgRed =  float(msg2[0].strip("'red: "))
          else:
              print("error")
def readRedx():
    

