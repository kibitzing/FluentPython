#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:40:54 2018

@author: jingu
"""
"""
examples from the book
metro_areas = [
        ('Tokyo', 'JP', 36.933, ( 35.63232, 139.231323)),
        ('Delhi NCR', 'IN', 21.12213, ( 28.123124, 77.123213)),
        ('Mexico City', 'MX', 20.1423, ( 19.23123, -99.123233)),
        ('New York-Newark', 'US', 20.104, ( 40.123213, -74.123123)),
        ('Sao Paulo', 'BR', 19.649, ( -23.12323, -46.123213))
        ]

name, cc, pop, (latitude, longitude) = ('Tokyo', 'JP', 36.933, ( 35.63232, 139.231323))
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:^9.4f} | {:^9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
 
from collections import namedtuple
Country = namedtuple('City2', ["name", "country", "population", "coordinates"])
tokyo = Country('Tokyo', 'JP', 36.933, ( 35.63232, 139.231323))

"""   

from collections import namedtuple
import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float32)
# this is more popular way 
parameters = namedtuple('parameters', 'w1 b1 w2 b2')
# but it also works
activators = namedtuple('activators', ['activator1', 'activator2'])

# gives all the parameters and activators in the form of named tuple
param_fullyConnectedLayer = parameters(tf.Variable([[2.,2.],[1.,1.]]), tf.Variable([2.,1.]), tf.Variable([[3.,2.],[3.,2.]]), tf.Variable([3.,3.]))
activators_fullyConnectedLayer = activators(tf.nn.relu, tf.nn.softmax)

# Layers
L1 = tf.add(tf.matmul(param_fullyConnectedLayer.w1, x), param_fullyConnectedLayer.b1)
L1 = activators_fullyConnectedLayer.activator1(L1)

L2 = tf.add(tf.matmul(param_fullyConnectedLayer.w2, L1), param_fullyConnectedLayer.b2)
L2 = activators_fullyConnectedLayer.activator2(L2)

# initializing
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

# it works! even tf.nn.relu and tf.nn.softmax
print(sess.run(L2, feed_dict={x:[[2.,2.],[1.,1.]]}))

# activators_fullyConnectedLayer = activators_fullyConnectedLayer._replace(activator1 = tf.nn.softmax)
# print(activators_fullyConnectedLayer)