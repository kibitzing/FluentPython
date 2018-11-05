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
2018_11-05_Fluent_Python
@Author Sanghong.Kim
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import math
from array import array
from datetime import datetime

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
        #print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        print('Elapsed Time : %0.8fs' % (elapsed))
        return result
    return clocked

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
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

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.x, self.y)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        componets = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*componets)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

@clock
def main(args):
    print("Add Your Code Below")
    v1 = Vector2d(3,4)
    v2 = Vector2d(3.1, 4.2)

    print(v1)

    print(format(v1))
    print(format(v1,'p'))

    print(hash(v1),',', hash(v2))
    print(set([v1, v2]))

    n = 2
    a = math.pi/n
    b = math.sin(a)

    print('(pi over {:}) is : {:.04f}, sin(pi over {:}) is : {:.04f}'.format(n,a,n,b))




# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
