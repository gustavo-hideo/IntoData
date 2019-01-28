# 03 PROVE: USING kNN WITH MORE INTERESTING DATA

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split    # split in train and test
from sklearn.neighbors import KNeighborsClassifier    # kNN for classification
from sklearn.neighbors import KNeighborsRegressor    # kNN using regression
from sklearn import preprocessing   # standardization and normalization
from sklearn import metrics     # accuracy_score


# LOADING DATASETS

# CAR EVALUATION
car = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"
                 ,header = None)

car_headers = ['buying_price', 'price_maint', 'doors', 'persons', 'lug_boot', 'safety', 'y_acceptance']
car.columns = car_headers


# AUTOMOBILE MPG
mpg = pd.io.parsers.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original"
                 ,header = None
                 ,sep = "\s+")

mpg_headers = ['y_mpg', 'cyl', 'disp', 'hp', 'wt', 'acc', 'year', 'origin', 'name']
mpg.columns = mpg_headers                 


# STUDENT PERFORMANCE
students = pd.read_csv("C:/DataScience/Datasets/student_performance/student-mat.csv"
                 ,header = 0     # defines the header as the first row
                 ,sep = ";")



# DATA WRANGLING

# CAR EVALUATION
cleaning_cols = {"buying_price":  {"vhigh": 4
                                  ,"high": 3
                                  ,"med": 2
                                  ,"low": 1},
                "price_maint":    {"vhigh": 4
                                  ,"high": 3
                                  ,"med": 2
                                  ,"low": 1},
                "doors":          {"2": 2
                                  ,"3": 3
                                  ,"4": 4
                                  ,"5more": 5},
                "persons":        {"2": 2
                                  ,"4": 4
                                  ,"more": 6},
                "lug_boot":       {"small": 1
                                  ,"med": 2
                                  ,"big": 3},
                "safety":         {"low": 1
                                  ,"med": 2
                                  ,"high": 3},
                "y_acceptance":   {"unacc": 0
                                  ,"acc": 1
                                  ,"good": 2
                                  ,"vgood": 3}}

car.replace(cleaning_cols, inplace = True)                                  

# PREPARING DATASETS TO SPLIT INTO TRAIN AND TEST
xcar = np.array(car)[:, 0:6]   # transforming into array and removing last column (y)
ycar = np.array(car)[:, -1]   # # transforming into array and keeping only the last column (y)

x_train, x_test, y_train, y_test = train_test_split(xcar, ycar, test_size = .3)

# STANDARDIZATION AND NORMALIZATION
"""
std_scale = preprocessing.StandardScaler().fit(car[car.columns[0:(len(car.columns)-1)]])
car_std = std_scale.transform(car[car.columns[0:(len(car.columns)-1)]])

print('Mean after standardization:\nbuying_price={:.2f}, price_maint={:.2f}, doors={:.2f}, persons={:.2f}, lug_boot={:.2f}, safety={:.2f}'
      .format(car_std[:,0].mean(), car_std[:,1].mean(), car_std[:,2].mean(), car_std[:,3].mean(), car_std[:,4].mean(), car_std[:,5].mean()))

print('\nMean after standardization:\nbuying_price={:.2f}, price_maint={:.2f}, doors={:.2f}, persons={:.2f}, lug_boot={:.2f}, safety={:.2f}'
      .format(car_std[:,0].std(), car_std[:,1].std(), car_std[:,2].std(), car_std[:,3].std(), car_std[:,4].std(), car_std[:,5].std()))
"""

std_scale = preprocessing.StandardScaler().fit(x_train)
x_train_std = std_scale.transform(x_train)
x_test_std = std_scale.transform(x_test)


# CLASSIFICATION kNN
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)

# ACCURACY
print("\n Prediction for car: \n {}" .format(metrics.accuracy_score(y_test, predictions)))






# AUTOMOBILE MPG
mpg['hp'].fillna(mpg['hp'].mean(), inplace = True)   # replacing null hp with hp mean
mpg = mpg[mpg['y_mpg'].notnull()]    # removing rows where y_mpg is null

print(mpg.isnull().sum())

# PREPARING DATASETS TO SPLIT INTO TRAIN AND TEST
xmpg = np.array(mpg)[:, 1:8]
ympg = np.array(mpg)[:, 0]

x_train, x_test, y_train, y_test = train_test_split(xmpg, ympg, test_size = .3)

# STANDARDIZATION AND NORMALIZATION
std_scale = preprocessing.StandardScaler().fit(x_train)
x_train_std = std_scale.transform(x_train)
x_test_std = std_scale.transform(x_test)


# REGRESSION
regr = KNeighborsRegressor(n_neighbors=3)
regr.fit(x_train, y_train)
predictions = regr.predict(x_test)

# ACCURACY
print("\n Prediction for mpg: \n {}" .format(metrics.r2_score(y_test, predictions)))






# STUDENTS PERFORMANCE
# 'Mjob'. 1 = at home. 0 = out of home.
# 'guardians'. 1 = a parent. 0 = other.
students = students[students.columns.drop(['reason', 'Fjob', 'G1', 'G2'])]  # Dropping unused columns
students['Mjob'] = np.where(students['Mjob'] == "at_home", 1, 0)
students['guardian'] = np.where(students['guardian'] == "other", 0, 1)

cleaning_cols = {"school":       {"GP": 1
                                 ,"MS": 2},
                "sex":           {"M": 1
                                 ,"F": 2},
                "address":       {"U": 1
                                 ,"R": 2},
                "famsize":       {"LE3": 1
                                 ,"GT3": 2},
                "Pstatus":       {"T": 1
                                 ,"A": 0},
                "schoolsup":     {"yes": 1
                                 ,"no": 0},
                "famsup":        {"yes": 1
                                 ,"no": 0},
                "paid":          {"yes": 1
                                 ,"no": 0},
                "activities":    {"yes": 1
                                 ,"no": 0},
                "nursery":       {"yes": 1
                                 ,"no": 0},
                "higher":        {"yes": 1
                                 ,"no": 0},
                "internet":      {"yes": 1
                                 ,"no": 0},
                "romantic":      {"yes": 1
                                 ,"no": 0}
                }
students.replace(cleaning_cols, inplace = True)                

# PREPARING DATASETS TO SPLIT INTO TRAIN AND TEST
xstudents = np.array(students)[:, 0:28]
ystudents = np.array(students)[:, -1]

x_train, x_test, y_train, y_test = train_test_split(xstudents, ystudents, test_size = .3)

# STANDARDIZATION AND NORMALIZATION
std_scale = preprocessing.StandardScaler().fit(x_train)
x_train_std = std_scale.transform(x_train)
x_test_std = std_scale.transform(x_test)


# REGRESSION
regr = KNeighborsRegressor(n_neighbors=3)
regr.fit(x_train, y_train)
predictions = regr.predict(x_test)

# ACCURACY
score = []
for y in predictions:
    for t in y_test:
        if abs(y - t) <= abs(y_test.mean() * 0.1):
            score.append(1)
        else:
            score.append(0)

score = np.array(score)
print("The score is: \n {}" .format(score.sum() / len(score)))


