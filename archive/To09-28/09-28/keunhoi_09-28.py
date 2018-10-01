#!/usr/bin/env python3
# -*- coding: utf-8 -*-

RANGE = 10000000
Haystack_key = tuple(range(RANGE))
Haystack_value = tuple(range(RANGE))
Haystack = dict(zip(Haystack_key,Haystack_value))
Needles = tuple(range(500))+tuple(range(-500,0))

def runtime(Haystack, Needles, mode):
    import timeit

    if mode == 'set':
        haystack = set(Haystack)
        needles = set(Needles)

        start = timeit.default_timer()
        found = len(needles & haystack)
        end = timeit.default_timer()
        t = end - start
        return t

    elif mode == 'list':
        found = 0
        haystack = list(Haystack)
        needles = list(Needles)
        start = timeit.default_timer()

        for needle in needles:
            if needle in haystack:
                found += 1

        end = timeit.default_timer()
        t = end - start
        return t

    elif mode == 'dict':
        haystack = Haystack
        needles = dict(zip(Needles,Needles))
        found = 0
        start = timeit.default_timer()
        for n in needles:
            if n in haystack:
                found += 1
        end = timeit.default_timer()
        t = end - start
        return t

def runtime_process(Haystack, Needles, mode):
    import time

    if mode == 'set':
        haystack = set(Haystack)
        needles = set(Needles)

        start = time.process_time()
        found = len(needles & haystack)
        end = time.process_time()
        t = end - start
        return t

    elif mode == 'list':
        found = 0
        haystack = list(Haystack)
        needles = list(Needles)
        start = time.process_time()

        for needle in needles:
            if needle in haystack:
                found += 1

        end = time.process_time()
        t = end - start
        return t

    elif mode == 'dict':
        haystack = Haystack
        needles = dict(zip(Needles,Needles))
        found = 0
        start = time.process_time()
        for n in needles.keys():
            if n in haystack.keys():
                found += 1
        end = time.process_time()
        t = end - start
        return t

a = runtime(Haystack, Needles, mode='set')
print('Runtime for set :', a)
b = runtime(Haystack, Needles, mode='list')
print('Runtime for list :', b)
c = runtime(Haystack, Needles, mode='dict')
print('Runtime for dict :', c)

a = runtime_process(Haystack, Needles, mode='set')
print('Runtime_process for set :', a)
b = runtime_process(Haystack, Needles, mode='list')
print('Runtime_process for list :', b)
c = runtime_process(Haystack, Needles, mode='dict')
print('Runtime_process for dict :', c)
print('Recommend use timeit() not time.process_time()')

print('='*50)
DIAL_CODES = ((86,'China'),
                (91,'India'),
                (1, 'US'),
                (62,'Indonesia'),
                (55,'Brazil'),
                (92,'Pakistan'),
                (880, 'Bangladesh'),
                (234, 'Nigeria'),
                (7, 'Russia'),
                (81, 'Japan'))
d1 = dict(DIAL_CODES)
d2 = dict(sorted(DIAL_CODES))
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
assert d1 == d2 and d2 == d3

import sys
haystack_memory1 = set(Haystack)
needles_memory1 = set(Needles)
haystack_memory2 = list(Haystack)
needles_memory2 = list(Needles)
haystack_memory3 = dict(zip(Haystack_key,Haystack_value))
needles_memory3 = dict(zip(Needles, Needles))
print('The size of set haystack :', sys.getsizeof(haystack_memory1))
print('The size of list haystack :', sys.getsizeof(haystack_memory2))
print('The size of dict haystack :', sys.getsizeof(haystack_memory3))
print('The size of set needles :', sys.getsizeof(needles_memory1))
print('The size of list needles :', sys.getsizeof(needles_memory2))
print('The size of dict needles :', sys.getsizeof(needles_memory3))