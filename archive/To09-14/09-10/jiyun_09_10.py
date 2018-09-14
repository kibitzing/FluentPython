# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:25:02 2018

@author: jiyun
"""

colors = ['Red','Orange','Yellow']
sizes = ['1', '2']
tshirts = [(color,size) for color in colors for size in sizes]
for color in colors:
    for size in sizes:
        
        
        print((color, size))
for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)


import os
_, filename = os.path.split('C:/Users/Desktop/iamge.raw')
filepath = os.path.dirname('C:/Users/Desktop/iamge.raw')
print(filename) #iamge.raw
print(filepath) #C:/Users/Desktop


symbols = "@*&$#"
symbol = tuple(ord(symbol) for symbol in symbols)
print(symbol) #(64, 42, 38, 36, 35)
import array
symbol = array.array('I', (ord(symbol) for symbol in symbols))
print(symbol) #array('I', [64, 42, 38, 36, 35])


traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
John, Tom, Mari = traveler_ids
country, _ = John
print(John, country) #('USA', '31195855') USA
John, Tom, Mari = Tom, John, Mari
print(John, country) #('BRA', 'CE342567') USA


def sum(a,b):
    s = a+b
    return s
x = (4,5)
print(sum(*x)) #9

