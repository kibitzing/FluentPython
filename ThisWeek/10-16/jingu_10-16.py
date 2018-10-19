"""
created by Jingu Kang on 2018-10-16
code: utf-8
"""

import tensorflow as tf
from functools import partial

a = tf.constant([[10, 20],[15,25]])

sess = tf.Session()

sess_init = partial(sess.run, tf.global_variables_initializer())

tf_mat_mul_by_a = partial(tf.matmul, a)

b = tf.constant([[2,0],[0,2]])
c = tf_mat_mul_by_a(b)

sess_init()
# session initiated!

print(sess.run(a))
# [[10 20]
#  [15 25]]

print(sess.run(c))
# [[20 40]
#  [30 50]]
