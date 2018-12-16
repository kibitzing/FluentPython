#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Generator function example

"""
import re
import reprlib

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')
    
g1 = [x*3 for x in gen_AB()]

for i in g1:
    print('==>', i)
    
g2 = (x*3 for x in gen_AB())

for i in g2:
    print('===>', i)