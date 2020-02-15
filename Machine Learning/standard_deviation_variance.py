#! /usr/bin/python3

#! standard_deviation_variance

import numpy


#####################################? Standard Deviation
#* Standard deviation is a number that describes how spread out the values are.

# Meaning that most of the values are within the range of 39.82102818504673 from the mean value, which is 76.
speed = [32,111,138,18,59,77,97]
x = numpy.std(speed) # calculating a deviation
print(x) # OUTPUT: 39.82102818504673
print(numpy.mean(speed)) # OUTPUT: 76.0

speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x) # OUTPUT: 39.82102818504673



#####################################? Variance
#* Variance is another number that indicates how spread out the values are.
#* In fact, if you take the square root of the variance, you get the standard deviation!

#* TO CALCULATE THE Variance YOU NEED:
#* 1. Find the mean
# (32+111+138+28+59+77+97) / 7 = 77.4

#* 2.For each value: find the difference from the mean
# 32 - 77.4 = -45.4
# 111 - 77.4 =  33.6
# 138 - 77.4 =  60.6
# 28 - 77.4 = -49.4
# 59 - 77.4 = -18.4
# 77 - 77.4 = - 0.4
# 97 - 77.4 =  19.6

#* 3. For each difference: find the square value:
# (-45.4)2 = 2061.16
# (33.6)2 = 1128.96
# (60.6)2 = 3672.36
# (-49.4)2 = 2440.36
# (-18.4)2 =  338.56
# (- 0.4)2 =    0.16
# (19.6)2 =  384.16

#* 4. The variance is the average number of these squared differences:
# (2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2

#* or you can simply use var() method:
import numpy
speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.var(speed)
print(x) # OUTPUT: 1432.2448979591834



#####################################? Standard Deviation
#* the another interesting thing of Standard Deviation is that it is the square root of the variance
# √1432.25 = 37.85

import numpy
speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.std(speed)
print(x) # OUTPUT: 37.84501153334721



#####################################? Symbols
#* Standard Deviation -> Sigma -> σ
#* Variance -> Sigma square -> σ2
