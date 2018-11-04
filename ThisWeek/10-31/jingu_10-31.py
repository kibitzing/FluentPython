#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 31/10/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        weakref.finalize 를 사용하여(파이썬 소멸자인듯) 메모리에서 언제 해제되는지 본다.
        주소값에 직접 접근하여 값이 사라지는지도 한번 본다. 사라지지는 않는다. 참조만 끊어질 뿐.
"""

import weakref
import ctypes

s1 = {1,2,3}
s2 = s1
adr = id(s1)

def bye():
    print('Callback function is called, 객체 소멸!')

def getValueFromId(id):
    return ctypes.cast(adr, ctypes.py_object).value

ender = weakref.finalize(s1, bye)

s5 = {1,2}
s4 = s5

print('ender.alive:', ender.alive) # alive
del s1

print('deleted s1')
print('ender.alive:', ender.alive) # alive

print('\nid of s1:', adr)
print('id of s2: {}\n'.format(id(s2)))
print('read from the memory', getValueFromId(adr))

s2 = 'spam'
print('ender.alive:', ender.alive)
# Callback function is called, 객체 소멸!
# ender.alive: False

print('\nid of s2:',id(s2))
print('id of s2 changed\n')
print('read from the memory:', getValueFromId(adr)) # still there
print('tuple (1,2,3) is not completely deleted from disk, it is still there.')

