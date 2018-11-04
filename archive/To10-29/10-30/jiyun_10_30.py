# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:16:27 2018

@author: jiyun
"""

t1 = (1,2, [30,40])
t2 =(1,2, [30,40])

print(t1 == t2) #True
print(t1 is t2) #False

t1[-1].append(99)

print(t1 == t2) #False
print(t1 is t2) #False

#######################################################

import copy

class Bus:
    
    def __init__(self, passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)
        
        
bus1 = Bus(['A','B','C','D'])

bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

bus1.drop('B')
bus1.pick('E')

print(bus2.passengers) #['A', 'C', 'D', 'E']

print(bus3.passengers) #['A', 'B', 'C', 'D']


