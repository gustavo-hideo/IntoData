# -*- coding: utf-8 -*-
"""
02 Prove Above & Beyond: Assignment - kNN Classifier
Created on Fri Jan 17 16:48:27 2020

@author: gusta
"""



# Importing libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import LabelEncoder
from statistics import mode
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


# Load iris dataset
data = pd.read_csv('C:/wandata/IntoData/BYUI/CS450 - Machine Learning and Data Mining/wi2020/iris.data')
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

# Encoding y
le = LabelEncoder()
y = le.fit_transform(y)


# Split into train set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)


# kNN algorithm
class knn():
    def __init__(self, k):
        self.k = k
        
    def fit(self, x_train, y_train):
        pass
    
    def predict(self, x_test):
        choices = []
        for i in range(x_test.shape[0]):
            distances = []      
            for j in range(x_train.shape[0]):
                dist = np.sum(x_test[i] - x_train[j])**2
                distances.append(dist)  #all the distances
            short_dist_index = np.argsort(distances)[0:self.k]  #index of k shortest distances
            choices.append(mode(y_train[short_dist_index])) #append the prediction in the choices list
        return choices
            


nn=knn(3)
nn.fit(x_train, y_train)
pred = np.array(nn.predict(x_test))
pred

# Accuracy
accuracy_score(y_test, pred)



# Coparing my results to an existing classifier
classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)
accuracy_score(y_test, predictions)










##############################

##  Car data set with categorical variables


# Load car dataset
cols = ['buying','maint','doors','persons','lug_boot','safety','accept']
car = pd.read_csv('C:/wandata/IntoData/BYUI/CS450 - Machine Learning and Data Mining/wi2020/car.data',
                  header=None,
                  names=cols)

#Enconding categorical variables
cleanup = {'buying': {'low':0,
                      'med':1,
                      'high':2,
                      'vhigh':3},
           'maint': {'low':0,
                      'med':1,
                      'high':2,
                      'vhigh':3},
            'doors': {'2':2,
                      '3':3,
                      '4':4,
                      '5more':5},
            'persons': {'2':2,
                        '4':4,
                        'more':5},
            'lug_boot': {'small':0,
                         'med':1,
                         'big':2},
            'safety': {'low':0,
                       'med':1,
                       'high':2}}
            
car.replace(cleanup, inplace=True)            

            
x = car.iloc[:,:-1].values
y = car.iloc[:,-1].values




# Split into train set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)



#
nn=knn(5)
nn.fit(x_train, y_train)
pred = np.array(nn.predict(x_test))
pred

# Accuracy
accuracy_score(y_test, pred)



# Coparing my results to an existing classifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)
accuracy_score(y_test, predictions)











