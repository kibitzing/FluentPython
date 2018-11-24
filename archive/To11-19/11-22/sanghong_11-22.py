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
2018_11-22_Fluent_Python
@Author Sanghong.Kim
몇가지 버전을 만들어 보려 하였으나 의미가 없어 잠시 접어 두었다.
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import collections

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

class DoppelDict1(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] *2)

class DoppelDict2(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

class DoppelDict3(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

class AnswerDict1(dict):
    def __getitem__(self, item):
        return 42

class AnswerDict2(collections.UserDict):
    def __getitem__(self, item):
        return 42

@clock
def main(args):
    print("Add Your Code Below")
    dd = DoppelDict1(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)
    dd = DoppelDict2(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)
    dd = DoppelDict3(one=1)
    print(dd)

    ad = AnswerDict1(a = 'foo')
    print(ad['a'])
    d = {}
    d.update(ad)
    print(d['a'])
    print(d)

    ad = AnswerDict2(a='foo')
    print(ad['a'])
    d = {}
    d.update(ad)
    print(d['a'])
    print(d)



# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
