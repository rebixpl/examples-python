#! /usr/bin/python3

#! linear_regression_predicting_future_values_and_bad_fit

#* regression is used when you try to find the relationship between variables
#* In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events



########################################? Linear Regression
#* Linear regression uses the relationship between the data-points to draw a straight line through all them and this line can be used to predict values

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# this method returns some important key values of Linear Regression
slope, intercept, r, p, std_err = stats.linregress(x,y)

# this function uses the slope and intercept values to return a new value.
# This new value represents where on the y-axis the corresponding x value will be placed
def myFunc(x):
    return slope * x + intercept

# Run each value of the x array through the function. This will result in a new array with new values for the y-axis:
myModel = list(map(myFunc, x))

plt.scatter(x,y) # draws the scatter plot
plt.plot(x, myModel) # draws the linear regression line
plt.show()



########################################? R-Squared
# the relationship between the values of the x-axis and the values of the y-axis is measured with a value called the r-squared
# The r-squared value changes from 0 to 1 ( 0 means no relationship and 1 means 100% related)

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept,r, p, std_err = stats.linregress(x,y)

# r-squared value
print(r) # OUTPUT: -0.7585915243761551
# The result -0.76 shows that there are a relationship, not perfect, but it indicates that we could use linear regression in future predictions.




########################################? Predict Future Values

# predicting the speed of a 10 years old car
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x,y)

def myFunc(x):
    return slope * x + intercept

speed = myFunc(10)

print(speed) # OUTPUT: 85.59308314937454



########################################? Bad Fit
# in this example linear regression would not be the best method to predict future values

import matplotlib.pyplot as plt
from scipy import stats

# These values for the x- and y-axis should result in a very bad fit for linear regression
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x,y)

print(r) # r-value OUTPUT: 0.013 indicates a very bad relationship, and tells us that this data set is not suitable for linear regression

def myFunc(x):
    return slope * x + intercept

myModel = list(map(myFunc, x))

plt.scatter(x,y)
plt.plot(x, myModel)
plt.show()
