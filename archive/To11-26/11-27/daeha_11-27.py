#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 실제 tensorflow library를 사용하여 다중 상속을 구현하는 예제
    (본 예제는 아직 작성중이며, 실행 code는 존재하지 않음)
    
    This code is based on below link
    https://github.com/tylersco/adapted_deep_embeddings
    
    pages 451~455; 한글 기준
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc, os
import tensorflow as tf

from utils import _conv, _max_pooling, _fully_connected

ABC = abc.ABCMeta('ABC', (object,), {})

PS_OPS = [
        'Variable', 'VariableV2', 'AutoReloadVariable', 'MutableHashTable',
        'MutablehashTableOfTensors', 'MutableDensehashTable'
        ]

def get_available_gpus():
    from tensorflow.python.client import device_lib
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']


def assign_to_device(device, ps_device):
    
    def _assign(op):
        node_def = op if isinstance(op, tf.NodeDef) else op.node_def
        if node_def.op in PS_OPS:
            return ps_device
        else:
            return device
    return _assign


class AttrDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setattr__
    
    
class Model(ABC):
    
    def __init__(self):
        super().__init__()
        
    def get_config(self, config):
        c = AttrDict()
        for k, v in config.items():
            c[k] = v
        return c
        
    @abc.abstractclassmethod
    def prediction(self): pass

    @abc.abstractclassmethod
    def optimize(self): pass


class BasicModel(Model):
    
    def __init__(self):
        self.saver = None
        self.learning_rate = 0.001
        #self.is_train = tf.placeholder(tf.bool)
        #self.is_task1 = tf.placeholder(tf.bool)
        
    def create_saver(self):
        self.saver = tf.train.Saver(tf.global_variables(), max_to_keep=1)
    
    def optimize(self):
        with tf.device('/cpu:0'):
            pred = self.prediction
            
            cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
                                        logits=pred, 
                                        labels=tf.one_hot(self.target, 10)))
            optimizer = tf.train.AdamOptimizer(learning_rate=self.learning_rate)
            
            update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
            with tf.control_dependencies(update_ops):
                train_op = optimizer.minimize(cost)
                
        return train_op, cost
    
    def metrics(self):
        d = self.get_single_device()
        with tf.device(assign_to_device(d, self.config.controller)):
            pred = self.prediction
            acc, update_acc = tf.metrics.accuracy(self.target, tf.argmax(tf.nn.softmax(pred), axis=1))
            return update_acc
        
        
class BasicMNIST(BasicModel):
    
    def __init__(self):
        super().__init__()
        self.input = tf.placeholder(tf.float32, [None, 784])
        self.target = tf.placeholder(tf.int64, [None])
        self.prediction
        self.optimize
        self.metrics
        
    def prediction(self):
        #d = self.get_single_device()
        with tf.device('/cpu:0'):
            x = self.input
            x = tf.reshape(x, [-1, 28, 28, 1])
            x = tf.nn.relu(_conv('conv1', x, 3, x.get_shape()[-1], 32, 1))
            x = _max_pooling('pool2', tf.nn.relu(_conv('conv2', x, 3, x.get_shape()[-1], 32, 1)), 2, 2)
            x = tf.contrib.layers.flatten(x)
            x = tf.nn.relu(_fully_connected('fc1', x, 128))
            x = _fully_connected('fc2', x, self.config.n)
            return x
    
if __name__ == "__main__":
    
    import numpy as np
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.astype(np.float32)/255.
    x_train = np.reshape(x_train, [60000, -1])
    x_test = x_test.astype(np.float32)/255.
    x_test = np.reshape(x_test, [10000, -1])
    
    tf.reset_default_graph()
    config = tf.ConfigProto(allow_soft_placement=True)
    with tf.Session(config=config) as sess:
        
        model = BasicMNIST()
        
        init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
        sess.run(init)
        for i in range(0, len(y_train), 32):  #TODO(): error
            x_train_mb, y_train_mb = x_train[i:i+32], y_train[i:i+32]
            sess.run(model.optimize, feed_dict={model.input: x_train_mb,
                                                model.target: y_train_mb,})
                                                #model.is_task1: True,
                                                #model.is_train: True,
                                                #model.learning_rate: 0.001})
    