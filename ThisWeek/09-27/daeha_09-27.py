#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    types python 내장 라이브러리 내부의
    MappingProxyType를 사용하여 손쉽게 tensorflow layer의 속성을 불러오는 예제
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import matplotlib.pyplot as plt
import numpy as np

tf.set_random_seed(1234)

# Hyper Parameters
BATCH_SIZE = 64
LR = 0.002         # learning rate
N_TEST_IMG = 5

# Mnist digits
mnist = input_data.read_data_sets('/Users/daehakim/Desktop/Programming/tensorflow/', one_hot=False)     # use not one-hotted target data
test_x = mnist.test.images[:200]
test_y = mnist.test.labels[:200]

# plot one example
print(mnist.train.images.shape)     # (55000, 28 * 28)
print(mnist.train.labels.shape)     # (55000, 10)

plt.imshow(mnist.train.images[12].reshape((28, 28)), cmap='gray')
plt.title('%i' % np.argmax(mnist.train.labels[1]))
plt.show()

l = set([tf.placeholder(tf.float32, [None, 28*28])])  #TODO():

# tf placeholder
tf_x = l.pop()  #same as `tf_x = tf.placeholder(tf.float32, [None, 28*28])`


from types import MappingProxyType
act_fn_dict = {1: [tf.nn.tanh], 
               2: [tf.nn.relu],
               3: [tf.nn.softplus],
               4: [tf.nn.sigmoid],
               5: [tf.nn.relu6]
               }
act_fn_proxy = MappingProxyType(act_fn_dict)

# encoder (align taps because of better looking)
en0 = tf.layers.dense(tf_x, 128, act_fn_proxy[1][0])
en1 = tf.layers.dense(en0,  64,  act_fn_proxy[1][0])
en2 = tf.layers.dense(en1,  32,  act_fn_proxy[1][0])
encoded = tf.layers.dense(en2, 3)

# decoder (align taps because of better looking)
de0 = tf.layers.dense(encoded, 12,    act_fn_proxy[1][0])
de1 = tf.layers.dense(de0,     64,    act_fn_proxy[1][0])
de2 = tf.layers.dense(de1,     128,   act_fn_proxy[1][0])
decoded = tf.layers.dense(de2, 28*28, act_fn_proxy[4][0])

loss = tf.losses.mean_squared_error(labels=tf_x, predictions=decoded)
train = tf.train.AdamOptimizer(LR).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# initialize figure
f, a = plt.subplots(2, N_TEST_IMG, figsize=(5, 2))
plt.ion()

print('Initial recon. results')
view_data = mnist.test.images[:N_TEST_IMG]
decoded_data = sess.run(decoded, {tf_x: view_data})
import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(121)
plt.imshow(np.reshape(view_data[0], (28, 28)), cmap='gray')

plt.subplot(122)
plt.imshow(np.reshape(decoded_data[0], (28, 28)), cmap='gray')
plt.show()

for step in range(10000):
    b_x, b_y = mnist.train.next_batch(BATCH_SIZE)
    _, encoded_, decoded_, loss_ = sess.run([train, encoded, decoded, loss], {tf_x: b_x})
    
    if step % 1000 == 0:
        print('step is ', step)

print('Trained recon. results')
decoded_data = sess.run(decoded, {tf_x: view_data})
plt.figure(1)
plt.subplot(121)
plt.imshow(np.reshape(view_data[0], (28, 28)), cmap='gray')

plt.subplot(122)
plt.imshow(np.reshape(decoded_data[0], (28, 28)), cmap='gray')
plt.show()
