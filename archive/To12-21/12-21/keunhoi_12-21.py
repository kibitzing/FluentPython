#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p473-477
# Example 16-8~15

'''
   예제 위주 작성
'''

from collections import namedtuple

class DemoException(Exception):
    """An exception type for the demonstration."""

# Example 16-8
def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')

# Example 16-12
def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')

# Example 16-13
Result = namedtuple('Result', 'count average')

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
    return Result(count, average)


if __name__ == '__main__':
    print('{0:=<50}'.format("Example 16-8"))
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(DemoException)