#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    namedtuple을 사용하는 예제
"""

import tensorflow as tf
from keras import backend as K

from collections import namedtuple

sess = tf.Session()

devices = sess.list_devices()
for d in devices:
    print(d.name)  # /job:localhost/replica:0/task:0/device:CPU:0 (MacOS)

tensor1 = tf.constant([1, 2, 3, 4, 5])

Tensor = namedtuple('Tensor', 'velocity weight bias')

# tf version
t1 = Tensor(float(1.24), tf.constant([[1,1],[1,2]]), tf.constant([[1,2],[2,1]]))
sess.run(t1.weight)
sess.run(t1.bias)

# keras version
t2 = Tensor._make([K.abs(2.0), K.abs(-1.0), K.abs(1.1)])

# keras tensor can apply both sess.run() ans K.get_value
sess.run(t2.weight)  # 1.0
sess.run(t2.bias)    # 1.1

K.get_value(t2.weight)  # 1.0
K.get_value(t2.bias)    # 1.1

print(t2._asdict())  # namedtuple()의 인스턴스(객체)를 OrderedDict로 변환해 주는 함수

t2 = t2._replace(weight=K.ones(shape=(2,2)))

K.get_value(t2.weight)  # array([[1., 1.],
                        #        [1., 1.]], dtype=float32)
                        
print(t2._fields)  # ('velocity', 'weight', 'bias')

#  * -- end code -- * 