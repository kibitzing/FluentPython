#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 03/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        Implement <=, >=, <, >
"""

class Vector:
    def __init__(self, component):
        self._component = component

    def __eq__(self, other):
        return (len(self._component) == len(other._component)) and (all(a==b for a,b in zip(self._component, other._component)))

    def __ne__(self, other):
        return (len(self._component) != len(other._component)) and (
            any(a != b for a, b in zip(self._component, other._component)))

    def __abs__(self):
        absValue = 0
        for i in self._component:
            absValue += i^2

        return absValue/len(self._component)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


a = Vector([1,2,3])
b = Vector([1,2,3])
c = Vector([1,2,9])
print(a==b) # True
print(a>=b) # True
print(a<=b) # True
print(a==c) # False
print(a>b) # False
print(a>c) # False
print(c>a) # True
