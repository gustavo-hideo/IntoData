"""
GUSTAVO HIDEO HIGA CORREA
REXBURG WEATHER | PREDICTING DAILY LOWEST TEMPERATURE
guide: https://scikit-learn.org/stable/modules/tree.html
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split    # split in train and test
from sklearn import tree   # Decision tree
from sklearn.model_selection import cross_val_score   # score regressor
from sklearn import metrics     # accuracy_score
import graphviz   # plot trees
import datetime as dt
import matplotlib.pyplot as plt

#pd.set_option('expand_frame_repr', False)     # show all variables when printing a dataset








#####################
# WEATHER | REXBURG # PREDICT THE MIN TEMPERATURE
#####################

# USE MORE DATA (2000-2018 MAYBE...)

# LOADING DATA
weather = pd.read_csv("C:/DataScience/Datasets/weather/rexburg1940-2018.csv")

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





