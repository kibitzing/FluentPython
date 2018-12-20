#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p468-472
# Example 16-3~7

'''
   예제 위주 작성
'''

from functools import wraps
from inspect import getgeneratorstate

# Example 16-3
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

# Example 16-4
def Example16_4():
    coro_avg = averager()
    next(coro_avg)
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))

# Example 16-5
def coroutine(func):

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, *kwargs)
        next(gen)
        return gen
    return primer

# Example 16-6

@coroutine
def averager2():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

# Example 16-7
def Example16_7():
    coro_avg = averager2()
    print(coro_avg.send(40))
    print(coro_avg.send(50))
    try:
        coro_avg.send('spam')
    except TypeError:
        print('TypeError occurs')

    try:
        coro_avg.send(60)
    except StopIteration:
        print('StopIteration occurs')


if __name__ == '__main__':
    print('{0:=<50}'.format("Example 16-4"))
    Example16_4()
    print('{0:=<50}'.format("Example 16-7"))
    Example16_7()
