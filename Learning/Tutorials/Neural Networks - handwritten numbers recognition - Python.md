# **NEURAL NETWORKS**
#### _Gustavo Hideo Higa Correa_
## Image recognition | Handwritten numbers


<br>

## **Importing libraries**
```python
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
import matplotlib.pyplot as plt
```
<br>

## **Loading dataset**
```python
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
```
<br>

## **Dataset**
The [MNIST database](https://towardsdatascience.com/image-classification-in-10-minutes-with-mnist-dataset-54c35b77a38d) contains 60,000 training images and 10,000 testing images taken from American Census Bureau employees and American high school students [4].
Therefore, in the second line, I have separated these two groups as train and test and also separated the labels and the images. x_train and x_test parts contain greyscale RGB codes (from 0 to 255) while y_train and y_test parts contains labels from 0 to 9 which represents which number they actually are.

<br>

## **Exploration**
This chunk of code shows an example of image and its target:
```python
print(y_train[7777])  # could be any number bellow 60,000
plt.imshow(x_train[5014], cmap='Greys')
x_train.shape
```

<br>

## **Data wrangling**

### Reshaping the data to 4 dimensions to use with keras
```python
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
```


### Normalizing dataset to use in the neural network
First we make sure the data are float, to get decimals when dividing, and divide by `255`, the `max` a RGB can be (so we get numbers betwwen 0 and 1):
```python
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255
```

<br>

## **Neural Network model**
* **Sequence()** model is a linear stack of layers, where we build the neural network
* **Dense** regular dense `NN` layer
  * Parameters:
    * **units** is the number of neurons in the first hidden layer
    * **activation** is the element-wise activation function, that will calculate a "weighted sum" of its inputs, adds a bias and then decides whether it should be "fired" or not. [Reference](https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0)
* **Dropout()** prevent overfitting, randomly dropping units (along with their connections) from the neural network during training. This prevents units from co-adapting too much
  * [Reference](http://www.jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf)
* **Flatten** turns the data in 1 dimension
* **MaxPooling2D** the pooling layer is used to reduce the spatial dimensions, but not depth, on a convolution on neural network model. With less spatial information you gain computation performance and have less parameters, so less chance to over-fit.

```python
model = Sequential()
model.add(Conv2D(28, kernel_size=(3,3), input_shape=(28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())  
model.add(Dense(128, activation=tf.nn.relu))
model.add(Dropout(0.2))
model.add(Dense(10, activation=tf.nn.softmax))
```

<br>

## **Compilation**
Compilation defines the learning process. It has three arguments:
* **optmizer**
* **loss function**
* **list of metrics**

<br>

## Complete guide for **Keras Sequential** model
[Reference](https://keras.io/getting-started/sequential-model-guide/)