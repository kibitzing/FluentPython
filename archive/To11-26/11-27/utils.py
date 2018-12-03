#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 여러 가지 함수를 가지고 있는 util 파일
    
    This code is based on below link
    https://github.com/tylersco/adapted_deep_embeddings
    
    pages 451~455; 한글 기준
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import numpy as np
import tensorflow as tf

def _stride(s):
    return [1, s, s, 1]


def _max_pooling(name, x, kernel_size, stride, padding='SAME'):
    return tf.nn.max_pool(x, ksize=_stride(kernel_size), strides=_stride(stride),
                          padding=padding, name=name)
    
    
def _conv(name, x, filter_size, in_size, out_size, stride, padding='SAME',
          bias=True, reuse=None, weight_decay=None):
    
    with tf.variable_scope(name, reuse=reuse):
        weights = tf.get_variable(
                'conv_weights', [filter_size, filter_size, in_size, out_size],
                tf.float32, initializer=tf.initializers.random_normal())
        
        res = tf.nn.conv2d(x, weights, _stride(stride), padding=padding)
        
        if bias:
            biases = tf.get_variable(
                    'conv_biases', [out_size], tf.float32,
                    initializer=tf.initializers.zeros())
            res += biases
            
        if weight_decay:
            wd = tf.nn.l2_loss(weights) * weight_decay
            tf.add_to_collection('weight_decay', wd)
            
    return res


def _fully_connected(name, x, out_size, reuse=None, weight_decay=None):
    
    with tf.variable_scope(name, reuse=reuse):
        weights = tf.get_variable(
                'fc_weights', [x.get_shape()[1], out_size], tf.float32,
                initializer=tf.initializers.random_normal())
        
        biases = tf.get_variable(
                'fc_biases', [out_size], tf.float32, initializer=tf.initializers.zeros())
        
        if weight_decay:
            wd = tf.nn.l2_loss(weights) * weight_decay
            tf.add_to_collection('weight_decay', wd)
            
        return tf.nn.xw_plus_b(x, weights, biases)