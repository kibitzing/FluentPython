#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 코루틴 종료와 예외 처리

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
        
        
class DemoException(Exception):
    """ 설명에 사용할 예외 유형 """
    
def demo_exc_handling():
    print('==> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('==> coroutine received: {!r}'.format(x))
    raise RuntimeError('This is should never run .')
    

def demo_finally():
    print('==> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('==> coroutine received: {!r}'.format(x))
    finally:
        print('==> coroutine ending')
    
exc_coro = demo_exc_handling()
next(exc_coro)  # ==> coroutine started.


# 1)
exc_coro.send(11)  # ==> coroutine received: 11
exc_coro.send(29)  # ==> coroutine received: 29
exc_coro.close()
getgeneratorstate(exc_coro)  # 'GEN_CLOSED'

# 2)
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException)  # *** DemoException handled. Continuing...
getgeneratorstate(exc_coro)  # 'GEN_SUSPENDED'

# 3)
exc_coro = demo_finally()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(ZeroDivisionError)  # ZeroDivisionError
getgeneratorstate(exc_coro)  # 'GEN_CLOSED'
