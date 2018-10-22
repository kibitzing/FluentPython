"""
created by Jingu Kang on 2018-10-15
coding: utf-8
"""

import tensorflow as tf
from inspect import signature

tf_Variable = tf.Variable
tf_constant = tf.constant
tf_sess = tf.Session

tf_reduce_sum = tf.reduce_sum
tf_matmul = tf.matmul

sig_V = signature(tf_Variable)
sig_C = signature(tf_constant)
sig_s = signature(tf_sess)
sig_r = signature(tf_reduce_sum)
sig_m = signature(tf_matmul)

print(sig_V)
print(sig_C)
print(sig_s)
print(sig_r)
print(sig_m)

#initial_value=None, trainable=True, collections=None, validate_shape=True, caching_device=None, name=None, variable_def=None, dtype=None, expected_shape=None, import_scope=None, constraint=None)
#(value, dtype=None, shape=None, name='Const', verify_shape=False)
#(target='', graph=None, config=None)
#(input_tensor, axis=None, keepdims=None, name=None, reduction_indices=None, keep_dims=None)
#(a, b, transpose_a=False, transpose_b=False, adjoint_a=False, adjoint_b=False, a_is_sparse=False, b_is_sparse=False, name=None)

# print(tf_Variable.__annotations__) # error
# print(tf_constant.__annotations__) # error
# print(tf_sess.__annotations__) # error
print(tf_reduce_sum.__annotations__) # {}
print(tf_matmul.__annotations__) # {}

#print(tf_Variable.__defaults__) # error
#print(tf_constant.__defaults__) # error
#print(tf_sess.__defaults__) # error
print(tf_reduce_sum.__defaults__) # None
print(tf_matmul.__defaults__) # (False, False, False, False, False, False, None)

#print(tf_Variable.__code__) # error
#print(tf_constant.__code__) # error
#print(tf_sess.__code__) # error
print(tf_reduce_sum.__code__.co_varnames) # 'args', 'kwargs', 'invalid_args', 'named_args', 'arg_name', 'spec')
print(tf_matmul.__code__.co_varnames) # ('a', 'b', 'transpose_a', 'transpose_b', 'adjoint_a', 'adjoint_b', 'a_is_sparse', 'b_is_sparse', 'name', 'a_shape', 'b_shape', 'use_sparse_matmul', 'sparse_matmul_types', 'ret')
print(tf_reduce_sum.__code__.co_argcount) # 0
print(tf_matmul.__code__.co_argcount) # 9
