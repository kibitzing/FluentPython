#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    큐(queue)를 활용하여 텐서플로 모델의 결과값을 저장하고 3D plot 하는 예제
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import matplotlib.pyplot as plt
import numpy as np
from collections import deque

tf.set_random_seed(1234)

# Hyper Parameters
BATCH_SIZE = 64
LR = 0.002         # learning rate
N_TEST_IMG = 5

# Mnist digits
mnist = input_data.read_data_sets('./mnist', one_hot=False)     # use not one-hotted target data
test_x = mnist.test.images[:200]
test_y = mnist.test.labels[:200]

# plot one example
print(mnist.train.images.shape)     # (55000, 28 * 28)
print(mnist.train.labels.shape)     # (55000, 10)

plt.imshow(mnist.train.images[12].reshape((28, 28)), cmap='gray')
plt.title('%i' % np.argmax(mnist.train.labels[1]))
plt.show()

# tf placeholder
tf_x = tf.placeholder(tf.float32, [None, 28*28])    # value in the range of (0, 1)

act_fn_list = [tf.nn.tanh, 
               tf.nn.relu,
               tf.nn.softplus,
               tf.nn.sigmoid,
               tf.nn.relu6
               ]
act_fn_list.__delitem__(4)  # erase tf.nn.relu6
act_fn_list.__setitem__(2, tf.nn.relu6)  # convert `tf.nn.softplust` to `tf.nn.relu6`

# encoder
en0 = tf.layers.dense(tf_x, 128, tf.nn.tanh)
en1 = tf.layers.dense(en0, 64, act_fn_list.__getitem__(0))
en2 = tf.layers.dense(en1, 32, act_fn_list.__getitem__(0))
encoded = tf.layers.dense(en2, 3)

# decoder
de0 = tf.layers.dense(encoded, 12, act_fn_list.__getitem__(0))
de1 = tf.layers.dense(de0, 64, act_fn_list.__getitem__(0))
de2 = tf.layers.dense(de1, 128, act_fn_list.__getitem__(0))
decoded = tf.layers.dense(de2, 28*28, act_fn_list.__getitem__(3))

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


encoded_info = sess.run(encoded, {tf_x: view_data})
encoded_dq = deque(encoded_info, maxlen=5)

# visualize in 3D plot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
view_data = test_x[:100]
encoded_data = sess.run(encoded, {tf_x: view_data})

fig = plt.figure(0)
ax = Axes3D(fig)
X = np.zeros(shape=(100,))
Y = np.zeros(shape=(100,))
Z = np.zeros(shape=(100,))

encoded_dq = deque(encoded_data, maxlen=100)
for i in range(len(encoded_dq)):
    X[i], Y[i], Z[i] = encoded_dq.popleft()

#X, Y, Z = encoded_data[:, 0], encoded_data[:, 1], encoded_data[:, 2]
for x, y, z, s in zip(X, Y, Z, test_y):
    c = cm.rainbow(int(255*s/9))
    ax.text(x, y, z, s, backgroundcolor=c)
ax.set_xlim(X.min(), X.max())
ax.set_ylim(Y.min(), Y.max())
ax.set_zlim(Z.min(), Z.max())
plt.show()
