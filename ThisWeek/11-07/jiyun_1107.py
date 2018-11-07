# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:02:52 2018

@author: jiyun
"""
#p262 ~ p266

import math
from array import array

class Vector2d:
  #  __slots__ = ('__x','__y') # 한 번에 많은 객체 사용 시 유용 
    
    typecode = 'd'
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    
    @property #getter 의 메서드를 나타낸다
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
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
   
    def angle(self):
        return math.atan2(self.y, self.x)

    def __bool__(self):
        return bool(abs(self))
    
    def __format__(self, fmt_spec = ''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({},{})'
        components = (format(c,fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    
    def __hash__(self):
        return hash(self.x)^hash(self.y)
    
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


v1 = Vector2d(3,4)
print(v1.__dict__) #__slots__ 추가 하기 전 {'_Vector2d__x': 3.0, '_Vector2d__y': 4.0}
print(v1._Vector2d__x) #3.0
v1._Vector2d__x = 7
print(v1._Vector2d__x) #7

#print(v1.__slots__) #('__x', '__y')

