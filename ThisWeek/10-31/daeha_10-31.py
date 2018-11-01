#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 가변 매개변수에 대한 예제
"""

class TwilightBus:
    
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers
            
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)
        

python_study_team = ['Kim', 'Kang', 'Lee', 'Park', 'Bot']

bus = TwilightBus(python_study_team)
bus.drop('Lee')
bus.drop('Park')
print(python_study_team)  # ['Kim', 'Kang', 'Bot']



class NormalBus:
    
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)
        
python_study_team = ['Kim', 'Kang', 'Lee', 'Park', 'Bot']

bus = NormalBus(python_study_team)
bus.drop('Lee')
bus.drop('Park')
print(python_study_team)  # ['Kim', 'Kang', 'Lee', 'Park', 'Bot']
