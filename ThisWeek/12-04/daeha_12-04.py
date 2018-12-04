#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 파이썬 중위 연산자 @를 사용하는 예제
    
    pages 479~484; 한글 기준
"""
import numpy as np
import tensorflow as tf

with tf.device("/cpu:0"):
    a = tf.Variable(tf.random_normal([10, 10], stddev=0.35))
    b = tf.Variable(tf.zeros([10, 20]))
c = a @ b  #TODO(): @ means dot_product operation
    
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    sess.run(c)
    print('c is {}'.format(c))