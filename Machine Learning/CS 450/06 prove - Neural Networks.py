"""
GUSTAVO HIDEO HIGA CORREA
CS 450
06 PROVE: NEURAL NETWORKS PART 1
EXPERIMENTATION
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split    # split in train and test
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
import matplotlib.pyplot as plt



# IMAGE RECOGNITION (HANDWRITTEN NUMBERS)
# LOADIND MNIST DATASET
"""
The MNIST database contains 60,000 training images and 10,000 testing images 
taken from American Census Bureau employees and American high school students [4].
Therefore, in the second line, I have separated these two groups as train and 
test and also separated the labels and the images. x_train and x_test parts contain
greyscale RGB codes (from 0 to 255) while y_train and y_test parts contains labels
from 0 to 9 which represents which number they actually are.

Dataset: https://towardsdatascience.com/image-classification-in-10-minutes-with-mnist-dataset-54c35b77a38d
Guide: https://keras.io/getting-started/sequential-model-guide/
"""
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()



# EXPLORATION
print(y_train[5014])
plt.imshow(x_train[5014], cmap='Greys')
x_train.shape  # 60,000 images, 28x28 pixels


# RESHAPING TO 4-DIMS TO USE WITH KERAS
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# NORMALIZING DATASET
x_train = x_train.astype('float32')    # making sure these are floats, so keep decimals when dividing to normalize
x_test = x_test.astype('float32')

x_train /= 255   # dividing by 255 (max) to get all between 0 and 1, normalized
x_test /= 255      


# CREATING NEURAL NETWORKING MODEL
"""
The Sequential() model is a linear stack of layers.
The first layer needs to know the input_shape, in our case (28, 28, 1) pixels.

Dense: Regular NN layer.


Dropout: Prevent overfitting, randomly dropping units (along with their connections)
from the neural network during training. This prevents units from co-adapting too much.
Reference: http://www.jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf




"""
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
model.fit(x_train, y_train, epochs=10)                

# SCORE
model.evaluate(x_test, y_test)















