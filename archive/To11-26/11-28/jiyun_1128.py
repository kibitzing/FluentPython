# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:32:20 2018

@author: jiyun
"""
import math
from Vector import Vector


def __abs__(self):
    return math.sqrt(sum(x*x for x in self))

def __neg__(self):
    return Vector(-x for x in self)

def __pos__(self):
    return Vector(self) # Vector의 __init__


"""
x와 +x가 달라지는 경우 1 (정밀도)
"""

import decimal

ctx = decimal.getcontext()
ctx.prec = 40
one_third = decimal.Decimal('1') / decimal.Decimal('3')
print(one_third == +one_third) #True
ctx.prec = 28
print(one_third == +one_third) #False


"""
x와 +x가 달라지는 경우 2 (Counter의 덧셈은 양수만 취함)
"""
import collections

ct = collections.Counter('abracadabra')
print(ct) #Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct['r'] = -3
ct['d'] = 0
print(ct) #Counter({'a': 5, 'b': 2, 'c': 1, 'd': 0, 'r': -3})
print(+ct) #Counter({'a': 5, 'b': 2, 'c': 1})

"""
+ 연산 오버로딩
"""

v1 = Vector([3,4,5,6])
v2 = Vector([6,7])
#Vector에 __add__구현 
print(v1+v2) #(9.0, 11.0, 5.0, 6.0)

