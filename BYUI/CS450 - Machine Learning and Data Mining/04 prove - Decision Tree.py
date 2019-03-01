"""
04 PROVE | DECISION TREE
EXPERIMENTATION

guide: https://scikit-learn.org/stable/modules/tree.html
"""

from dfply import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split    # split in train and test
from sklearn import tree   # Decision tree
from sklearn.model_selection import cross_val_score   # score regressor
from sklearn import metrics     # accuracy_score
import graphviz   # plot trees
import datetime as dt
import matplotlib.pyplot as plt
import datadotworld as dw   # Load datasets

#pd.set_option('expand_frame_repr', False)     # show all variables when printing a dataset




#####################
# HEART DISEASE UCI #
#####################

# LOADING DATA
# heart = pd.read_csv("C:/DataScience/Datasets/Biology/heart disease uci/heart.csv")
heart = dw.load_dataset('gustavo-hideo/general', auto_update = True).dataframes['heart']
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
#cesarean = pd.read_csv('C:/DataScience/Datasets/Biology/cesarean uci/cesarean.csv')
cesarean = dw.load_dataset('gustavo-hideo/general', auto_update = True).dataframes['cesarean']
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










#####################
# WEATHER | REXBURG # PREDICT THE MIN TEMPERATURE
#####################

# USE MORE DATA (2000-2018 MAYBE...)

# LOADING DATA
#weather = pd.read_csv("C:/DataScience/Datasets/weather/rexburg1940-2018.csv")
weather = dw.load_dataset('gustavo-hideo/general', auto_update = True).dataframes['rexburg1940_2018']
rexburg = weather[weather['NAME'].str.contains("REXBURG")]
rexburg = rexburg.dropna(subset=['TMIN'])   # removing nulls TMIN
#pd.options.mode.chained_assignment = None  # avoid warning for converting string to datetime bellow
rexburg['DATE'] = pd.to_datetime(rexburg['DATE'])
rexburg['WEEK'] = rexburg['DATE'].dt.week  # creating column with WEEK NUMBER
rexburg['MONTH'] = rexburg['DATE'].dt.month  # creating column with MONTH NUMBER
rexburg['YEAR'] = rexburg['DATE'].dt.year  # creating column with YEAR
rexburg['DAY'] = rexburg['DATE'].dt.day  # creating column with DAY
# creating seasons
rexburg.loc[rexburg['MONTH'].isin([12,1,2]), 'SEASON'] = 4  # winter
rexburg.loc[rexburg['MONTH'].isin([3,4,5]), 'SEASON'] = 2  # spring
rexburg.loc[rexburg['MONTH'].isin([6,7,8]), 'SEASON'] = 1  # summer
rexburg.loc[rexburg['MONTH'].isin([9,10,11]), 'SEASON'] = 3  # fall

rex1 = rexburg[['DATE','DAY','MONTH','WEEK','YEAR','SEASON','TMIN']]   # selecting columns
# OVERALL WEEKS AVERAGE
weeks_avg = pd.DataFrame(rex1.groupby(['WEEK'])['TMIN'].mean())
weeks_avg = round(weeks_avg, 0)
weeks_avg = weeks_avg.rename(columns = {"TMIN":"WEEK_AVG"})
rex2 = pd.merge(rex1, weeks_avg, on=['WEEK'], how='left')

# AVERAGE PREVIOUS 7 DAYS
rex2['AVG_DAYS_7'] = round((rex2['TMIN'].shift(1) + \
                      rex2['TMIN'].shift(2) + \
                      rex2['TMIN'].shift(3) + \
                      rex2['TMIN'].shift(4) + \
                      rex2['TMIN'].shift(5) + \
                      rex2['TMIN'].shift(6) + \
                      rex2['TMIN'].shift(7)) / 7, 0)
# GETTING PREVIOUS DAYS
rex2['PREV_DAY_1'] = rex2['TMIN'].shift(1)
rex2['PREV_DAY_2'] = rex2['TMIN'].shift(2)

# REMOVING NULLS
rex2 = rex2.dropna(subset=['AVG_DAYS_7'])   
rex2 = rex2.dropna(subset=['PREV_DAY_1'])   
rex2 = rex2.dropna(subset=['PREV_DAY_2'])

rex = rex2[['DAY','WEEK','MONTH','SEASON','WEEK_AVG','AVG_DAYS_7','PREV_DAY_1','PREV_DAY_2', 'TMIN']]

#print(rex.isnull().sum())

# TRANSFORMING IN ARRAYS
xrex = np.array(rex)[:,0:len(rex.columns)-1]   # x | data
yrex = np.array(rex)[:,-1]   # y | target

# SPLITING DATA IN TRAIN AND TEST
x_train, x_test, y_train, y_test = train_test_split(xrex, yrex, test_size = .3)


# FITTING REGRESSION
reg = tree.DecisionTreeRegressor(max_depth=3)
reg = reg.fit(x_train, y_train)

# PREDICTION
predictions = reg.predict(x_test)

print("The R^2 Score is: {}" .format(round(reg.score(x_test, y_test),3)))



# PLOTTING
xrex_columns = rex.columns[0:len(rex.columns)-1]   # features (data) names
yrex_columns = rex.columns[-1]              # class (target) name

rex_plot = tree.export_graphviz(reg, out_file = None,
                                  feature_names = xrex_columns,
                                  class_names = yrex_columns,
                                  filled = True,    # paints nodes to indicate majorities
                                  rounded = True   # change format to boxes with rounded corners and font=Helvetica
                                  ,proportion = True)
rex_graph = graphviz.Source(rex_plot)

rex_graph


"""
FEATURE IMPORTANCE

A feature has its "importance" measured by calculating the increase in the
model's prediction error after permuting the feature. In other words, a feature
is "important" if shuffling its values increase the model error, because in
this case the model relied on the feature for the prediction.
The importance ranges between 0 and 1, where 1 is the most important.
"""

# FEATURE IMPORTANCE
#print("\n Features importance: \n {}" .format(reg.feature_importances_))
plt.plot(reg.feature_importances_, 'o')
plt.xticks(range(xrex.shape[1]), rex.columns[0:-1], rotation = 90)
plt.ylim(0,1)
plt.title("Rexburg Weather | features importance")
plt.show()






















