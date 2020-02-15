#! /usr/bin/python3

#! data_distribution_creating_big_data_sets_histogram_matplotlib


#############################? Creating an array containing 250 random floats between 0 and 5:
import numpy
# SYNTAX -> numpy.random.uniform(min, max, size)
x = numpy.random.uniform(0.0, 5.0, 250);



###########################? Histogram
# To visualize the data set we can draw a histogram with the data we collected.
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5) # creates histogram from 'x' array with 5 bars
plt.show() # draws histogram

#? Histogram Explained
# We use the array from the example above to draw a histogram with 5 bars.
# The first bar represents how many values in the array are between 0 and 1.
# The second bar represents how many values are between 1 and 2.
# Etc.




############################? Big Data Distributions
import numpy
import matplotlib.pyplot as plp

x = numpy.random.uniform(0.0, 5.5, 100000)

plp.hist(x, 100)
plp.show()
