import serial
from time import sleep

with serial.Serial('/dev/ttyUSB0', 57600) as ser:
    for i in range(10000000000000): #1trillion=max
        x= ser.readline()
        l = x.rstrip()
        print(x)
        msgString = str(l)
        character = list(msgString)
        message = ''.join(character[1:100])
        message2 =  message.split(",")
        messageRed =  message2[0].strip("red: ")
        messageGreen =  message2[1].strip("green: ")
        messageYellow =  message2[2].strip("yellow: ")
        print(i,messageRed, messageGreen, messageYellow)
        sleep(.5)
    quit()
