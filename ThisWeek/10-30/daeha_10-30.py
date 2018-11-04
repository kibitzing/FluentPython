#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 객체의 깊은 복사와 얕은 복사
"""

class Bus:
    
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)
        
        
# copy와 deepcopy의 비교
import copy

bus1 = Bus(['Alexa', 'Dean', 'Roman', 'Seth'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

id(bus1), id(bus2), id(bus3)

bus1.drop('Alexa')
print(bus2.passengers)  # ['Dean', 'Roman', 'Seth']

id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)

print(bus3.passengers)  # ['Alexa', 'Dean', 'Roman', 'Seth']

