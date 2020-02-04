# -*- coding: utf-8 -*-
"""
Prove 04 - Decision Tree Classifier
Created on Wed Jan 29 17:28:29 2020
@author: gusta
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_graphviz
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.externals.six import StringIO
from IPython.display import Image  
import pydotplus



le = LabelEncoder()

##############
# titanic 
##############

data = pd.read_csv('C:/data/titanic/train.csv')
data = data.loc[:,('Survived','Pclass','Sex','Age','SibSp','Parch','Fare')]
data.dropna(inplace=True)

#data.Age = data.Age.map(lambda x: 0 if x<20 else (1 if x<30 else (2 if x<50 else 3)))
#data.SibSp = data.SibSp.map(lambda x: 2 if x>1 else x)
#data.Parch = data.Parch.map(lambda x: 2 if x>1 else x)
#data.Fare = data.Fare.map(lambda x: 0 if x<20 else (1 if x<50 else 2))


data.Sex = le.fit_transform(data.Sex)

x = data.iloc[:,1:]
y = data.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)




# tree
dtree = DecisionTreeClassifier()
dtree.fit(x_train, y_train)

pred = dtree.predict(x_test)
accuracy_score(y_test, pred)




# Plot
dot_data = StringIO()
export_graphviz(dtree, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('C:/Users/gusta/Downloads/tree.png')
Image(graph.create_png())



# One Hot Encoding for Pclass
one_hot = pd.get_dummies(data.Pclass, drop_first=True)
data.drop('Pclass', axis=1, inplace=True)
data = data.join(one_hot)

x = data.iloc[:,1:]
y = data.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)

# tree
dtree = DecisionTreeClassifier()
dtree.fit(x_train, y_train)

pred = dtree.predict(x_test)
accuracy_score(y_test, pred)







#######
# Different parameters
dtree = DecisionTreeClassifier(criterion='gini')
dtree.fit(x_train, y_train)
pred = dtree.predict(x_test)
print('Criterion=gini', accuracy_score(y_test, pred))


dtree = DecisionTreeClassifier(criterion='entropy')
dtree.fit(x_train, y_train)
pred = dtree.predict(x_test)
print('Criterion=entropy', accuracy_score(y_test, pred))

# Limiting depth of the tree
dtree = DecisionTreeClassifier(criterion='gini', max_depth=5)
dtree.fit(x_train, y_train)
pred = dtree.predict(x_test)
print('Criterion=entropy, max_depth=5', accuracy_score(y_test, pred))

max_depth = []
acc_gini = []
acc_entropy = []
for i in range(1,30):
    dtree = DecisionTreeClassifier(criterion='gini', max_depth=i)
    dtree.fit(x_train, y_train)
    pred = dtree.predict(x_test)
    acc_gini.append(accuracy_score(y_test, pred))
    ####
    dtree = DecisionTreeClassifier(criterion='entropy', max_depth=i)
    dtree.fit(x_train, y_train)
    pred = dtree.predict(x_test)
    acc_entropy.append(accuracy_score(y_test, pred))
    ####
    max_depth.append(i)

d = pd.DataFrame({'acc_gini':pd.Series(acc_gini), 
                  'acc_entropy':pd.Series(acc_entropy),
                  'max_depth':pd.Series(max_depth)})


# visualizing changes in parameters
plt.plot('max_depth','acc_gini', data=d, label='gini')
plt.plot('max_depth','acc_entropy', data=d, label='entropy')
plt.xlabel('max_depth')
plt.ylabel('accuracy')
plt.legend()



##############
# voting 
##############
names = ['class','handicapped','water-project-cost-sharing','adoption-of-the-budget-resolution','physician-fee-freeze','el-salvador-aid','religious-groups-in-schools','anti-satellite-test-ban','aid-to-nicaraguan-contras','mx-missile','immigration','synfuels-corporation-cutback','education-spending','superfund-right-to-sue','crime','duty-free-exports','export-administration-act-south-africa']
data = pd.read_csv('C:/data/voting/house-votes-84.data',
                   names = names)

data.replace('?', np.nan, inplace=True)
data.dropna(inplace=True)
data = data.apply(le.fit_transform)

x = data.iloc[:,1:]
y = data.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)


# tree
dtree = DecisionTreeClassifier()
dtree.fit(x_train, y_train)

pred = dtree.predict(x_test)
accuracy_score(y_test, pred)




# Plot
dot_data = StringIO()
export_graphviz(dtree, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('C:/Users/gusta/Downloads/tree.png')
Image(graph.create_png())
    
    











##############
# lenses 
##############
names = ['lenses','age','spectacle','astigmatic','tearprod']
data = pd.read_csv('C:/data/lenses/lenses.data',
                   sep='\s+',
                   names=names,
                   engine='python')

x = data.iloc[:,1:]
y = data.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=5)


# tree
dtree = DecisionTreeClassifier()
dtree.fit(x_train, y_train)

pred = dtree.predict(x_test)
accuracy_score(y_test, pred)




# Plot
dot_data = StringIO()
export_graphviz(dtree, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('C:/Users/gusta/Downloads/tree.png')
Image(graph.create_png())
    

    















##############
# lenses 
##############

names = ['mpg','cyl','disp','hp','wg','acc','model_year','origin','car_name']
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data',
                   sep='\s+',names=names)

data.replace('?',np.nan, inplace=True)
data.dropna(inplace=True)

x = data.iloc[:,1:-1]
y = data.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=5)


# tree
dtree = DecisionTreeRegressor()
dtree.fit(x_train, y_train)

pred = dtree.predict(x_test)
# Mean Absolute Error for regression
mean_absolute_error(y_test, pred)




# Plot
dot_data = StringIO()
export_graphviz(dtree, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('C:/Users/gusta/Downloads/tree.png')
Image(graph.create_png())
    










    

