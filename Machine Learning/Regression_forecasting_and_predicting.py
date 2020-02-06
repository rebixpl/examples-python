#! /usr/bin/python3

#! Notice that this code is not completed becouse i realised that ongoing 
#! tutorial is too hard for me at the moment and completeing it don't have any sense

# installation of a module for example:
# pip3 install pandas

import pandas as pd
import quandl , math, datetime
import numpy as np
from sklearn import preprocessing, svm, model_selection #  model_selection is used to create testing and training samples
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

# which decent looking thing you want
style.use('ggplot')

# importing data from QUANDL
quandl.ApiConfig.api_key = 'zKBZHWxdBgCq2jmz56Gh'
df = quandl.get('WIKI/GOOGL')

# creating a list of the columns that we wanna have from WIKI/GOOGL
df = df[['Adj. Open', 'Adj. High', 'Adj. Low','Adj. Close','Adj. Volume',]]

# the high minus the low percent / percent volatility(zmiennosc)
df['HL_PCT'] = (df['Adj. High'] - #! /usr/bin/python3

# installation of a module for example:
# pip3 install pandas

import pandas as pd
import quandl , math, datetime
import numpy as np
from sklearn import preprocessing, svm, model_selection #  model_selection is used to create testing and training samples
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

# which decent looking thing you want
style.use('ggplot')

# importing data from QUANDL
quandl.ApiConfig.api_key = 'zKBZHWxdBgCq2jmz56Gh'
df = quandl.get('WIKI/GOOGL')

# creating a list of the columns that we wanna have from WIKI/GOOGL
df = df[['Adj. Open', 'Adj. High', 'Adj. Low','Adj. Close','Adj. Volume',]]

# the high minus the low percent / percent volatility(zmiennosc)
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

# the daily percent change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0



df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]



# it's future forecast column definition
forecast_col = 'Adj. Close'

# it changes nan (not defined) data to -99999 (you can't have no data column in machine learning)
df.fillna(-99999, inplace=True)



# this is a regression algorithm 
# Regresja – metoda statystyczna pozwalająca na opisanie współzmienności kilku zmiennych przez dopasowanie do nich funkcji. 
# Umożliwia przewidywanie nieznanych wartości jednych wielkości na podstawie znanych wartości innych.
forecast_out = int(math.ceil(0.01*len(df))) # math.ceil() rounds up value to the nearest whole for example 3.3 -> 4
print(forecast_out)



# label
df['label'] = df[forecast_col].shift(-forecast_out)



# features
X = np.array(df.drop(['label'],1)) # remove rows or columns by specifying label names (it also returns it as an array by np.array() function)


# scale X
x = preprocessing.scale(X)

X_lately = X[-forecast_out:]

X = X[:-forecast_out:]


# labels
df.dropna(inplace=True) # removes missing values
y = np.array(df['label'])
y = np.array(df['label'])



# creating training and testing set
X_train, X_test, y_train, y_test =model_selection.train_test_split(X, y, test_size=0.2) # test_size=0.2 // we are gonna use 20% of the testing data



# defining a classifier
# n_jobs=-1 -> it runs as many jobs as possible by your processor (default of jobs is 1)(training part would be faster)
# n_jobs=10 -> it runs 10 jobs at a time (training part would be faster)
clf = LinearRegression(n_jobs=10) # you can easily switch the algorithms by changing this line for example for: clf = svm.SVR()

# fit (train) classifier
clf.fit(X_train, y_train)

# test (score) a classifier
accuracy = clf.score(X_test, y_test)

# predicting data
forecast_set = clf.predict(X_lately)

print(forecast_set, accuracy, forecast_out)

# this specifies that entire column is just full of nan a number data
df['Forecast'] = np.nan

# finds out what the last date was
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_date + one_day



# populates the dataframe with the new Dates and forecast values
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) -1)] + [i]


df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()df['Adj. Close']) / df['Adj. Close'] * 100.0

# the daily percent change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0



df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]



# it's future forecast column definition
forecast_col = 'Adj. Close'

# it changes nan (not defined) data to -99999 (you can't have no data column in machine learning)
df.fillna(-99999, inplace=True)



# this is a regression algorithm 
# Regresja – metoda statystyczna pozwalająca na opisanie współzmienności kilku zmiennych przez dopasowanie do nich funkcji. 
# Umożliwia przewidywanie nieznanych wartości jednych wielkości na podstawie znanych wartości innych.
forecast_out = int(math.ceil(0.01*len(df))) # math.ceil() rounds up value to the nearest whole for example 3.3 -> 4
print(forecast_out)



# label
df['label'] = df[forecast_col].shift(-forecast_out)



# features
X = np.array(df.drop(['label'],1)) # remove rows or columns by specifying label names (it also returns it as an array by np.array() function)


# scale X
x = preprocessing.scale(X)

X_lately = X[-forecast_out:]

X = X[:-forecast_out:]


# labels
df.dropna(inplace=True) # removes missing values
y = np.array(df['label'])
y = np.array(df['label'])



# creating training and testing set
X_train, X_test, y_train, y_test =model_selection.train_test_split(X, y, test_size=0.2) # test_size=0.2 // we are gonna use 20% of the testing data



# defining a classifier
# n_jobs=-1 -> it runs as many jobs as possible by your processor (default of jobs is 1)(training part would be faster)
# n_jobs=10 -> it runs 10 jobs at a time (training part would be faster)
clf = LinearRegression(n_jobs=10) # you can easily switch the algorithms by changing this line for example for: clf = svm.SVR()

# fit (train) classifier
clf.fit(X_train, y_train)

# test (score) a classifier
accuracy = clf.score(X_test, y_test)

# predicting data
forecast_set = clf.predict(X_lately)

print(forecast_set, accuracy, forecast_out)

# this specifies that entire column is just full of nan a number data
df['Forecast'] = np.nan

# finds out what the last date was
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_date + one_day



# populates the dataframe with the new Dates and forecast values
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) -1)] + [i]


df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
