#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 20/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        implemented simple dataset getter using coroutine + decorator pattern
"""
from functools import wraps
from inspect import getgeneratorstate
import random

def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen =func(*args, **kwargs)
        next(gen)
        return(gen)
    return primer

@coroutine
def datasetGetter():
    dataset = [(i,3*i) for i in range(20)]
    random_number = 0
    while True:
        term = yield dataset[random_number][1]
        random_number = term

coro_dtGetter = datasetGetter()

print(getgeneratorstate(coro_dtGetter))
print(coro_dtGetter.send(int(random.random()*20)))
print(coro_dtGetter.send(int(random.random()*20)))
print(coro_dtGetter.send(int(random.random()*20)))

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

coro_avg =averager()

print(getgeneratorstate(coro_avg))
print(coro_avg.send(10))
