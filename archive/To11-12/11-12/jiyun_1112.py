# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:43:29 2018

@author: jiyun
"""

# 원서 기준 287~291

import math
from array import array
import reprlib
import numbers

class Vector:
   
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components) #벡터 요소 배열로 저장
    
    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components) #제한된 길이로 표현하기 위함, array 'd' 노출하지 않기 위함
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._cmoponents))
    
    def __len__(self):
        return len(self._components)
    
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls = cls))
     
    shortcut_names = 'xyzt'   
    
    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))
        
    def __setattr__(self,name,value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}' 
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name = cls.__name__, attr_name = name)
                raise AttributeError(msg)
        super().__setattr__(name,value) #에러가 발생하지 않을 때
     
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv) # '*'로 언패킹 할 필요 없음, 바로 생성자에 전달

v1 = Vector(range(10))
print(len(v1)) #10
#print(v1[1,4]) #TypeError: Vector indices must be integers
print(v1.x) #0.0
# v1.x = 100 # (__setattr__()메서드 생성 후) AttributeError: readonly attribute 'x'
print(v1.x) #100 이 때 __getattr__()메서드 호출하지 X
print(v1)

###############################################################################3

import functools
import operator

print(functools.reduce(lambda a,b : a^b, range(6)))
print(functools.reduce(operator.xor, range(6)))

