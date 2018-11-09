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
2018_11-09_Fluent_Python
@Author Sanghong.Kim
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
from array import array
import reprlib
import math


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
        return self._components[index]

    def __add__(self, other):
        components = []
        if len(self._components) != len(other._components):
            return ("Dimention of {}, {} doesn't match".format(self,other))
        else:
            for index in range(len(self._components)):
                components.append(self._components[index] + other._components[index])
            return "Sum of {}, {} is Vector({})".format(self,other,components)

    def __mul__(self, scalar):
        components = []
        if type(scalar) is str:
            return ("{} can't multiply by {}, {} is string!".format(self, scalar,scalar))
        else:
            for index in range(len(self._components)):
                components.append(self._components[index] * scalar)
            return "{} multiply by {} is Vector({})".format(self, scalar, components)

    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

class MySeq:
    def __getitem__(self, index):
        return index

@clock
def main(args):
    print("Add Your Code Below")
    v1 = Vector([3, 4, 5])
    print(len(v1))
    v2 = Vector([7, 5, 13])
    print(v1.__add__(v2))
    v3 = Vector([4, 5, 1, 10])
    print(v1.__add__(v3))
    print(v1.__mul__('a'))
    print(v1.__mul__(2))

    s = MySeq()
    print(s[1])
    print(s[1:5:2])
    print(s[1, 2, 3, [4, 5, 6]])

# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
