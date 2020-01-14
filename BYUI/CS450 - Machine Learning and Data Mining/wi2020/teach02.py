# -*- coding: utf-8 -*-
"""
basic K-Nearest Neighbors

Created on Mon Jan 13 10:00:06 2020

@author: gusta
"""



import numpy as np

x = np.array([3, 6])
y = np.array([5, 2])
data = np.array([[2, 3], [3, 4], [5, 7], [2, 7], [3, 2], [1, 2], [9, 3], [4, 1]])
animals = ["dog", "cat", "bird", "fish", "fish", "dog", "cat", "dog"]


dist = np.sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2)


# Euclidean Distance
def euc(a,b):
    dist = np.sqrt(np.sum((b-a)**2))
    return dist

# Compare x to each item in the data array
l_dist = []
for i in range(data.shape[0]):
    dist = euc(x,data[i])
    l_dist.append(dist)


# Find the smallest two distances
n = 2  # Number of smallest distances
ind_short = np.argsort(l_dist)[0:n]
# Return the distance and target of the smallest distances
[ (l_dist[i], animals[i]) for i in ind_short ]
    


