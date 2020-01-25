# -*- coding: utf-8 -*-
"""
03 Prove Using kNN with (slightly) More Interesting Data
Created on Fri Jan 17 16:48:27 2020

@author: gusta
"""



# Importing libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from collections import Counter




# mode algorithm
#a = [1,2,3,4,5,5,5]
#x = [1,2,3,4,5,5,5,6,7,6,5,4,3,3,4,5,6,6,6,7,4]
"""
Returns the number with highest frequency from a list
If there is a tie, it gets the candidate with highest frequency from the full data
"""
class mode():
    def __init__(self, candidates, data):
        self.candidates = dict(Counter(candidates))
        self.data = Counter(data)
          
    def m_choices(self):
        max_value = max(list(self.candidates.values()))
        maxs = [value for value, freq in self.candidates.items() if freq == max_value]
        if len(maxs) == 1:
            choice = maxs
        else:
            opts = []
            for i in maxs:
                opts.append(self.data[i])
            opts_index = np.argmax(opts)
            choice = maxs[opts_index]
        return choice[0]

#m = mode(a,x)
#m.m_choices()



# my kNN algorithm
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
            m = mode(y_train[short_dist_index], y_train)
            choice = m.m_choices()
            choices.append(choice) #append the prediction in the choices list
        return choices
            











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




# Normalizing features
minmax = MinMaxScaler().fit(x)
x = minmax.transform(x)



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


            









##############################
        
##  MPG data set with missing values
cols = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','car name']

mpg = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original',
                  sep='\s+',
                  header=None,
                  names=cols).iloc[:,:-1]

#Enconding cylinders (from [3,4,5,6,8] to [1,2,3,4])
le = LabelEncoder()
mpg['cylinders'] = le.fit_transform(mpg['cylinders'])

# OneHotEncoding for the Origin
mpg = pd.get_dummies(mpg, columns=['origin'])

# Missing values
mpg = mpg[mpg['mpg'].notnull()]
mpg = mpg[mpg['horsepower'].notnull()]



#Train and test sets
x = mpg.iloc[:,1:]
y = mpg.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)


#Regression
regr = KNeighborsRegressor(n_neighbors=3)
regr.fit(x_train, y_train)
predictions = regr.predict(x_test)
print('Average error is: %.3f' % np.mean(y_test - predictions))









##################
# Students grades data set
stu = pd.read_csv('C:/wandata/IntoData/BYUI/CS450 - Machine Learning and Data Mining/wi2020/student/student-mat.csv',
                  sep=';')

le = LabelEncoder()
stu['school'] = le.fit_transform(stu['school'])
stu['sex'] = le.fit_transform(stu['sex'])
stu['address'] = le.fit_transform(stu['address'])
stu['famsize'] = le.fit_transform(stu['famsize'])
stu['Pstatus'] = le.fit_transform(stu['Pstatus'])
stu['Mjob'] = le.fit_transform(stu['Mjob'])
stu['Fjob'] = le.fit_transform(stu['Fjob'])
stu['reason'] = le.fit_transform(stu['reason'])
stu['guardian'] = le.fit_transform(stu['guardian'])
stu['schoolsup'] = le.fit_transform(stu['schoolsup'])
stu['famsup'] = le.fit_transform(stu['famsup'])
stu['paid'] = le.fit_transform(stu['paid'])
stu['activities'] = le.fit_transform(stu['activities'])
stu['nursery'] = le.fit_transform(stu['nursery'])
stu['higher'] = le.fit_transform(stu['higher'])
stu['internet'] = le.fit_transform(stu['internet'])
stu['romantic'] = le.fit_transform(stu['romantic'])




#Train and test sets
x = stu.iloc[:,:-1]
y = stu.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)


#Regression
regr = KNeighborsRegressor(n_neighbors=3)
regr.fit(x_train, y_train)
predictions = regr.predict(x_test)
print('Average error is: %.3f' % np.mean(y_test - predictions))














