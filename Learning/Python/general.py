# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:15:02 2020

@author: gusta
"""


# Import datasets from R
from rpy2.robjects import r, pandas2ri

def data(name): 
    return pandas2ri.ri2py(r[name])
###
    


mt = data('mtcars')

mt.shape
mt.describe()
mt.head(3)
mt.loc[8]
mt.columns
mt.loc[8, 'mpg']
mt.loc[range(4,6)]







