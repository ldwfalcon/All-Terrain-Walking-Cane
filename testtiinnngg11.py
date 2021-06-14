import serial
from time import sleep
tollRed = 1000
tollGreen = 1000
tollYellow = 1000

with serial.Serial('/dev/ttyUSB0', 57600) as ser:
    for i in range(10000000000000): #1trillion=max
        x= ser.readline()
        l = x.rstrip()
        print(x)
        msgString = str(l)
        character = list(msgString)
        msg = ''.join(character[1:100])
        msg =  msg.split(",")
        rawMsgRed =  msg2[0].strip("red: ")
        rawMsgGreen =  msg2[1].strip("green: ")
        rawMsgYellow =  msg2[2].strip("yellow: ")
        if i = 1:
            tolleranceQ = input("Do you want to change the tolerance of red, green or red.  Write the number you want it to be or keep them as Red:"+ tolRed +"Green:"+ tolGreen + "Yellow:"+ tolYellow + "or ] for no and seperate them with a coma.")
            splitTollAns = tolleranceQ.split(",")
            if splitTollAns[0] != "]":
                tollRed = splitTollAns[0]
            if splitTollAns[1] != "]":
                tollGreen = splitTollAns[1]
            if splitTollAns[2] != "]":
                tollYellow = splitTollAns[2]
            caneWeightCalComm = input("Remove the cane from the ground and type \")
            if caneWeightCalComm = "[":
                initLightMsgRed = rawMsgRed
                initLightMsgGreen = rawMsgGreen
                initLightMsgYellow = rawMsgYellow
            caneWeightCalComm = input("Place the cane on the ground and type \")
            if caneWeightCalComm = "]":
                initSelfMsgRed = rawMsgRed
                initSelfMsgGreen = rawMsgGreen
                initSelfMsgYellow = rawMsgYellow
        msgRed = rawMsgRed - initMsgRed
        msgGreen = rawMsgGreen - initMsgGreen
        msgYellow = rawMsgYellow - initMsgYellow
        if initSelfMsgRed < initLightMsgRed - tollRed:
                                      print("Red on ground")
        if initSelfMsgGreen < initLightMsgGreen - tollGreen:
                                      print("Green on ground")
        if initSelfMsgYellow < initLightMsgYellow - tollYellow:
                                      print("Yellow on ground")
        print(i,msgRed, msgGreen, msgYellow)
        sleep(.01)
    quit()
