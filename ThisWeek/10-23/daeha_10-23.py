#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

""" python global variable을 다루는 예제
"""

global x
x = "global variable"

def test1():
    global x
    y = "local variable"
    print(x, y)
    x = "changed variable"
    
test1()  # global variable local variable


def test2():
    #global x
    y = "local variable"
    print(x, y)
    x = "changed variable"
    
test2()  # UnboundLocalError: local variable 'x' referenced before assignment