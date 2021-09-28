import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial
from sensorInfo import reqRawSens
from matplotlib.widgets import Button
import math
from pynput.keyboard import Key, Listener

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

def sqrt(s): #so that can use sqrt to square root somehting
    return s**0.5

def calibrate(c):
    output = []
    output.append(reqRawSens(c)[0])
    return output[0] #returns all the information requested as a list

Xrange = 25 # length of X graph data
# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
axs = fig.add_subplot(2, 1, 2)
xs = [] #store trials here (n)
yRed = [] #store relative frequency here
yGreen = []
yYellow = []
yMaxList = []
yMinList = []
for i in range(2):
    redCal = calibrate('red')
    greenCal = calibrate('green')
    yellowCal = calibrate('yellow')
# This function is called periodically from FuncAnimation

def animate(o, xs, yRed):
#Aquire and parse data from serial port

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
    plt.subplot(211)
    ax.plot(xs, yRed, label="Red", color = 'red')
    ax.plot(xs, yGreen, label="Green", color = 'lightgreen')
    ax.plot(xs, yYellow, label="Yellow", color = 'orange')
    
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.title('BRUH')
    plt.ylabel('Raw Force Data')
    plt.axis([minX, minX+Xrange, minY, maxY]) #Use for arbitrary number of trials
    ax.legend
    totalWeight = (abs(yRed[-1])+abs(yGreen[-1])+abs(yYellow[-1])+1) # the total measured raw weight, we add 1 in order to make sure it is not equal to zero
    n = [0.025,0.05,0.275,0.325, 0.4, 0.525, 0.7,0.875] #different possible width
    for i in range(8):
        if totalWeight/3 < 10*10**(i/2):
            width = n[i]
            break
        elif i == 7:
            width = 1 #max width

    axs.clear()
    if o > 0:
        axs.bar('Red', abs(yRed[-1])/totalWeight, width, yerr=0, bottom = 0,label='Red', color = 'red') #yerr is the error line length
        axs.bar('Green', abs(yGreen[-1])/totalWeight, width, yerr=0, bottom = 0,label='Green', color = 'lightgreen')
        axs.bar('Yellow', abs(yYellow[-1])//totalWeight, width, yerr=0, bottom = 0,label='Yellow', color = 'orange')
    axs.set_ylabel('% of Total Force')
    axs.legend()
    if o >= Xrange: #removes the 25th number of the list
        del xs[0]
        del yRed[0]
        del yGreen[0]
        del yYellow[0]
 
def show(key):

    pressed_key = str(key).replace("'", "")
    print(" key: ", pressed_key)
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, yRed), interval=1)
    plt.show()
    if key == Key.esc:
            # Stop listener
        return 1


    # Listener
while 1 == 1 :
    # Set up plot to call animate() function periodically
	# Add x and y to lists   
    with Listener(on_press=show) as listener:
        listener.join()

