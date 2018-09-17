#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# example 2-20
from array import array
from random import  random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats[-1])
print(floats2 == floats)

floats3 = floats2.tobytes()
print(floats3 == floats2)

# =============================================
print('='*50)
# example 2-21
import sys
del sys.modules['array']
import array
numbers = array.array('h',list(range(-2,3)))
memv = memoryview(numbers)
print(len(memv))
memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5] = 4
print(numbers)

# =============================================
print('='*50)
# example 2-22
import numpy as np
a = np.arange(12)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[:,1])
print(a.transpose())

# =============================================
print('='*50)
# example 2-23
from collections import deque
dq = deque(range(10), maxlen=10)
print('dq = ', dq)
print('dq.rotate(3) = ', dq.rotate(3))
print('dq = ', dq)
print('dq.rotate(-4) = ', dq.rotate(-4))
print('dq.appendleft(-1) = ', dq.appendleft(-1))
print('dq = ', dq)
print('dq.append(-2) = ', dq.append(-2))
print('dq = ', dq)
print('dq.extend([10,11,12]) = ', dq.extend([10,11,12])
print('dq = ', dq)
print('dq.extendleft([12,11,10]) = ', dq.extendleft([12,11,10])
print('dq = ', dq)