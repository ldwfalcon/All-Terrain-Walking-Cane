import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial
from sensorInfo import reqRawSens
from matplotlib.widgets import Button
import math


#initialize serial port
ser = serial.Serial()
ser.port = '/dev/ttyUSB0' #Arduino serial port
ser.baudrate = 57600
ser.open()
    #Aquire and parse data from serial port v
line=ser.readline()      #ascii
line_as_lists = line.split(b',')
o = int(line_as_lists[0])
if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #print serial parameters
	
def calibrate(c):
    output = []
    output.append(reqRawSens(c)[0])
    return output[0] #returns all the information requested as a list

Xrange = 18 # length of X graph data
# Create figure for plotting

fig = plt.figure(figsize= (9,7))
fig.patch.set_facecolor('darkgrey')

ax = fig.add_subplot()
ax.set_facecolor('grey')
xs = [] #store trials here (n)
yRed = [] #store relative frequency here
yGreen = []
yYellow = []
yRed2 = [] #store relative frequency here
yGreen2 = []
yYellow2 = []
yRedAv = [] #to be used to store average 
yGreenAv = []
yYellowAv = []
yMaxList = []
yMinList = []
oStore1 = 0
redCal = calibrate('red')
greenCal = calibrate('green')
yellowCal = calibrate('yellow')

def animate(o, xs, yRed):

#Aquire and parse data from serial port
    
	# Add x and y to lists
    xs.append(o)
    readings = reqRawSens('red, green, yellow') #requesting all at the same time in order to get faster reaing as it only has to go through the code once instead of fully, multiple times.
    
    yRed.append(readings[0]-redCal)
    yGreen.append(readings[1]-greenCal)
    yYellow.append(readings[2]-yellowCal)


    # Limit x and y lists to 20 items
    #xs = xs[-20:]
    #yRed = yRed[-20:]

    if o >= Xrange:
         minX = xs[-Xrange] # min X axis 
    else:
        minX = xs[-o]
    yMaxList.clear()
    yMinList.clear()
    yMaxList.extend([max(yRed), max(yGreen), max(yYellow)])
    yMinList.extend([min(yRed), min(yGreen), min(yYellow)])
    yMin = min(yMinList)
    yMax = max(yMaxList)
    if max(yMaxList) - min(yMinList) < 10 : #the minimum difference in maxY and minY is 10, if it is not met, the min and max are creating by finding the middle of the min and max
        maxY = (yMax+yMin)/2+5
        minY = (yMax+yMin)/2-5
    else:
        maxY = yMax + (yMax-yMin)/20 #makes sure that the min and max can clearly be seen by adding some space
        minY = yMin - (yMax-yMin)/20 
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, yRed, label="Red", color = 'red')
    ax.plot(xs, yGreen, label="Green", color = 'lightgreen')
    ax.plot(xs, yYellow, label="Yellow", color = 'orange')
    if o >= 3:
        if o >= 4:
            oStore0 = o #oStore, stores the previous value of o
            print(oStore0)
            if oStore0 - o >= 3:
                oStore1 = oStore1+1
                print(oStore1)
                if oStore1 == 3:
                    yRedAv.append(yRed[0])
                    yGreenAv.append(yGreen[0])
                    yYellowAv.append(yYellow[0])
                    ax.plot(xs, yRedAv, label="Red", color = 'red', dashes = [10,5,10,5])
                    ax.plot(xs, yGreenAv, label="Green", color = 'lightgreen', dashes = [10,5,10,5])
                    ax.plot(xs, yYellowAv, label="Yellow", color = 'orange', dashes = [10,5,10,5])
                    print('etw')
    else:
        yRedAv.append(0)
        yGreenAv.append(0)
        yYellowAv.append(0)    

    # Format plot
    plt.xticks(rotation=45, ha='right')


    plt.axis([minX, minX+Xrange, minY, maxY]) #Use for arbitrary number of trials
    #plt.title('This is how I roll...')
    #plt.ylabel('Relative frequency')
    ax.legend()
    print(min(yGreen), max(yGreen))
    
    if o >= Xrange: #removes the 25th number of the list
        del xs[-Xrange]
        del yRed[-Xrange]
        del yGreen[-Xrange]
        del yYellow[-Xrange]
        del yRedAv[-Xrange]
        del yGreenAv[-Xrange]
        del yYellowAv[-Xrange] 
# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, yRed), interval=1)
plt.show()

