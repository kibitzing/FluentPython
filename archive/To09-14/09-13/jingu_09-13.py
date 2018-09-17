#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by Jingu Kang on 2018/09/13
"""

#### 
## 간단한 batch 짜기
####
import random

x = [i for i in range(100)]

def batch_suffle(x, batch_size):
    random.shuffle(x)
    return x[:batch_size]


for i in range(5):
    a = batch_suffle(x, 10)
    print(a)
#
#l = [1,2,3]
#print(id(l))
#
#l *= 2
#print(id(l))
#print(l)
#
#t = (1,2,3)
#print(id(t))
#t *= 2
#print(t)
#print(id(t))
## id changed
#
##t = (1,2, [30, 40])
##t[2] = [50, 60]
##print(t)
### t # (1,2,[30,40,50,60])   뭐야 안된다며!
#
#fruits = ['grape' , 'raspberry', 'apple', 'banana']
#print(sorted(fruits))
#print(fruits)
#fruits.sort()
#print(fruits)
#
#print(sorted(fruits, reverse=True, key=len))
#print(fruits)
#
#print(sorted(fruits, reverse=False, key=str.lower))
#print(fruits)
#