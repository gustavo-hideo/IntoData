"""
GUSTAVO HIDEO HIGA CORREA
CS 450
06 PROVE: NEURAL NETWORKS PART 1
NN
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split    # split in train and test
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
import matplotlib.pyplot as plt


#pd.set_option('expand_frame_repr', False)     # show all variables when printing a dataset


# IMAGE RECOGNITION (HANDWRITTEN NUMBERS)
# LOADIND MNIST DATASET

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


"""
# EXPLORATION
print(y_train[5014])
plt.imshow(x_train[3105], cmap='Greys')
x_train.shape  # 60,000 images, 28x28 pixels
"""

# RESHAPING TO 4-DIMS TO USE WITH KERAS
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# NORMALIZING DATASET
x_train = x_train.astype('float32')    # making sure these are floats, so keep decimals when dividing to normalize
x_test = x_test.astype('float32')

x_train /= 255   # dividing by 255 (max) to get all between 0 and 1, normalized
x_test /= 255      


# CREATING NEURAL NETWORKING MODEL

model = Sequential()
model.add(Conv2D(28, kernel_size=(3,3), input_shape=(28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())   # Flattening the 2D arrays for fully connected layers
model.add(Dense(128, activation=tf.nn.relu))
model.add(Dropout(0.2))
model.add(Dense(10, activation=tf.nn.softmax))   # the last Dense layer must have 10 neurons, because we have 10 number classes to predict (0-9)

# COMPILATION
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
              )

# FITTING
model.fit(x_train, y_train, epochs=8)                

# SCORE
#model.evaluate(x_test, y_test)



# FLAGGING THAT ALGORITHM IS ALREADY LOADED
ran = 1





# VISUALIZATIONS OF ACCURACY
















