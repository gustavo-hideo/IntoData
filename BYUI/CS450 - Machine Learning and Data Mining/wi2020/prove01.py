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
from sklearn.metrics import accuracy_score




class HardCodedClassifier():
    def __init__(self):
        self.pred = []
    
    def fit(self, x, y):
        pass
    
    def predict(self, x):
        for i in x:
            self.pred.append(0)
        return self.pred



class predIris():
    def __init__(self, data, ncol, size, algo):
        self.data = data
        self.ncol = ncol
        self.size = size
        self.algo = algo
    
    def loadData(self):
        iris = pd.read_csv('C:/wandata/IntoData/BYUI/CS450 - Machine Learning and Data Mining/wi2020/' + self.data, header=None)
        x = iris.iloc[:, :-1].values
        y = iris.iloc[:, self.ncol-1].values
        return x, y
    
    def encode(self):
        le = LabelEncoder()
        y = le.fit_transform(self.y)
        return y
    
    def split(self):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=self.size)
        return x_train, x_test, y_train, y_test
    
    def algo(self):
        if self.algo == 1:
            classifier = GaussianNB()
        else:
            classifier = HardCodedClassifier()
        
        classifier.fit(x_train, y_train)
        predictions = classifier.predict(x_test)
        return predictions
    
    def accuracy(self):
        score = accuracy_score(y_test, predictions)
        print("Accuracy: % .2f" %(score*100) + "%")
    

def main():    
    data = input('Type in the name of the dataset with its extension:')
    print()
    ncol = int(input('Type in the number of features (independent variables)'))
    print()
    size = float(input('What is the desired size for the test set? (between 0-1)'))
    print()
    print('What algorithm do you wish to use?')
    print()
    print('1: GaussianNB')
    print('2: HardCodedClassifier')
    algo = input()
    
    
    pred = predIris(data, ncol, size, algo)
    pred.accuracy()
    
    



if __name__ == "__main__":
    main()












# Loading iris dataset as txt file
iris = pd.read_csv('C:/wandata/IntoData/BYUI/CS450 - Machine Learning and Data Mining/wi2020/iris.data', header=None)
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
predictions_gau = classifier.predict(x_test)

# Accuracy
score = accuracy_score(y_test, predictions_gau)
score



#############


# My own algorithm: HardCodedClassifier

class HardCodedClassifier():
    def __init__(self):
        self.pred = []
    
    def fit(self, x, y):
        pass
    
    def predict(self, x):
        for i in x:
            self.pred.append(0)
        return self.pred
    

    
    

# Using my algorithm
classifier = HardCodedClassifier()
classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)
#predictions


# Accuracy
score2 = accuracy_score(y_test, predictions)
score2


