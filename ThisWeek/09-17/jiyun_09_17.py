# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:08:20 2018

@author: jiyun
"""
a = ['a','b','c','d']
b= ['A','B','C','D']

print(a.__iadd__(b)) #['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
print(a) #['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
print(b) #['A', 'B', 'C', 'D']
print(a.append(b)) #None
print(a) #['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D', ['A', 'B', 'C', 'D']]

print(b.index('B')) #1
print(b.__len__()) #4
print(b.reverse())# None
print(b) #['D', 'C', 'B', 'A']
print(b.sort(reverse=True)) #None
print(b) #['D', 'C', 'B', 'A']

##################################################################

import array
numbers = array.array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
memv_oct = memv.cast('B')
print(memv_oct.tolist()) #[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
print(memv_oct) #<memory at 0x000002527DEC1B88>
memv_oct[7] = 4 
print(numbers) #array('h', [-2, -1, 0, 1025, 2])

##################################################################

import numpy as np
a = np.arange(10)
print(a)
print(type(a)) #<class 'numpy.ndarray'>
print(a.shape) #(10,)
a.shape = 2,5
print(a.transpose())
#[[0 5]
# [1 6]
# [2 7]
# [3 8]
# [4 9]]
print(a)
#[[0 1 2 3 4]
# [5 6 7 8 9]]

##################################################################

import tensorflow as tf
from time import perf_counter as pc
tic = pc()
sess = tf.Session()
x = tf.constant([True, False], dtype = tf.float32)
print(sess.run(x)) #[1. 0.]
x = tf.cast(x,tf.int32)
print(sess.run(x)) #[1 0]
toc = pc()-tic
print(toc) #0.009586730491321305
