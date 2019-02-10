"""
GUSTAVO HIDEO HIGA CORREA
CESAREAN PREDICTION

guide: https://scikit-learn.org/stable/modules/tree.html
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split    # split in train and test
from sklearn import tree   # Decision tree
from sklearn.model_selection import cross_val_score   # score regressor
from sklearn import metrics     # accuracy_score
import graphviz   # plot trees
import matplotlib.pyplot as plt

#pd.set_option('expand_frame_repr', False)     # show all variables when printing a dataset



#####################
#   CESAREAN  UCI   #
#####################
"""
'Age' { 22,26,28,27,32,36,33,23,20,29,25,37,24,18,30,40,31,19,21,35,17,38 } 
'Delivery number' { 1,2,3,4 } 
'Delivery time' { 0,1,2 } -> {0 = timely , 1 = premature , 2 = latecomer} 
'Blood Pressure' { 2,1,0 } -> {0 = low , 1 = normal , 2 = high } 
'Heart Problem' { 1,0 } -> {0 = apt, 1 = inept } 

Caesarian { 0,1 } -> {0 = No, 1 = Yes } 
"""

# LOADING DATA
cesarean = pd.read_csv('C:/DataScience/Datasets/Biology/cesarean uci/cesarean.csv')
cesarean = cesarean[['HeartProblem','DeliveryTime','Caesarian']]

xcesarean = np.array(cesarean)[:,0:len(cesarean.columns)-1]   # x | data
ycesarean = np.array(cesarean)[:,-1]   # y | target

# SPLITING DATA IN TRAIN AND TEST
x_train, x_test, y_train, y_test = train_test_split(xcesarean, ycesarean, test_size = .3)

# DECISION TREE
clf = tree.DecisionTreeClassifier(min_samples_leaf = 10, criterion = "entropy", splitter="random")  # stop tree to grow when the sample size of the nodes are less than 10
clf = clf.fit(x_train, y_train)

# PREDICTION
predictions = clf.predict(x_test)

# PREDICT PROBABILITIES
prediction_proba = clf.predict_proba(x_test)

# ACCURACY
print("\n Prediction for Cesarean tree: \n {}" .format(round(metrics.accuracy_score(y_test, predictions), 2)))


# PLOTTING
xcesarean_columns = cesarean.columns[0:len(cesarean.columns)-1]   # features (data) names
ycesarean_columns = cesarean.columns[-1]              # class (target) name

cesarean_plot = tree.export_graphviz(clf, out_file = None,
                                  feature_names = xcesarean_columns,
                                  class_names = ycesarean_columns,
                                  filled = True,    # paints nodes to indicate majorities
                                  rounded = True   # change format to boxes with rounded corners and font=Helvetica
                                  ,proportion = True)
cesarean_graph = graphviz.Source(cesarean_plot)

cesarean_graph


# FEATURE IMPORTANCE
plt.plot(clf.feature_importances_, 'o')
plt.xticks(range(xcesarean.shape[1]), cesarean.columns[0:-1], rotation = 90)
plt.ylim(0,1)
plt.title("Cesarean | features importance")
plt.show()





