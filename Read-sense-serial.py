import serial
def readSensors(a):
    with serial.Serial('/dev/ttyUSB0', 57600) as ser:
          x= ser.readline()
          l = x.rstrip()
          msgString = str(l)
          character = list(msgString)
          msg = ''.join(character[1:100])
          msg2 =  (msg.strip("'")).split(",")
          redRawSensVal = msg2[0].strip("'red: ")
          greenRawSensVal = msg2[1].strip("green: ")
          yellowRawSensVal = msg2[2].strip("yellow: ")
          #read red
          
          if redRawSensVal != "error":
              rawMsgRed =  float(redRawSensVal)#remove 'red: ' from string and co'
          else:
              print("Error with Red. ")
              
              #read green 
          if greenRawSensVal != "error":
              rawMsgGreen =  float(greenRawSensVal)
          else:
              print("Error with Green. ")
              
              #read yellow 
          if yellowRawSensVal != "error":
              rawMsgYellow =  float(yellowRawSensVal)
          else:
              print("Error with Yellow. ")
              

          if a.count(',') == 0:
              print('hi')
              if a == 'red':
                  print(rawMsgRed)
              if a == 'green':
                  print(rawMsgGreen)
              if a == 'yellow':
                  print(rawMsgYellow)
          if a.count(',') == 1:
              colorRequest = a.strip(', ')
              print('hi1')
              for i in range(2):
                  if a[i] == 'red':
                      print(rawMsgRed)
                  if a[i] == 'green':
                      print(rawMsgGreen)
                  if a[i] == 'yellow':
                      print(rawMsgYellow)
          if a.count(',') == 2:
              print('hi2')
              colorRequest = a.strip(', ')
              for i in range(3):
                  if a[i] == 'red':
                      print(rawMsgRed)
                  if a[i] == 'green':
                      print(rawMsgGreen)
                  if a[i] == 'yellow':
                      print(rawMsgYellow)
