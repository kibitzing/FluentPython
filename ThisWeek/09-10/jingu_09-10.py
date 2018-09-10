#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:52:54 2018

@author: jingu
"""

"""
symbols = '^&*!@'
tuple(ord(symbol) for symbol in symbols)
import array
array.array('I' (ord(symbol)) for symbol in symbols)
"""
import tensorflow as tf
import numpy as np
print("---from here for tuple---")
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'),('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('country: %s, passport number: %s' % passport)
        
for country, _ in traveler_ids:
    print('country: %s' % country)
    
print("\n---from here for list---")
l_traveler_ids = [['USA', '31195855'],['BRA', 'CE342567'], ['ESP', 'XDA205856']]
for passport in sorted(l_traveler_ids):
    #print('%s/%s' % passport)
    print('country: %s, passport number: %s' % (passport[0], passport[1]))
# change to list, it does not works! 
print("it does not work if not changing to print('%s/%s' % (passport[0], passport[1]))")    
for country, _ in l_traveler_ids:
    print('country: %s' %country)
print('it works for list also')
print('----tensorflow exmample----')

W = tf.Variable([[10, 20],[2,3]])
b = tf.Variable([15,4])
def layer(W, b, x):
    return tf.reduce_sum(tf.multiply(W,x), 1) + b

parameters = (W,b)
init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init)
print('result of dot product: {}'.format(sess.run(layer(*parameters,[10,20])))) #result of dot product: [515  84]
