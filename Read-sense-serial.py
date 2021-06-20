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
              

          if a.count(',') == 0: #if there are no ',' then only one HX711 value was requested
              if a == 'red':
                  print(rawMsgRed)
              elif a == 'green':
                  print(rawMsgGreen)
              elif a == 'yellow':
                  print(rawMsgYellow)
          if a.count(',') == 1: #if there is 1 ',' then two HX711 values were requested

              colorRequest = a.split(",") #split input at the commas
              print(colorRequest)
              for i in range(2):
                  if colorRequest[i] == 'red':
                      print(rawMsgRed)
                  if colorRequest[i] == 'green':
                      print(rawMsgGreen)
                  if colorRequest[i] == 'yellow':
                      print(rawMsgYellow)
          if a.count(',') == 2: #if there are 2 ',' then three HX711 values were requested
              colorRequest = a.split(', ')
              for i in range(3):
                  if colorRequest[i] == 'red':
                      print(rawMsgRed)
                  elif colorRequest[i] == 'green':
                      print(rawMsgGreen)
                  elif colorRequest[i] == 'yellow':
                      print(rawMsgYellow)
readSensors("red , red, yellow")

