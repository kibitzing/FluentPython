#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p463-467
# Example 16-1~2

'''
   예제 위주 작성
'''

# Example 16-1
def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine recieved:', x)

# Example 16-2
def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)

if __name__ == '__main__':
    print('{0:=<50}'.format("Example 16-1"))
    my_coro = simple_coroutine()
    print(my_coro)
    print(next(my_coro))
    # print(my_coro.send(32))

    print('{0:=<50}'.format("Example 16-2"))
    my_coro2 = simple_coro2(14)
    from inspect import getgeneratorstate
    print(getgeneratorstate(my_coro2))
    print(next(my_coro2))
    print(getgeneratorstate(my_coro2))
    print(my_coro2.send(28))
    # print(my_coro2.send(99))
    print(getgeneratorstate(my_coro2))