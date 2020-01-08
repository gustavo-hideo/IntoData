# -*- coding: utf-8 -*-
"""
01 Prove : Assignment - Experiment Shell & Hardcoded Classifier

by Gustavo Hideo
"""

# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

# Loading iris dataset as txt file
iris = pd.read_csv('C:/Users/gustavo_hideo/Documents/cs450/iris.data', header=None)
x = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values


# Enconding dependent variable y
le = LabelEncoder()
y = le.fit_transform(y)




# Splitting into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)




# GaussianNB algorithm
classifier = GaussianNB()
classifier.fit(x_train, y_train)

# predictions
predictions = classifier.predict(x_test)
# Checking the prediction
print(predictions==y_test)



#############


# My own algorithm: HardCodedClassifier










