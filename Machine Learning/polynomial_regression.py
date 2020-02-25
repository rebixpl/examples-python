#! /usr/bin/python3

#! polynomial_regression

#* if your data points clearly will not fit a linear regression (a straight line through all data points), it might be ideal for polynomial regression.

######################################? Polynomial Regression

import matplotlib.pyplot as plt
import numpy

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22] #  hours of the day
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]  # the speed

# this method  lets us make a polynomial model
mymodel = numpy.poly1d(numpy.polyfit(x,y,3))

# then we specify how the line will display, we start at position 1, and end at position 22, the line complexity is 100 ( if we set it to for example 10 the line would be less precise)
myline = numpy.linspace(1,22,100)

plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()



######################################? R-Squared
#* The relationship between x and y is measured with a value called the r-squared.
#* The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

import numpy 
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22] #  hours of the day
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]  # the speed

mymodel1 = numpy.poly1d(numpy.polyfit(x,y,3))

print(r2_score(y, mymodel1(x))) # OUTPUT: 0.9432150416451026  shows that there is a very good relationship, and we can use polynomial regression in future predictions



######################################? Predict Future Values

# Let us try to predict the speed of a car that passes the tollbooth at around 17 P.M
import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel2 = numpy.poly1d(numpy.polyfit(x,y,3))

speed = mymodel2(17)
print(speed) # OUTPUT: 88.87  # this is the predicted speed we can read it from diagram



######################################?  Bad Fit?
# In this case polynomial regression would not be the best method to predict values

import numpy
import matplotlib.pyplot as plt

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel3 = numpy.poly1d(numpy.polyfit(x,y,3))

myline = numpy.linspace(2,95,100)

plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()
print(r2_score(y, mymodel3(x))) # OUTPUT: around 1 % relationship *poor as fuck*
