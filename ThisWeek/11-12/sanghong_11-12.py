#!/usr/bin/envs python3
# -*- coding: utf-8 -*-

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_11-12_Fluent_Python
@Author Sanghong.Kim
오늘의 예제는 v.x, v.y 등 attribute와 관련된 예제이다.
책에서는 x,y,z,t 로 나누었으나 해당 코드는 x,y,z, a to len(self._components) 를 string 모듈을 import 하여 구현하였다.
set attribute 도 마찬가지 이다.
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import numbers
from array import array
import reprlib
import math
import string

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

class Vector:
    typecode = 'd'
    shortcut_names = 'xyz'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return 'Vector({})'.format(str(tuple(self)))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                 bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x* x for x in self))

    def __bool__(self):
        return bool(abs(self))

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
            raise TypeError(msg.format(cls=cls))

    def __add__(self, other):
        if len(self._components) != len(other._components):
            return ("Dimention of {}, {} doesn't match".format(self,other))
        else:
            components = [self._components[index] + other._components[index] for index in range(len(self._components))]
            return "Sum of {}, {} is Vector({})".format(self,other,components)

    def __mul__(self, scalar):
        if type(scalar) is str:
            return ("{} can't multiply by {}, {} is string!".format(self, scalar,scalar))
        else:
            components = [self._components[index] * scalar for index in range(len(self._components))]
            return "{} multiply by {} is Vector({})".format(self, scalar, components)

    def __getattr__(self, name):
        cls = type(self)
        if 3 < len(self._components) < 26:
            shortcut_names = 'xyz' + string.ascii_lowercase[:len(self._components)-3]
        elif 26 <= len(self._components):
            shortcut_names = 'xyz' + string.ascii_lowercase[:23]
        else:
            shortcut_names = self.shortcut_names
        if len(name) == 1:
            # self.shortcut_names 로 하면 되는데 cls.shortcut_names로 하면 안됨..
            pos = shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                self.shortcut_names = shortcut_names
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}, objects that can be attribute : {!r}'
        raise AttributeError(msg.format(cls,name,shortcut_names))


    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif self.shortcut_names.find(name) == -1:
                error = "can't set attributes '{attr_name!r} in {cls_name!r}'"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

@clock
def main(args):
    print("Add Your Code Below")
    v = Vector(range(15))
    print(v[-1])
    print(v[1:4])
    # __str__을 수정하여 output이 Vector((6.0,)) 으로 나타난다, ,를 없애는 방법을 찾고 싶다.
    print(v[-1:])
    #print(v[1,2])
    print(v.a)
    print(v.b)
    v.a = 50
    v.k = 20
    print(v.a)
    print(v.k)


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
