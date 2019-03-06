"""
GUSTAVO HIDEO HIGA CORREA
CS 450
06 PROVE: NEURAL NETWORKS PART 3
NN - Stocks
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from matplotlib import pyplot as plt
import datadotworld as dw


pd.set_option('expand_frame_repr', False)     # show all variables when printing a dataset


# LOADING PBR STOCKS DATASET
dw_ds = dw.load_dataset('https://data.world/gustavo-hideo/general')
stocks_raw = dw_ds.dataframes['pbr_stocks']
#stocks.info()

stocks = stocks_raw.drop(columns = ['adj_close'])  # removing adj_close column


# CREATING NEW VARIABLES
stocks['daily_var'] = round(stocks['close'] - stocks['open'], 2)  # daily variation (close - open)
stocks['daily_var_rol_avg'] = stocks.daily_var.rolling(5).mean() # rolling average of 5 days for daily variation
stocks['close_rol_avg'] = stocks.close.rolling(5).mean() # rolling average of 5 days for close

stocks['daily_var_prev1d'] = stocks['daily_var'].shift(1)
stocks['daily_var_rol_avg_prev1d'] = stocks['daily_var_rol_avg'].shift(1)
stocks['close_rol_avg_prev1d'] = stocks['close_rol_avg'].shift(1)
stocks['low_prev1d'] = stocks['low'].shift(1)
stocks['high_prev1d'] = stocks['high'].shift(1)

stocks['close_prev1d'] = stocks['close'].shift(1)
stocks['close_prev2d'] = stocks['close'].shift(2)
stocks['close_prev6d'] = stocks['close'].shift(6)
stocks['close_var2d'] = round((stocks['close_prev1d'] - stocks['close_prev2d']) / (stocks['close_prev1d'] + stocks['close_prev2d']), 4)
stocks['close_var6d'] = round((stocks['close_prev1d'] - stocks['close_prev6d']) / (stocks['close_prev1d'] + stocks['close_prev6d']), 4)


stocks['volume_prev1d'] = stocks['volume'].shift(1)
stocks['volume_prev2d'] = stocks['volume'].shift(2)
stocks['volume_prev6d'] = stocks['volume'].shift(6)
stocks['volume_var2d'] = round((stocks['volume_prev1d'] - stocks['volume_prev2d']) / (stocks['volume_prev1d'] + stocks['volume_prev2d']), 4)
stocks['volume_var6d'] = round((stocks['volume_prev1d'] - stocks['volume_prev6d']) / (stocks['volume_prev1d'] + stocks['volume_prev6d']), 4)

stocks = stocks[['daily_var_prev1d'
                ,'daily_var_rol_avg_prev1d'
                ,'close_rol_avg_prev1d'
                ,'low_prev1d'
                ,'high_prev1d'
                ,'close_prev1d'
                ,'close_prev2d'
                ,'close_prev6d'
                ,'close_var2d'
                ,'close_var6d'
                ,'volume_prev1d'
                ,'volume_prev2d'
                ,'volume_prev6d'
                ,'volume_var2d'
                ,'volume_var6d'
                ,'close']]



# SPLITTING INTO TRAIN AND TEST
# &
# SCALING INPUTS (FEATURES) AND OUTPUT (TARGET)
nrow = stocks.shape[0]
ncol = stocks.shape[1]
train_start = 0
train_end = int(np.floor(0.8 * nrow))
test_start = train_end
test_end = nrow

# 80% train | 20% test
train = np.array(stocks)[train_start:train_end]
test = np.array(stocks)[test_start:test_end]

train.reshape(1,1006,16)

# Scalling
scaler = MinMaxScaler()
train_norm = scaler.fit_transform(train)
test_norm = scaler.fit_transform(test)

# Features and Targets
train_x = train_norm[:,ncol-1]   # x|data
train_y = train_norm[:,-1]       # y|target
test_x = test_norm[:,ncol-1]   # x|data
test_y = test_norm[:,-1]       # y|target

# Final Train and Test
x_train = train_x[train_start:train_end]
y_train = train_y[train_start:train_end]
x_test = test_x[test_start:test_end]
y_test = test_y[test_start:test_end]




# NN MODEL
# https://www.tensorflow.org/api_docs/python/tf/keras/models/Sequential
# https://www.tensorflow.org/api_docs/python/tf/keras/layers
model = Sequential()
model.add(Dense(32, input_shape=(1006,), activation='relu'))
#model.add(Flatten())
#model.add(Dense(16))
#model.add(Dropout(0.2))
#model.add(Dense(8))

# Compile model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse','mae'])

# Fitting model
model.fit(x_train, y_train, epochs=3, verbose=1)



from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from tensorflow.python.keras.wrappers.scikit_learn import KerasRegressor



















