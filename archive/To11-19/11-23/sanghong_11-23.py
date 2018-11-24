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
2018_11-23_Fluent_Python
@Author Sanghong.Kim
오늘 본 코드에서 다중 상속 및 다중 상속된 클래스에서 어떤식으로 데이터가 움직이는지 보았다.
금일 17:00에 발표가 있어서 긴장이 많이 된다.
ps. 연말에는 항상 연구실이 바쁜 것 같아 보인다.
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import tkinter

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

class A:
    def ping(self):
        print('ping:', self)

class B:
    def pong(self):
        print('pong:', self)

class C(A):
    def pong(self):
        print('PONG:',self)

class D(B,C):
    def ping(self):
        super().ping()
        print('post-ping:',self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

class D2(C,B):
    def ping(self):
        super().ping()
        print('post-ping:',self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

@clock
def main(args):
    print("Add Your Code Below")
    d = D()
    print(d.pong())
    print(C.pong(d))
    print_mro(D)
    print_mro(D2)
    print_mro(tkinter.Text)

# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
