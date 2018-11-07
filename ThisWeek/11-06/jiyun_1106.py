# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:47:33 2018

@author: jiyun
"""
import math
from array import array

class Vector2d:
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

"""
2차원 벡터 클래스
"""
v1 = Vector2d(3,4)
print(v1.x, v1.y) #언패킹, __iter__ 덕분
v1_clone = eval(repr(v1))
print(v1 == v1_clone) # True
octets = bytes(v1) 
print(octets) #b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
print(bool(Vector2d(0,0))) #False

"""
frombytes() 클래스 메서드 테스트
"""
v1_clone = Vector2d.frombytes(bytes(v1))
print(v1 == v1_clone) #True

"""
직교 좌표를 이용한 format() 테스트
"""
print(format(v1, '.3e')) #(3.000e+00,4.000e+00)
print(format(v1, '.3ep')) #<5.000e+00, 9.273e-01>

"""
angle() 메서드 테스트
"""
print(Vector2d(0,0).angle()) #0.0
epsilon = 10**-8
print(abs(Vector2d(0,1).angle() - math.pi/2) < epsilon) #True

"""
극좌표를 이용한 format() 테스트
"""
print(format(Vector2d(1,1),'p')) # <1.4142135623730951, 0.7853981633974483>

"""
x와 y 읽기 전용 프로퍼티 테스트
"""
print(v1.x, v1.y)
# v1.x=123 #AttributeError: can't set attribute

"""
해시 테스트
"""
print(hash(v1), set(v1)) #7 {3.0, 4.0}