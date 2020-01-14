# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:51:49 2020

@author: gusta
"""


class Movie():
    def __init__(self, title='', year=0, runtime=0):
        if runtime < 0:
            self.runtime = 0
        else:
            self.runtime = runtime
        self.title = title
        self.year = year
    
    def __repr__(self):
        return ('%s (%i) - %i mins' % (self.title, self.year, self.runtime))
    
    def movie_min(self):
        hours = self.runtime // 60
        minutes = self.runtime % 60
        print('%i hours and %i minutes' % (hours, minutes))
        

m = Movie()


m1 = Movie('John Wick', 1980, 90)
m2 = Movie('World Cup', 2002, 5)
m3 = Movie('testing', 2020, -20)
m3 = Movie('testing2', 2010, 180)

def create_movie_list():
    movies = []
    movies.append(m1)
    movies.append(m2)
    movies.append(m3)
    
    #movies2 = [i for i in movies if ]
    
    return movies
    
    
lmovies = create_movie_list()

for i in lmovies:
    print(i)
    
 

long_movies = [i for i in lmovies if i.runtime > 50]
for i in long_movies:
    print(i)


import random
stars = {i.title : random.uniform(0,5) for i in lmovies}
for title in stars:
    print('Title: %s - %.2f stars' % (title, stars[title]))




### Getting movie data
# movie_id
# views
# stars
    
import numpy as np
    
def get_movie_data():
    
    num_movies = 10
    
    array = np.zeros([num_movies, 3], dtype=np.float)
    
    for i in range(num_movies):
        movie_id = i+100
        views = random.randint(100, 1000)
        star = random.uniform(0,5)
        
        array[i][0] = movie_id
        array[i][1] = views
        array[i][2] = star
    
    return array

gendata = get_movie_data()
print('# rows: %i' % gendata.shape[0])
print('# columns: %i' % gendata.shape[1])
print()
print('First two rows:')
r = gendata[0:2,:]
print(r)
print()
print('Last two columns:')
c = gendata[:,-2:]
print(c)
print()
print('1D array using second column:')
d = gendata[:,1]
print(d)




