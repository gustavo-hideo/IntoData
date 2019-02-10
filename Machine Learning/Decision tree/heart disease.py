"""
GUSTAVO HIDEO HIGA CORREA
HEART DISEASE PREDICTION

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
# HEART DISEASE UCI #
#####################

# LOADING DATA
heart = pd.read_csv("C:/DataScience/Datasets/Biology/heart disease uci/heart.csv")
heart = heart[['age','sex','cp','chol','target']]  # using only "important" features after running "feature_important_"

xheart = np.array(heart)[:,0:len(heart.columns)-1]   # x | data
yheart = np.array(heart)[:,-1]   # y | target

# SPLITING DATA IN TRAIN AND TEST
x_train, x_test, y_train, y_test = train_test_split(xheart, yheart, test_size = .3)

# DECISION TREE
clf = tree.DecisionTreeClassifier(min_samples_leaf = 10, criterion = "entropy", splitter="random")  # stop tree to grow when the sample size of the nodes are less than 10
clf = clf.fit(x_train, y_train)

# PREDICTION
predictions = clf.predict(x_test)

# PREDICT PROBABILITIES
prediction_proba = clf.predict_proba(x_test)

# ACCURACY
print("\n Prediction for Heart tree: \n {}" .format(round(metrics.accuracy_score(y_test, predictions), 2)))


# PLOTTING
xheart_columns = heart.columns[0:len(heart.columns)-1]   # features (data) names
yheart_columns = heart.columns[-1]              # class (target) name

heart_plot = tree.export_graphviz(clf, out_file = None,
                                  feature_names = xheart_columns,
                                  class_names = yheart_columns,
                                  filled = True,    # paints nodes to indicate majorities
                                  rounded = True   # change format to boxes with rounded corners and font=Helvetica
                                  ,proportion = True)
heart_graph = graphviz.Source(heart_plot)

heart_graph

# FEATURE IMPORTANCE
plt.plot(clf.feature_importances_, 'o')
plt.xticks(range(xheart.shape[1]), heart.columns[0:-1], rotation = 90)
plt.ylim(0,1)
plt.title("Heart Disease | features importance")
plt.show()





