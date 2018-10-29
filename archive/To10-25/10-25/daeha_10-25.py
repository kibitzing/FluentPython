#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Working example for my blog post at:
# https://danijar.github.io/structuring-your-tensorflow-models

""" 텐서플로 라이브러리를 이용한 데코레이터 예제
    출저: https://danijar.github.io/structuring-your-tensorflow-models
"""

import functools
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


def doublewrap(function):
    
    @functools.wraps(function)
    def decorator(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            return function(args[0])
        else:
            return lambda wrapee: function(wrapee, *args, **kwargs)
    return decorator

@doublewrap
def define_scope(function, scope=None, *args, **kwargs):
    """A decorator for functions that define Tensorflow operations."""
    
    attribute = '_cache_' + function.__name__
    name = scope or function.__name__
    
    @property
    @functools.wraps(function)
    def decorator(self):
        if not hasattr(self, attribute):
            with tf.variable_scope(name, *args, **kwargs):
                setattr(self, attribute, function(self))
        return getattr(self, attribute)
    return decorator


class Model:

    def __init__(self, image, label):
        self.image = image
        self.label = label
        self.prediction
        self.optimize
        self.error

    @define_scope(initializer=tf.contrib.slim.xavier_initializer())
    def prediction(self):
        x = self.image
        x = tf.contrib.slim.fully_connected(x, 200)
        x = tf.contrib.slim.fully_connected(x, 200)
        x = tf.contrib.slim.fully_connected(x, 10, tf.nn.softmax)
        return x

    @define_scope
    def optimize(self):
        logprob = tf.log(self.prediction + 1e-12)
        cross_entropy = -tf.reduce_sum(self.label * logprob)
        optimizer = tf.train.RMSPropOptimizer(0.03)
        return optimizer.minimize(cross_entropy)

    @define_scope
    def error(self):
        mistakes = tf.not_equal(
            tf.argmax(self.label, 1), tf.argmax(self.prediction, 1))
        return tf.reduce_mean(tf.cast(mistakes, tf.float32))


def main():
    mnist = input_data.read_data_sets('./mnist/', one_hot=True)
    
    image = tf.placeholder(tf.float32, [None, 784])
    label = tf.placeholder(tf.float32, [None, 10])
    model = Model(image, label)
    sess = tf.Session()
    sess.run(tf.initialize_all_variables())

    for _ in range(10):
      images, labels = mnist.test.images, mnist.test.labels
      error = sess.run(model.error, {image: images, label: labels})
      print('Test error {:6.2f}%'.format(100 * error))
      for _ in range(60):
        images, labels = mnist.train.next_batch(100)
        sess.run(model.optimize, {image: images, label: labels})


def _main():
    mnist = input_data.read_data_sets('./mnist/', one_hot=True)

    image = tf.placeholder(tf.float32, [None, 784])
    label = tf.placeholder(tf.float32, [None, 10])
    model = Model(image, label)

    train, test = tf.keras.datasets.mnist.load_data()
    train_x, train_y = train
    
    train_x = train_x.reshape(60000, 784)
    train_y = tf.keras.utils.to_categorical(train_y, 10)
    
    sess = tf.Session()
    sess.run(tf.initialize_all_variables())

    for _ in range(10):
      images, labels = mnist.test.images, mnist.test.labels
      error = sess.run(model.error, {image: images, label: labels})
      print('Test error {:6.2f}%'.format(100 * error))
      for _ in range(2):
        sess.run(model.optimize, {image: train_x, label: train_y})
        print("Training...")


if __name__ == '__main__':
    #main()
    _main()
        