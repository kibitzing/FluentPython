#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 07/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        pdate the code of 11-06 try double underbar and override
"""

from array import array
import math

class Vector3d:
    typecode = 'd'

    def __init__(self, x, y, z):
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

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

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('꺽쇠'):
            fmt_spec = fmt_spec[:-2]
            coords = (self.x, self.y, self.z)
            outer_fmt = '<{}, {}, {}>'
        elif fmt_spec.endswith('대괄호'):
            fmt_spec = fmt_spec[:-3]
            coords = (self.x, self.y, self.z)
            outer_fmt = '[{}, {}, {}]'
        else:
            coords = self
            outer_fmt = '({},{})'
        components = (format (c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y) ^ hash(self.z)
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

v1 = Vector3d(5,12,13)
v2 = Vector3d(5,12,13)
v3 = Vector3d(12,5,13)

print(v1._Vector3d__x)

class ShortVector3d(Vector3d):
    typecode = 'f'

    def __init__(self, x, y, z):
        self.__x_ = float(x)
        self.__y_ = float(y)
        self.__z = float(z)

    @property
    def x(self):
        return self.__x_

    @property
    def y(self):
        return self.__y_

    @property
    def z(self):
        return self.__z

sv1 = ShortVector3d(1,2,3)

print(sv1._ShortVector3d__x_)
print(sv1._ShortVector3d__y_)
print(sv1._ShortVector3d__z)

print(str(sv1))
print(repr(sv1))