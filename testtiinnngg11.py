import serial
from time import sleep
tollRed = 1000
tollGreen = 1000
tollYellow = 1000

with serial.Serial('/dev/ttyUSB0', 57600) as ser:
    for i in range(10000000000000): #1trillion=max
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
        if i == 0:
            tolleranceQ = input("Do you want to change the tolerance of red, green or red.  Write the number you want it to be or keep them as Red:"+ str(tollRed) +"Green:"+ str(tollGreen) + "Yellow:"+ str(tollYellow) + "or ] for no and seperate them with a coma.")
            splitTollAns = tolleranceQ.split(",")
            if splitTollAns[0] != "]":
                tollRed = splitTollAns[0]
            if splitTollAns[1] != "]":
                tollGreen = splitTollAns[1]
            if splitTollAns[2] != "]":
                tollYellow = splitTollAns[2]
            caneWeightCalComm = input("Remove the cane from the ground and type ]")
            if caneWeightCalComm == "]":
                x1= ser.readline()
                l1 = x1.rstrip()
                msgString1 = str(l1)
                character1 = list(msgString1)
                msg3 = ''.join(character1[1:100])
                msg5 =  (msg3.strip("'")).split(",")
                rawMsgRed1 =  msg5[0].strip("red: ")
                rawMsgGreen1 =  msg5[1].strip("green: ")
                rawMsgYellow1 =  msg5[2].strip("yellow: ")
                initLightMsgRed = float(rawMsgRed1)
                initLightMsgGreen = float(rawMsgGreen1)
                initLightMsgYellow = float(rawMsgYellow1)
            caneWeightCalComm = input("Place the cane on the ground and type ]")
            if caneWeightCalComm == "]":
                x2= ser.readline()
                l2 = x2.rstrip()
                msgString2 = str(l2)
                character2 = list(msgString2)
                msg4 = ''.join(character2[1:100])
                msg6 =  (msg4.strip("'")).split(",")
                rawMsgRed2 =  msg6[0].strip("'red: ")
                rawMsgGreen2 =  msg6[1].strip("green: ")
                rawMsgYellow2 =  msg6[2].strip("yellow: ")
                initSelfMsgRed = float(rawMsgRed2)
                initSelfMsgGreen = float(rawMsgGreen2)
                initSelfMsgYellow = float(rawMsgYellow2)
            print("Calibration has been completed! Here are the results: \n")
            resultsTable = ["Red", "Green", "Yellow"]
            resultsTable2 = ["Light", "Cane", "Tollerance"]
            data = [[initLightMsgRed, initLightMsgGreen, initLightMsgYellow],
            [initSelfMsgRed, initSelfMsgGreen, initSelfMsgYellow],
            [tollRed, tollGreen, tollYellow]]
            format_row = "{:>12}" * (len(resultsTable) + 1)
            print(format_row.format("", *resultsTable))
            for data, row in zip(resultsTable2, data):
                print(format_row.format(data, *row))
            sleep(4)
            x= ser.readline()
            l = x.rstrip()
            msgString = str(l)
            character = list(msgString)
            msg = ''.join(character[1:100])
            msg2 =  (msg.strip("'")).split(",")
            rawMsgRed3 =  msg2[0].strip("'red: ")
            rawMsgGreen3 =  msg2[1].strip("green: ")
            rawMsgYellow3 =  msg2[2].strip("yellow: ")
            initSelfMsgRed3 = float(rawMsgRed3)
            initSelfMsgGreen3 = float(rawMsgGreen3)
            initSelfMsgYellow3 = float(rawMsgYellow3)
            print(initSelfMsgRed3 , " " , initSelfMsgGreen3 , " " , initSelfMsgYellow3)
            print("\n")
        msgRed = rawMsgRed - initLightMsgRed
        msgGreen = rawMsgGreen - initLightMsgGreen
        msgYellow = rawMsgYellow - initLightMsgYellow
        if msgRed < initLightMsgRed - tollRed:
                                      print("Red on ground")
        if msgGreen < initLightMsgGreen - tollGreen:
                                      print("Green on ground")
        if msgYellow < initLightMsgYellow - tollYellow:
                                      print("Yellow on ground")
        print(i,msgRed, msgGreen, msgYellow)
        sleep(.5)
    quit()
