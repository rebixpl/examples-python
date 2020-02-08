#! /usr/bin/python3

#! Machine Learning - Mean Median Mode
# In Machine Learning (and in mathematics) there are often three values that interests us:
# - Mean - The average value
# - Median - The mid point value
# - Mode - The most common value



#?  Mean - average value
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed) # 'mean()' method is the NumPy method thus we need to import numpy
print(x) # OUTPUT: 89.76923076923077
# its doing this calculation -> (99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77



#? Median - this is the value in the middle, after you have sorted all the values
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x) # OUTPUT: 87.0



#? Mode - it's the value that appears most number of times
from scipy import stats  # importing only stats.mode() method from scipy to do mode
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x) # OUTPUT: ModeResult(mode=array([86]), count=array([3]))

#The mode() method returns a ModeResult object that contains the mode number (86), 
# and count (how many times the mode number appeared (3)).
