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
2018_11-07_Fluent_Python
@Author Sanghong.Kim
영문판 기준 page 293 ~ 9장 끝까지 보았습니다.
한글판 기준 page 346 ~ 9장 끝까지 보았습니다.
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import math
from array import array

class Vector2d:
    __slots__ = ('__x', '__y')

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

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

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

    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)



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
        print('[Elapsed Time : %0.8fs]' % (elapsed))
        return result
    return clocked

@clock
def main(args):
    print("Add Your Code Below")
    v1 = Vector2d(1.1, 2.2)
    dumpd = bytes(v1)
    print(dumpd)
    print(len(dumpd))
    # 클래스로 정의 하였기에 Typecode를 객체를 통해 변경하면 안됨
    # 다시한번 클래스와 객체와의 차이를 알 수 있는 기회
    # v1.typecode = 'f'
    Vector2d.typecode = 'f'
    dumpf = bytes(v1)
    print(dumpf)
    print(len(dumpf))




# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
