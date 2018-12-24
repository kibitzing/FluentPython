# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:16:34 2018

@author: jiyun
"""
from inspect import getgeneratorstate
from functools import wraps

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
print(getgeneratorstate(coro_avg)) # GEN_CREATED
next(coro_avg) # 코루틴 활성화
print(getgeneratorstate(coro_avg)) #GEN_SUSPENDED
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))

def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager2():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
    
coro_avg2 = averager2()
print(coro_avg2.send(10)) # next 호출하지 않아도 사용 가능
print(coro_avg2.send(40))
print(coro_avg2.send('spam')) # TypeError

# coro_avg2.send(20) StopIteration
