import serial
output = []
def reqRawSens(a):
    output.clear()
    with serial.Serial('/dev/ttyUSB0', 57600) as ser:
          x= ser.readline()
          l = x.rstrip()
          msgString = str(l)
          character = list(msgString)
          msg = ''.join(character[1:100])
          msg2 =  (msg.strip("'")).split(",")
          redRawSensVal = msg2[1].strip("'red: ")
          greenRawSensVal = msg2[2].strip("green: ") 
          yellowRawSensVal = msg2[3].strip("yellow: ")
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
            
          requests = a.count(',') #counts how many commas there is in order to see how many items have been requested
          colorRequest = a.split(', ')
          for i in range(requests +1):  #will go through based on how many sensors were requested
                  if colorRequest[i] == 'red':
                      output.append(rawMsgRed) #adds the value requested to the final output
                  if colorRequest[i] == 'green':
                      output.append(rawMsgGreen)
                  if colorRequest[i] == 'yellow':
                      output.append(rawMsgYellow)
          return output #returns all the information requested as a list