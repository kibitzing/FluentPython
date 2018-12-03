#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 28/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        implement overloading for '+', '*'
        
"""

from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools

class Vector:

    def __init__(self, components):
        self.typecode = 'd'

        self._components = array(self.typecode, components) # 배열로 저장한다. '보호된' 객체 속성

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return  'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        print('hi', index,slice(index))
        if isinstance(index, slice):
            print('hihi')
            return cls(self._components[index])

        elif isinstance(index, numbers.Integral):
            print('hello')
            return self._components[index]

        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))
    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a + b for a, b in pairs)

    def __mul__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a * (b+1) for a, b in pairs)


    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos =cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if len(name) == 1:
                if name in cls.shortcut_names:
                    error = 'Readonly attribute'
                elif name.islower():
                    error = "can't set attributes from 'a' to 'z' in {cls_name!r}"
                else:
                    error = ''
                if error:
                    msg = error.format(cls_name = cls.__name__ , attr_name = name)
                    raise AttributeError(msg)

        super().__setattr__(name,value)

import decimal

ctx = decimal.getcontext()
ctx.prec =40
one_third = decimal.Decimal('1')/decimal.Decimal('3')
print(one_third)

ctx.prec = 39

print(one_third ==+one_third)

v1 = Vector([3,4,5])
v2 = Vector([6,7,8])

print(v1+v2)
print(v1*v2)
