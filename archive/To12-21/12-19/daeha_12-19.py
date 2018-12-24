#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 코루틴 기본 예제

"""



def coroutine():
    print('==> coroutine started!')
    x = yield
    print('==> coroutine received:', x)
    

my_coro = coroutine()
my_coro  # <generator object coroutine at 0x10d034a40>

next(my_coro)  # ==> coroutine started!

my_coro.send(42)  # StopIteration