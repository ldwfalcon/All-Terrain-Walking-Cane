import serial
def reqRawSens(a):
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
          global rawRed
          global rawGreen
          global rawYellow
          #read red   
          if redRawSensVal != "error":
              rawMsgRed =  float(redRawSensVal)#remove 'red: ' from string and co'
          else:
              print("Error with raw Red. ")
              
              #read green 
          if greenRawSensVal != "error":
              rawMsgGreen =  float(greenRawSensVal)
          else:
              print("Error with raw Green. ")
              
              #read yellow 
          if yellowRawSensVal != "error":
              rawMsgYellow =  float(yellowRawSensVal)
          else:
              print("Error with raw Yellow. ")
              

          if a.count(',') == 0: #if there are no ',' then only one HX711 value was requested
              if a == 'red':
                  rawRed = rawMsgRed
              elif a == 'green':
                  rawGreen = rawMsgGreen
              elif a == 'yellow':
                  rawYellow = rawMsgYellow
                  
          if a.count(',') == 1: #if there is 1 ',' then two HX711 values were requested
              colorRequest = a.split(', ') #split input at the commas
              for i in range(2):
                  if colorRequest[i] == 'red':
                      rawRed =rawMsgRed
                  if colorRequest[i] == 'green':
                      rawGreen = rawMsgGreen
                  if colorRequest[i] == 'yellow':
                      rawYellow = rawMsgYellow
                      
          if a.count(',') == 2: #if there are 2 ',' then three HX711 values were requested
              colorRequest = a.split(', ')
              for i in range(3):
                  if colorRequest[i] == 'red':
                      rawRed = rawMsgRed
                  if colorRequest[i] == 'green':
                      rawGreen = rawMsgGreen
                  if colorRequest[i] == 'yellow':
                      rawYellow = rawMsgYellow
                      
