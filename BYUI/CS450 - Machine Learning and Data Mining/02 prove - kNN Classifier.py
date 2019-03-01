# 02 PROVE - kNN CLASSIFIER


# LIBRARIES
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from collections import Counter


# MY ALGORITHM
class KNeighborsClassifier:

	def __init__(self, k):
		self.k = k

	def fit(self, data_train, targets_train):
		self.data_train = data_train
		self.targets_train = targets_train

	def predict(self, data_test):
		knn = []
		i = -1
		for x in data_test:
			distances = []
			i = i + 1
			j = -1
			for y in self.data_train:
				j = j + 1
				dist = round(sum(np.square(data_test[i] - self.data_train[j])), 2)
				distances.append(dist)
				
			pos = np.argsort(distances)      # returns the list of indexes in increasing sort, so I can get the indexes of the lowest 'X' distances
			neighbors = np.array(self.targets_train)[pos]   # neighbors contains the closest targets from data_train in the order of data_test (data_test, best_neighbor)
			neighbors = neighbors[:self.k]   # list with closest 'K' neighbors
			c = Counter(neighbors)     		 # function to find the most frequent element on a list
			best_neighbor = c.most_common(1)[0][0]      # most frequent element on the list
			knn.append(best_neighbor)        # append the chosen neighbor target to the KNN list
		
		return knn


  

# LOAD DATA
#iris = pd.read_csv("C:\\DataScience\\Datasets\\CS 450\\iris.csv", header = True)
iris = datasets.load_iris()
x = iris.data
y = iris.target





# SPLIT INTO DATA AND TARGETS
#x = pd.DataFrame(iris.values[:,0:-1])
#y = pd.Categorical(pd.Series(iris.values[:, -1], dtype = "category"))
#y_len = len(y.unique())
#y = y.rename_categories(range(y_len))
#y = pd.Series(y)

# 5.5  3.5  1.3  0.2

# SPLITING INTO TRAINING AND TESTING DATASETS
#
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
#print(x_train) # [5.3 3.7 1.5 0.2] # [7.2 3.2 6.  1.8]     last # [5.7 3.  4.2 1.2]
#print(x_test)  # [6.9 3.1 5.1 2.3] # [6.3 3.4 5.6 2.4]     last # [6.5 2.8 4.6 1.5]

# USING MY ALGORITHM
classifier = KNeighborsClassifier(3)

classifier.fit(x_train, y_train)

targets_predicted = classifier.predict(x_test)
print(targets_predicted)



# Accuracy
acc = accuracy_score(y_test, targets_predicted)
print("\n Accuracy of HardCodedClassifier's prediction: \n {}" .format(acc))
