#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" yield from을 사용하는 예제

"""
import tensorflow as tf
import numpy as np

x = np.random.sample((100,2))

dataset = tf.data.Dataset.from_tensor_slices(x)

iter = dataset.make_one_shot_iterator()
el = iter.get_next()

with tf.Session() as sess:
    print(sess.run(el))  # [0.35986122 0.1065075 ]
    
# using two numpy arrays
features, labels = (np.random.sample((100,2)), np.random.sample((100,1)))
dataset = tf.data.Dataset.from_tensor_slices((features,labels))

iter = dataset.make_one_shot_iterator()
el = iter.get_next()

with tf.Session() as sess:
    print(sess.run(el))  # (array([0.4385316, 0.8297516]), array([0.10580645]))
    


# from generator
sequence = np.array([[[1]],[[2],[3]],[[3],[4],[5]]])

def generator():
    for el in sequence:
        yield el
        
dataset = tf.data.Dataset().batch(1).from_generator(generator,
                                             output_types=tf.int64,
                                             output_shapes=(tf.TensorShape([None, 1])))

iter = dataset.make_initializable_iterator()
el = iter.get_next()

with tf.Session() as sess:
    sess.run(iter.initializer)
    print(sess.run(el))
    
    print(sess.run(el))
    print(sess.run(el))