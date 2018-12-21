#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 코루틴을 기동하기 위한 decorator

"""
from functools import wraps
from inspect import getgeneratorstate


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
        

coro_avg = averager()
getgeneratorstate(coro_avg)  # 'GEN_SUSPENDED'

coro_avg.send(10)  # 10.0
coro_avg.send(30)  # 20.0
coro_avg.send(5)   # 15.0

coro_avg.send('spam')  # TypeError: unsupported operand type(s) for +=: 'float' and 'str'
coro_avg.send(60)  # StopIteration; 코루틴 안에서 예외처리가 완료되지 않았으므로 
                   #                StopIteration 예외 발생