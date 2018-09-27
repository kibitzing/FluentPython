#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

start = time.clock()
haystack1 = set(range(10000000))
needles1 = set(range(0,10000000,10000))
elapsed1 = (time.clock() - start)

start = time.clock()
haystack2 = [range(10000000)]
needles2 = [range(0,10000000,10000)]
elapsed2 = (time.clock() - start)

start = time.clock()
haystack3 = list(range(10000000))
needles3 = list(range(0,10000000,10000))
elapsed3 = (time.clock() - start)

start = time.clock()
found1 = len(needles1 & haystack1)
elapsed4 = (time.clock() - start)

start = time.clock()
found2 = len(set(needles2) & set(haystack2))
elapsed5 = (time.clock() - start)

start = time.clock()
found3 = len(set(needles3) & set(haystack3))
elapsed6 = (time.clock() - start)

start = time.clock()
found = 0
for n in needles2:
    if n in haystack2:
        found += 1
elapsed7 = (time.clock() - start)

print('elapsed1 is:', elapsed1)
print('elapsed2 is:', elapsed2)
print('elapsed3 is:', elapsed3)
print('='*50)
print('elapsed4 is:', elapsed4)
print('elapsed5 is:', elapsed5)
print('elapsed6 is:', elapsed6)
print('elapsed7 is:', elapsed7)
