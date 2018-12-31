#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 27/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        yield, yield from, send, next 총 복습
"""

def sayHello():
    a = 1
    print('a',a)
    yield a
    a = 2
    print('a',a)
    yield a
    a=3
    print('a',a)
    yield a

b = sayHello()
c = next(b)
print('c',c)
c = next(b)
print('c',c)
c = next(b)
print('c',c)

def sayHi():
    a = 1
    print('a',a)
    a = yield a
    print('a',a)
    a = yield a
    print('a',a)
    a = yield a

b = sayHi()
print(b)
c = next(b)
print('c',c)
c = b.send(11)
print('c',c)
c = b.send(22)
print('c',c)

print('say bye')
def sayBye():
    a = [1,22,333]
    print('a',a)
    yield from a
    a = 2
    print('a',a)
    yield a
    a=3
    print('a',a)
    yield a

b = sayBye()
c = next(b)
print('c',c)
c = next(b)
print('c',c)
c = next(b)
print('c',c)
c = next(b)
print('c',c)
c = next(b)
print('c',c)
