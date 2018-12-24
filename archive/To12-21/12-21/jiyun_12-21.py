# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:39:01 2018

@author: jiyun
"""
"""
코루틴 종료와 예외처리(이어서)
"""
from inspect import getgeneratorstate

class DemoException(Exception):
    """ 설명에 사용할 예외 유형"""
    
def demo_exc_handling():
    print('-> corountine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('***DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run')

def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('***DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')

exc_coro = demo_exc_handling()
next(exc_coro) # -> corountine started
exc_coro.send(99) #-> coroutine received: 99
exc_coro.close()
print(getgeneratorstate(exc_coro)) # GEN_CLOSED, Stop Itertation
exc_coro.send(DemoException) #-> coroutine received: <class '__main__.DemoException'>
exc_coro.throw(DemoException) #***DemoException handled. Continuing...
print(getgeneratorstate(exc_coro)) #GEN_SUSPENDED
#exc_coro.throw(ZeroDivisionError) # ZeroDivisionError

# getgeneratorstate(exc_coro)
# Out[17]: 'GEN_CLOSED'

"""
코루틴에서 값 반환하기
"""
from collections import namedtuple

Result = namedtuple('Result','count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count,average)

coro_avg = averager()
next(coro_avg)
print(coro_avg.send(10)) #None
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(20)
#coro_avg.send(None) # StopIteration: Result(count=4, average=17.5)

try:
    print(coro_avg.send(None))
except StopIteration as exc:
    result = exc.value
    print(result) # Result(count=4, average=17.5)
    
"""
yield from 사용하기
"""
def gen():
    for c in 'AB':
        yield c
    for i in range(1,3):
        yield i
        
def gen2():
    yield from 'AB'
    yield from range(1,3)
    
def chain(*iterables):
    for it in iterables:
        yield from it

print(list(gen()))
print(list(gen2()))
s = 'AB'
t = tuple(range(1,3))
print(list(chain(s,t)))

# 전부 ['A', 'B', 1, 2]

