"""
GUSTAVO HIDEO HIGA CORREA
STOCKS PREDICTOR
"""


import pandas as pd
import numpy as np
import quandl
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from fastai.tabular import add_datepart
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

pd.set_option('expand_frame_repr', False)     # show all variables when printing a dataset

# Quandl API: SSEPkWgCjFSkGNqtuy4z
#quandl.ApiConfig.api_key = "API_KEY"

data = quandl.get("NSE/TATAGLOBAL", start_date="2015-01-01", end_date="2018-12-31")


data.Close.plot()
plt.show()


plt.figure(figsize=(16,8))
plt.plot(data['Close'], label='Closing price history')


# Creating new dataframe with only Date and Close
data = data.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0,len(data)), columns=['Date','Close'])

for i in range(0, len(data)):
    new_data['Date'][i] = data.index[i]
    new_data['Close'][i] = data['Close'][i]

# Setting index
new_data.index = new_data.Date
new_data.drop('Date', axis=1, inplace=True)

"""
# Adding date features using 'fastai'
add_datepart(new_data, 'Date')
new_data.drop('Elapsed', axis=1, inplace=True)  # elapsed will be the time stamp

# Flagging if date is Monday/Friday
new_data['mon_fri'] = 0
for i in range(0, len(new_data)):
    if (new_data['Dayofweek'][i] == 0 or new_data['Dayofweek'][i] == 4):
        new_data['mon_fri'][i] = 1
    else:
        new_data['mon_fri'][i] = 0
"""

# 80% train, 20% test
dataset = new_data.values

train_end = int(dataset.shape[0]*.8)

train = dataset[0:train_end]
test = dataset[train_end:data.shape[0]+1]

# Normalizing
scaler = MinMaxScaler(feature_range=(0,1))
scaled_train = scaler.fit_transform(train)
scaled_test = scaler.fit_transform(test)




# x_train, y_train, x_test, y_test
# the target (y) is always the next day's 'Close'

x_train, y_train = [], []
for i in range(1,train.shape[0]):
    x_train.append(scaled_train[i-1:i,0])
    y_train.append(scaled_train[i,0])

x_train, y_train = np.array(x_train), np.array(y_train)



x_test = []
for i in range(1,test.shape[0]):
    x_test.append(scaled_test[i-1:i,0])

x_test = np.array(x_test)

# reshaping - including one more dimension
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))




# LSTM Network
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2)


# Prediction
closing_price = model.predict(x_test)
closing_price = scaler.inverse_transform(closing_price)





# Results with RMSE
"""
RMSE:
Root Mean Square Error (RMSE) is the standard deviation
of the residuals (prediction errors). Residuals are a measure
of how far from the regression line data points are; RMSE is
a measure of how spread out these residuals are. In other
words, it tells you how concentrated the data is around the
line of best fit.

Square root of the mean of the difference between real Y and
expected Y squared.
"""
test = test[:-1]

rms = np.sqrt(np.mean(np.power((test - closing_price),2)))
rms



# Plotting

train = new_data[0:train_end]
test = new_data[train_end:new_data.shape[0]+1]
test = test[:-1]
#test = test[:-1]
#test = new_data[197:]

test['Predictions'] = closing_price

plt.figure(figsize=(21,10))
plt.plot(train['Close'])
#plt.plot(test['Close'])
plt.plot(test[['Close', 'Predictions']])




