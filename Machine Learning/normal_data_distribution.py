#! /usr/bin/python3

#! normal_data_distribution

#? The values are concentrated around a given value.
#?  A normal distribution graph is also known as the bell curve because of it's characteristic shape of a bell.

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000) # you use 'numpy.random.normal(mean_val, standard_deviation, number_of_values)' to generate normal data distribution

plt.hist(x, 100) # generates histogram with data 'x' and 100 bars
plt.show() # draws histogram on screen

#* We specify that the mean value is 5.0, and the standard deviation is 1.0.
#* Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
#* And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.
