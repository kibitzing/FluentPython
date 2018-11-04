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
2018_10-30_Fluent_Python
@Author Sanghong.Kim
오늘은 예제만 돌려 보았다.
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import copy

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

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


l1 = [3, [66, 55, 44], (7, 8, 9)]
a = [10, 20]
b = [a ,30]

@clock
def main(args):
    print("Add Your Code Below")
    l2 = list(l1)
    print(l2 == l1)
    print(l2 is l1)
    print('l1 : ', l1)
    print('l2 : ', l2)

    l2 = list(l1)
    l1.append(100)
    l1[1].remove(55)
    print('l1 : ', l1)
    print('l2 : ', l2)
    l2[1] += [33,22]
    l2[2] += (10,11)
    print('l1 : ', l1)
    print('l2 : ', l2)

    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))

    bus1.drop('Bill')
    print(bus2.passengers)
    print(bus3.passengers)
    print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
    print(bus3.passengers)

    a.append(b)
    print(a)
    c = copy.deepcopy(a)
    print(c)

# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
