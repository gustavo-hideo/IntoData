# DATA EXPLORATION

import pandas as pd



# LOADING DATA FROM INTERNET
iris = pd.io.parsers.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    ,header=None
    ,usecols=[0,1,2,3,4])




# RENAMING COLUMNS
iris.columns = ['col1', 'col2', 'col3', 'col4', 'y']


# DESCRIPTIVE
iris.head()