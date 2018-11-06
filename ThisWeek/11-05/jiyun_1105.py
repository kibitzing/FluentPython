# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:51:44 2018

@author: jiyun
"""
class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    @staticmethod
    def statmeth(*args):
        return args
    
print(Demo.klassmeth()) #(<class '__main__.Demo'>,)
print(Demo.klassmeth('spam'))
print(Demo.statmeth()) #()
print(Demo.statmeth('spam'))   # 클래스와 함께 작동하지 않음


########################################################
import math
import array

class Vector2d:
    typecode = 'd'
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
   
    def __bool__(self):
        return bool(abs(self))
    
    def __format__(self, fmt_spec = ''):
        components = (format(c,fmt_spec) for c in self)
        return '({},{})'.format(*components)
    
    
v1 = Vector2d(3,4)
print(format(v1, '.3e')) #(3.000e+00,4.000e+00)
