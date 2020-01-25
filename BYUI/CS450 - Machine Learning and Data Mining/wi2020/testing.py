# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:42:29 2020

@author: gusta
"""

x = [1,2,3,4,5, 5, 4, 4, 3, 2, 1, 4, 3, 4, 3, 4, 3, 5 , 2, 5, 1, 4, 3, 2, 4, 3, 2, 3, 5 , 2, 5, 1, 4, 3, 4, 3, 2, 3, 5 , 2, 5, 1, 4, 3, 4, 3, 2, 3, 5 , 2, 5, 4, 5, 4, 2, 2, 3,2]
a = [1,2,3,4,5, 5, 4, 4, 3, 2, 1, 4, 3, 4, 3, 2, 3, 5 , 2, 5, 4, 5, 4, 2, 2, 3,2]




from collections import Counter
import numpy as np




class mode():
    def __init__(self, candidates, data):
        self.candidates = dict(Counter(candidates))
        self.data = Counter(data)
        
    def m_max(self):
        max_value = max(list(self.candidates.values()))
        self.maxs = [value for value, freq in self.candidates.items() if freq == max_value]
    
    def m_choice(self):
        maxs = self.maxs
        if len(maxs) == 1:
            choices = maxs
        else:
            opts = []
            for i in maxs:
                opts.append(self.data[i])
            opts_index = np.argmax(opts)
            choices = maxs[opts_index]
        return choices

mode(a,x).m_choice()




    


counter = Counter(a)
counterx = Counter(x)


counter_dict = dict(counter)  # Creates a dictionary with every value and its frequency
max_value = max(list(counter_dict.values())) # the max number for frequency
maxs = [value for value, freq in counter_dict.items() if freq==max_value]  #all items with frequency equals to max_value
if len(maxs) == 1:
    choice = maxs
else:     # if there is a tie
    opts = []
    for i in maxs:
        opts.append(counterx[i])  #gets the frequency of each possible choice in the full data
    opts_i = np.argmax(opts)  #gets the index of the higher frequency
    choice = maxs[opts_i]  #chooses the option with higher frequency in the full data

choice
    
    






