# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:42:08 2018

@author: jiyun
"""

class Bus:
    
    def __init__(self, passengers = []):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
   
    def pick(self,name):
        self.passengers.append(name)
        print('%s가 탔습니다.' %name)
        
    def drop(self, name):
        self.passengers.remove(name)
        print('%s가 내렸습니다.' %name)

    
team = ['A','B','C']
bus = Bus(team)
bus.drop('A')
bus.pick('F')
print(team) #['A', 'B', 'C'] 
print(bus.passengers) #['B', 'C', 'F']
