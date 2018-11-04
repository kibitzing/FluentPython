# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 20:08:18 2018

@author: jiyun
"""
from array import array
import math

class Vector3d:
    typecode = 'd'
    
    def __init__(self, x, y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def __iter__(self):
        return (i for i in (self.x, self.y, self.z))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
#    def __abs__(self):
#        return math.hypot(self.x, self.y)
    
#    def __bool__(self):
#        return bool(abs(self))
    
    
v1 = Vector3d(3,4,5)
print(v1.x, v1.y, v1.z)
x, y, z = v1 #언패킹 (__iter__ 덕분)
print(x,y,z)
print(v1)
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
print(v1)
octets = bytes(v1)
print(octets)


