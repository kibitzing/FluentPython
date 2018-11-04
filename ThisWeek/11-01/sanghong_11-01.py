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
2018__Fluent_Python
@Author Sanghong.Kim
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import weakref

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

def bye():
    print('바람과 함께 사라지다')

class Cheese:
    def __init__(self,kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

@clock
def main(args):
    print("Add Your Code Below")
    s1 = {1, 2, 3}
    s2 = s1

    print('------------------ ex 8-16 --------------------')
    ender = weakref.finalize(s1, bye)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 'spam'
    print(ender.alive)

    print('------------------ ex 8-17 --------------------')
    s1 = {1, 2, 3}
    wref = weakref.ref(s1)
    print(wref)
    print(wref())
    s1 = {4, 5, 6, 7}
    print(wref())
    print(wref is None)
    print(wref() is None)
    stock = weakref.WeakValueDictionary()

    print('------------------ ex 8-19 --------------------')
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

    for cheese in catalog:
        stock[cheese.kind] = cheese

    print(sorted(stock.keys()))
    del catalog
    print(sorted(stock.keys()))
    del cheese
    print(sorted(stock.keys()))

    print('---------------- ex 8-20,21 -------------------')
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    t3 = t1[:]
    t4 = (1, 2, 3)

    print(t1 is t2)
    print(t1 is t3)
    print(t1 is t4)

    w1 = 'ABC'
    w2 = 'ABC'
    w3 = 'AB' + 'C'
    print(w1 is w2)
    print(w1 is w3)








# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
