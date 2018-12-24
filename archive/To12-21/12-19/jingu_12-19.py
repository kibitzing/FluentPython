#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 19/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
      used coroutine to implment summer and multiplier.
        
"""
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

print(next(coro_avg))

print(coro_avg.send(10))
print(coro_avg.send(20))
print(coro_avg.send(100))

def summer():
    sum  = 0.0

    while True:
        term = yield sum
        sum += term

summer1 = summer()

print(next(summer1))
print(summer1.send(10))
print(summer1.send(20))

def multiplier():
    multiple = 1.0

    while True:
        term = yield multiple
        multiple = multiple * term

myMul = multiplier()
print(next(myMul))
print(myMul.send(2))
print(myMul.send(20))
print(myMul.send(0.5))
