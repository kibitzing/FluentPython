#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    텐서플로 텐서를 list comprehension으로 확인하는 방법
"""

import tensorflow as tf

sess = tf.Session()

devices = sess.list_devices()
for d in devices:
    print(d.name)  # /job:localhost/replica:0/task:0/device:CPU:0 (MacOS)

tensor1 = tf.constant([1, 2, 3, 4, 5])

vals = [tensor1[k] for k in range(tensor1.get_shape().as_list()[0])]
print('value is {}'.format(sess.run(vals[0])))
print('value is {}'.format(sess.run(vals[1])))
print('value is {}'.format(sess.run(vals[2])))
print('value is {}'.format(sess.run(vals[3])))
print('value is {}'.format(sess.run(vals[4])))
sess.close()
