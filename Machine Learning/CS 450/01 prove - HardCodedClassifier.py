# 01 PROVE - EXPERIMENTAL SHELL & HARDCODED CLASSIFIER

# LIBRARIES
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import urllib


# LOAD DATA
iris = datasets.load_iris()


# CREATING TRAINING AND TESTING SETS
x = pd.DataFrame(iris.data)
y = pd.Series(iris.target)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)


# NAIVE BAYES | GAUSSIANNB ALGORITHM
classifier = GaussianNB()
classifier.fit(x_train, y_train)

targets_predicted = classifier.predict(x_test)


# EVALUATE ACCURACY
acc = accuracy_score(y_test, targets_predicted)
print("\n GaussianNB accuracy: \n {}" .format(acc))






# MY ALGORITHM
class HardCodedClassifier:

	def __init__(self):
		pass

	def fit(self, data_train, targets_train):
		a = print("\n .fit() is doing nothing here!")
		return a

	def predict(self, data_test):
		prediction = [0 for x, row in data_test.iterrows()]
		return prediction



# LOAD DATA
iris = pd.read_csv("C:\\Users\\Gustavo\\iCloudDrive\\Data Science\\Machine Learning\\CS 450 - Machine Learning and Data Mining\\W01\\iris.csv", header = None)


# SPLIT INTO DATA AND TARGETS
x = pd.DataFrame(iris.values[:,0:-1])
y = pd.Categorical(pd.Series(iris.values[:, -1], dtype = "category"))
y_len = len(y.unique())
y = y.rename_categories(range(y_len))
y = pd.Series(y)



# SPLITING INTO TRAINING AND TESTING DATASETS
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

# USING MY ALGORITHM
classifier = HardCodedClassifier()

classifier.fit(x_train, y_train)

targets_predicted = classifier.predict(x_test)



# Accuracy
acc = accuracy_score(y_test, targets_predicted)
print("\n Accuracy of HardCodedClassifier's prediction: \n {}" .format(acc))





