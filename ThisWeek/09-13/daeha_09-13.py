#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    bisect 라이브러리를 이용해서 최적화 알고리즘 수행 도중 tensor의 값의 범위를 확인
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

import bisect

tf.set_random_seed(1)

# Hyper Parameters
BATCH_SIZE = 64
LR = 0.002         # learning rate
N_TEST_IMG = 5

def partition(score, breakpoints=[0, 100, 10000], grades='LMH'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

# Mnist digits
mnist = input_data.read_data_sets('./mnist', one_hot=False)     # use not one-hotted target data
test_x = mnist.test.images[:200]
test_y = mnist.test.labels[:200]

# plot one example
print(mnist.train.images.shape)     # (55000, 28 * 28)
print(mnist.train.labels.shape)     # (55000, 10)
plt.imshow(mnist.train.images[0].reshape((28, 28)), cmap='gray')
plt.title('%i' % np.argmax(mnist.train.labels[0]))
plt.show()

# tf placeholder
tf_x = tf.placeholder(tf.float32, [None, 28*28])    # value in the range of (0, 1)

# encoder
en0 = tf.layers.dense(tf_x, 128, tf.nn.tanh)
en1 = tf.layers.dense(en0, 64, tf.nn.tanh)
en2 = tf.layers.dense(en1, 12, tf.nn.tanh)
encoded = tf.layers.dense(en2, 3)

# decoder
de0 = tf.layers.dense(encoded, 12, tf.nn.tanh)
de1 = tf.layers.dense(de0, 64, tf.nn.tanh)
de2 = tf.layers.dense(de1, 128, tf.nn.tanh)
decoded = tf.layers.dense(de2, 28*28, tf.nn.sigmoid)

# TODO(): on the purpose of testing bisect library
grade = tf.reduce_sum(decoded, keep_dims=False)

loss = tf.losses.mean_squared_error(labels=tf_x, predictions=decoded)
train = tf.train.AdamOptimizer(LR).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# initialize figure
f, a = plt.subplots(2, N_TEST_IMG, figsize=(5, 2))
plt.ion()

view_data = mnist.test.images[:N_TEST_IMG]
for i in range(N_TEST_IMG):
    a[0][i].imshow(np.reshape(view_data[i], (28, 28)), cmap='gray')
    a[0][i].set_xticks(()); a[0][i].set_yticks(())

for step in range(8000):
    b_x, b_y = mnist.train.next_batch(BATCH_SIZE)
    _, encoded_, decoded_, loss_ = sess.run([train, encoded, decoded, loss], {tf_x: b_x})
    
    if step % 1000 == 0:
        grade_ = sess.run([grade], {tf_x: b_x})
        print('complexity of decoded img is ', partition(grade_[0]))
    if step % 100 == 0:     # plotting
        print('train loss: %.4f' % loss_)
        decoded_data = sess.run(decoded, {tf_x: view_data})
        for i in range(N_TEST_IMG):
            a[1][i].clear()
            a[1][i].imshow(np.reshape(decoded_data[i], (28, 28)), cmap='gray')
            a[1][i].set_xticks(()); a[1][i].set_yticks(())
        plt.draw(); plt.pause(0.01)
plt.ioff()
