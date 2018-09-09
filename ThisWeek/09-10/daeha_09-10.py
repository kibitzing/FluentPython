#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    언패킹(unpacking)을 사용하여 텐서를 확인하는 예제
"""

import tensorflow as tf

sess = tf.Session()

devices = sess.list_devices()
for d in devices:
    print(d.name)  # /job:localhost/replica:0/task:0/device:CPU:0 (MacOS)

tensor1 = tf.constant([1, 2, 3, 4, 5])

val1, *vals = [tensor1[k] for k in range(tensor1.get_shape().as_list()[0])]  # unpacking
print('value is {}'.format(sess.run(val1)))
print('value is {}'.format(sess.run(vals)))

val1, val2, val3, *vals = [tensor1[k] for k in range(tensor1.get_shape().as_list()[0])]  # unpacking
print('value is {} / type is {}'.format(sess.run(val1), type(sess.run(val1))))
print('value is {} / type is {}'.format(sess.run(val2), type(sess.run(val2))))
print('value is {} / type is {}'.format(sess.run(val3), type(sess.run(val3))))
print('value is {} / type is {}'.format(sess.run(vals), type(sess.run(vals))))
sess.close()
