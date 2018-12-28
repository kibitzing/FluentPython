#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 코루틴에서 값 반환하기

"""
from collections import namedtuple


Result = namedtuple('Result', 'count average')

def averager():
    total = .0
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

coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(29)

try:
    coro_avg.send(None)
except StopIteration as exc:
    result = exc.value
print(result)  # Result(count=2, average=19.5)