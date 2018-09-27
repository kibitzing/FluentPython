# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 22:15:55 2018

@author: jiyun
"""


a = {2,3,4}
b = {3,5,7}
c = {3}
print(a.isdisjoint(b)) #False
print(a.__contains__(2)) #True
print(b.__gt__(c)) #True

########################################

import timeit

haystack_d = {}
needles_d = {}

haystack_s = set([])
needles_s = set([])

haystack_l = []
needles_l = []

for i in range(10000000):
    haystack_d.update({i : i})
    haystack_s.update([i])
    haystack_l.append(i)
    
for i in range(-500,500):
    needles_d.update({i:i})
    needles_s.update([i])
    needles_l.append(i)

found = 0
start = timeit.default_timer()
for n in needles_d:
    if n in haystack_d:
        found += 1
end = timeit.default_timer()
print(end- start) #6.591617608364686e-05

found = 0
start = timeit.default_timer()
for n in needles_s:
    if n in haystack_s:
        found += 1
        
end = timeit.default_timer()
print(end- start) #6.38722636381317e-05

found = 0
start = timeit.default_timer()
for n in needles_l:
    if n in haystack_l:
        found += 1    
end = timeit.default_timer()
print(end- start) #37.88397679954994
