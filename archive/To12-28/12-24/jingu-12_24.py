#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 24/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        simple example using yield from 
        
"""

def gen_by_three(*iterables):
    for it in iterables:
        i = 0
        its = [it[i:i+3] for i in range(0, len(it)-3, 3)]
        yield from its
        i += 3
        if i > len(it):
            yield from it[i:-1]

str1 = 'KRWUSDCNY'
str2 = 'KORUSACHN'

gen1 = list(gen_by_three(str1, str2))
print(gen1)


def gen():
    for c in 'AB':
        yield c
    for i in range(1,3):
        yield i

a = list(gen())
print(a)

def gen_new():
    yield from 'AB'
    yield from range(1,3)

b =list(gen_new())
print(b)

def chain(*iterables):
    for it in iterables:
        yield from it

s = 'abc'
t = tuple(range(3))
c1 = chain(s,t)

print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))

c = list(chain(s,t))
print(c)
