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
2018_10-26_Fluent_Python
@Author Sanghong.Kim
오늘 고려대학교에서 진행하는 음성학강의를 보고 왔다.
11월 초쯤에 BTS "Fake Love" covered by Trump 라는 것이 올라올 것이다.
음성 합성기술을 이용하여 Trump의 목소리를 합성하여 트럼프가 Fake Love 라는 음악을 부르는 것인데 재미있다.

@d1
@d2
def f():
    print('f')

def f();
    print('f')

f = d1(d2(f))
와 동일 -> 누적 데커레이터
"""

# Import Modules
import time
import os
import sys
import argparse
import functools

registry_1 = []
registry_2 = set()

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

def register_1(func):
    print('running register(%s)' % func)
    registry_1.append(func)
    return func

def register_2(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry_2.add(func)
        else:
            registry_2.discard(func)

        return func

    return decorate

# 데커레이터로 구현하는 단순 연산기
@clock
class calc_class:
    def __init__(self, a, operator, b):
        self.operator = operator
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def __repr__(self):
        fmt = '{} {} {} = {}'
        if self.operator is '+':
            return fmt.format(self.a,self.operator,self.b,self.add())
        elif self.operator is '*':
            return fmt.format(self.a,self.operator,self.b,self.mul())
        else:
            return "sorry"


def calc_func(func):
    def value(a, b):
        if func.__name__ is 'add':
            y = '%i + %i = %i' % (a, b, a + b)
        elif func.__name__ is 'mul':
            y = '%i + %i = %i' % (a, b, a * b)
        else:
            y = "sorry"
        return y
    return value

@clock
@calc_func
def add(a, b):
    return a,b

@clock
@calc_func
def mul(a,b):
    return a,b

@clock
@calc_func
def sub(a,b):
    return a,b

@register_1
def f1():
    print('running f1()')

@register_2()
def f2():
    print('running f2()')

@register_2(active=False)
def f3():
    print('running f3()')

@register_2()
def f4():
    print('running f4()')

def main(args):
    print("Add Your Code Below")

    '''
    print('------------------ Example ---------------------')
    print('running main()')
    print('registry ->', registry_1)
    f1()

    register_2()

    # 등록된 것들을 동시에 반환
    print('registry ->', registry_2)
    f2()
    print('registry ->', registry_2)
    f3()
    print('registry ->', registry_2)
    f4()
    '''

    print('-------------- sum & mul using class -----------')
    print(calc_class(4, '+', 6))
    print(calc_class(4, '*', 6))
    print(calc_class(4, '-', 6))

    print('----------- sum & mul using decorator ----------')
    print(add(4, 6))
    print(mul(4, 6))
    print(sub(4, 6))
    print('------------------- Done -----------------------')


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
