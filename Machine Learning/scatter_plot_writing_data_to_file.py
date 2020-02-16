#! /usr/bin/python3

#! scatter_plot_writing_data_to_file

#######################################? scatter plot

#* scatter plot is a diagram where each value in the data set is represented by a dot
#* we can draw scatter plot using scatter(x, y) method

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y) # generates scatter diagram (it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis)
plt.show() # draws scatter plot diagram onto the screen



#######################################? Random Data Distributions
import numpy
import matplotlib.pyplot as plt

# generating random data
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0,2.0,1000)

# converting data from numpy array into string
xStr = numpy.array2string(x, precision=10, separator=',', suppress_small=True)
yStr = numpy.array2string(y, precision=10, separator=',', suppress_small=True)

# writing data to file
data_file = open("demofiles/demofile2.txt", "w")
data_file.write(xStr)
data_file.write(yStr)
data_file.close()

# creating scatter diagram
plt.scatter(x,y)
plt.show()
