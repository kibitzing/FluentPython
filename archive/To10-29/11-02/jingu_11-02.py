#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 02/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        Implemented Vector3d Class
"""

from array import array
import math

class Vector3d:
    typecode = 'd'

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __iter__(self):
        return (i for i in (self.x, self.y, self.z))

    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r}, {!r}, {!r})'.format(classname, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(math.hypot(self.x, self.y), self.z)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

v1 = Vector3d(5,12,13)
print(v1.x, v1.y, v1.z)

x, y, z = v1
print(x,y,z)

print(v1)
print(repr(v1))

v1_clone = eval(repr(v1))
print(v1 == v1_clone)

octets = bytes(v1)
print(octets)

print(abs(v1))
print(bool(v1), bool(Vector3d(0,0,0)))

print(v1.frombytes(octets=octets))
