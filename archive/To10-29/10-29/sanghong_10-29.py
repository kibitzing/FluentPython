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
2018_10-29_Fluent_Python
@Author Sanghong.Kim
"""

# Import Modules
import time
import os
import sys
import argparse
import functools

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

charles = {'name': 'Charles L. Dodgson', 'born': 1832}
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

@clock
def main(args):
    print("Add Your Code Below")
    lewis = charles
    print(lewis is charles)
    print(id(charles), id(lewis))
    lewis['balance'] = 950
    print(charles)
    # 같은 것들이 할당 되어 있으나 다른 객체이다. ==는 값을 비교, is는 정체성을 비교
    print(alex == charles)
    print(alex is not charles)

    print(t1 == t2)
    print(id(t1[-1])) # t1[-1] == t1[2] 튜블내의 리스트는 가변형이다.
    t1[-1].append(99)
    print(id(t1[-1]))
    print(t1)
    print(t2)
    print(t1 == t2)

    return 0

# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
