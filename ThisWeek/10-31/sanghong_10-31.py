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
2018_10-31_Fluent_Python
@Author Sanghong.Kim

"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import torch
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
        #print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        print('Running Time : %0.8fs' % elapsed)
        return result
    return clocked

@clock
def f(a, b):
    '''For int'''
    a += b
    return a

@clock
def torchf(a,b):
    '''Only for torch tensor'''
    a.add(b)
    return a

class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

class TwilightBus_edit:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

def main(args):
    print("Add Your Code Below")
    x = torch.rand(1,2)
    y = torch.rand(1,2)
    t = (10, 20)
    u = (30, 40)
    print(x)
    print(y)

    # 1,1 tensor 의 경우 f 가 더 빨랐으나 그 외의 tensor 의 경우 미묘하지만 torch.Tensor.add 가 더 빨랐다.
    # 물론 int 형은 add 가 없다. 역시 해당 package 가 제공하는 것을 사용하는 이유가 있구나 싶다.
    print(f(x,y))
    print(type(x))
    print(torchf(x,y))

    # 농구팀에 있던 Tina가 사라지고 없던 Sanghong이 추가 되었다.
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
    bus = TwilightBus(basketball_team)
    bus.drop('Tina')
    bus.pick('Sanghong')
    print('basketball team :', basketball_team)
    print('bus passengers :', bus.passengers)

    # 농구팀은 변하지 않고 버스 탑승객만 변하는 것을 알 수 있다.
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
    bus = TwilightBus_edit(basketball_team)
    bus.drop('Tina')
    bus.pick('Sanghong')
    print('basketball team :', basketball_team)
    print('bus passengers :', bus.passengers)

# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
