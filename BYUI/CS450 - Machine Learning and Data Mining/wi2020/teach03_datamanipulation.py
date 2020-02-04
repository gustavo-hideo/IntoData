# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:04:50 2020

@author: gusta
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# Loading data set
cols = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income']
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
                   header=None,
                   names=cols,
                   na_values=[' ?'])

le = LabelEncoder()
data['income'] = le.fit_transform(data['income'])
data.sex = le.fit_transform(data.sex)

# Dropping unused features
data.drop(['education','occupation'], axis=1, inplace=True)
data.dropna(axis=0, subset=['native-country'], inplace=True)


# Dealing with missing data

#Workclass
data['workclass_nan'] = 0
data.loc[data['workclass'].isnull(), 'workclass_nan'] = 1

work = data.loc[:,('income','workclass_nan')] #subset with income and workclass_nan only

# Ratio of income==1 for NAN and not-NAN
work1 = work[work['workclass_nan']==1] #subset with only NAN workclass
count_work1 = work1.shape[0]
work1_income1 = work1[work1['income']==1].shape[0] #number of incomes==1
work1_ratio = work1_income1 / count_work1
work1_ratio

work0 = work[work['workclass_nan']==0] #subset with only not-NAN workclass
count_work0 = work0.shape[0]
work0_income1 = work0[work0['income']==1].shape[0] #number of incomes==1
work0_ratio = work0_income1 / count_work0
work0_ratio
###
# People with lower income are more likely to leave the workclass null
###
data.fillna(value={'workclass':1}, inplace=True)
workclass_dict = {' Never-worked': 0,
                  ' Without-pay': 0,
                  ' Self-emp-not-inc': 1,
                  ' Self-emp-inc': 1,
                  ' Private': 1,
                  ' State-gov': 2,
                  ' Federal-gov': 2,
                  ' Local-gov': 2}
data.workclass.replace(workclass_dict, inplace=True)




# Categorical features
marital_status_dict = {' Never-married':0,
                       ' Married-AF-spouse':1,
                       ' Married-civ-spouse':1,
                       ' Married-spouse-absent':1,
                       ' Divorced':2,
                       ' Separated':2,
                       ' Widowed':2}
data['marital-status'].replace(marital_status_dict, inplace=True)

relationship_dict = {' Not-in-family':0,
                     ' Other-relative':0,
                     ' Own-child':0,
                     ' Unmarried':0,
                     ' Husband':1,
                     ' Wife':1}

data['relationship'].replace(relationship_dict, inplace=True)

race_dict = {' Amer-Indian-Eskimo':0,
             ' Black':0,
             ' Other':0,
             ' Asian-Pac-Islander':1,
             ' White':1}

data['race'].replace(race_dict, inplace=True)











