# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:14:59 2020

@author: gusta
"""


"""
https://towardsdatascience.com/writing-your-first-neural-net-in-less-than-30-lines-of-code-with-keras-18e160a35502
"""

import pandas as pd
import numpy as np
from matplotlib import image, pyplot
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D
from keras import layers
from os import listdir
from os.path import isfile, join
from keras.datasets import mnist




from keras.utils import to_categorical

# Importing MNIST data
(x_train, y_train), (x_test, y_test) = mnist.load_data()


model = Sequential()
model.add(layers.Dense(784, activation='relu', input_shape=(28*28,)))
model.add(layers.Dense(56, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

x_train = x_train.reshape((60000, 28*28))
#x_train = x_train.astype('float32') / 255
x_test = x_test.reshape((10000, 28*28))
#x_test = x_test.astype('float32') / 255

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model.fit(x_train, y_train, epochs=10, batch_size=96)






