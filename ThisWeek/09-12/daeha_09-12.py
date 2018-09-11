#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    slicing을 사용하는 예제
"""

import tensorflow as tf
from keras import backend as K

state = tf.Variable(0, name="counter")

one = tf.constant(1)
new_value  = tf.add(state, one)
added_value = tf.assign(state, new_value)
final_value = tf.multiply(new_value, added_value)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:

    devices = sess.list_devices()
    for d in devices:
        print(d.name)  # /job:localhost/replica:0/task:0/device:CPU:0 (MacOS)
    
    sess.run(init_op)
    for _ in range(5):
        sess.run(added_value)
        a = sess.run([state, new_value, final_value])
        
        a_list = list(a)  # convert tuple to list
        print('all: ', a_list[:])
        print('reversed: ', a_list[::-1])
        print('reversed with 2 space: ', a_list[::-2])
        print('reversed with 3 space: ', a_list[::-3])
        print('\n')
        
sess.close()

#  * -- end code -- * 