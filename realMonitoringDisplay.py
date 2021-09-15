import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial
from sensorInfo import reqRawSens


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
ax = fig.add_subplot(1, 1, 1)
xs = [] #store trials here (n)
yRed = [] #store relative frequency here
yGreen = []
yYellow = []
yMaxList = []
yMinList = []
# This function is called periodically from FuncAnimation
def animate(o, xs, yRed):

#Aquire and parse data from serial port

	# Add x and y to lists
    xs.append(o)
    yRed.append(reqRawSens('red')[0])
    yGreen.append(reqRawSens('green')[0])
    yYellow.append(reqRawSens('yellow')[0])

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
    if max(yMaxList) - min(yMinList) < 10 : #the minimum difference in maxY and minY is 10, if it is not met, the min and max are creating by finding the middle of the min and max
        maxY = (max(yMaxList)+min(yMinList))/2+5
        minY = (max(yMaxList)+min(yMinList))/2-5
    else:
        maxY = max(yMaxList) + 5 #makes sure that the min and max can clearly be seen by adding some space
        minY = min(yMinList) -5 
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, yRed, label="Red")
    ax.plot(xs, yGreen, label="Green")
    ax.plot(xs, yYellow, label="Yellow")
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('This is how I roll...')
    plt.ylabel('Relative frequency')
    plt.legend()
    plt.axis([minX, minX+Xrange, minY, maxY]) #Use for arbitrary number of trials
    #plt.axis([1, 100, 0, 1.1]) #Use for 100 trial demo
    if o >= Xrange: #removes the 25th number of the list
        del xs[-Xrange]
        del yRed[-Xrange]
        del yGreen[-Xrange]
        del yYellow[-Xrange]
# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, yRed), interval=50)
plt.show()

