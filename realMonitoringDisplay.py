import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial
from sensorInfo import reqRawSens
from sensorCalibration import calibrate
from matplotlib.widgets import CheckButtons


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
redCal = calibrate('red')
greenCal = calibrate('green')
yellowCal = calibrate('yellow')
# This function is called periodically from FuncAnimation
def animate(o, xs, yRed):
    circle1 = plt.Circle((2, 2), 2, color='r')

#Aquire and parse data from serial port

	# Add x and y to lists
    xs.append(o)
    yRed.append(reqRawSens('red')[0]-redCal)
    yGreen.append(reqRawSens('green')[0]-greenCal)
    yYellow.append(reqRawSens('yellow')[0]-yellowCal)
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
    ax.add_patch(circle1)
    ax.plot(xs, yRed, label="Red", color = 'red')
    ax.plot(xs, yGreen, label="Green", color = 'lightgreen')
    ax.plot(xs, yYellow, label="Yellow", color = 'orange')
    
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.title('This is how I roll...')
    plt.ylabel('Relative frequency')
    plt.axis([minX, minX+Xrange, minY, maxY]) #Use for arbitrary number of trials
    ax.legend

    width = 1       # the width of the bars: can also be len(x) sequence
    axs.clear()
    if o > 1:
        totalWeight= yRed[2]+yGreen[2]+yYellow[2]+1
        axs.bar('Red', yRed[2]/totalWeight, width, yerr=0, bottom = 0,label='Red', color = 'red') #yerr is the error line length
        axs.bar('Green', yGreen[2]/totalWeight, width, yerr=0, bottom = 0,label='Green', color = 'lightgreen')
        axs.bar('Yellow', yYellow[2]//totalWeight, width, yerr=0, bottom = 0,label='Yellow', color = 'orange')
    axs.set_ylabel('Scores')
    axs.set_title('Scores by group and gender')
    axs.legend()
    if o >= Xrange: #removes the 25th number of the list
        del xs[-Xrange]
        del yRed[-Xrange]
        del yGreen[-Xrange]
        del yYellow[-Xrange]

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, yRed), interval=50)

plt.show()


