#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 실제 tensorflow library를 사용하여 다중 상속을 구현하는 예제
    (본 예제는 아직 작성중이며, 실행 code는 존재하지 않음)
    
    This code is based on below link
    https://github.com/tylersco/adapted_deep_embeddings
    
    pages 451~455; 한글 기준
"""


import abc, os
import tensorflow as tf

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
    
    def __init__(self, config):
        self.config = self.get_config(config)
        self.saver = None
        self.learning_rate = tf.placeholder(tf.float32)
        self.is_train = tf.placeholder(tf.bool)
        self.is_task1 = tf.placeholder(tf.bool)
        
    def create_saver(self):
        self.saver = tf.train.Saver(tf.global_variables(), max_to_keep=1)
        
    def save_model(self, sess, step):
        self.saver.save(sess, os.path.join(self.config.save_dir_by_rep, 'model.cktp'), 
                        global_step=step)
        
    def get_single_device(self):
        devices = get_available_gpus()
        d = self.config.controller
        if devices:
            d = devices[0]
        return d
    
    def optimize(self):
        d = self.get_single_device()
        with tf.device(assign_to_device(d, self.config.controller)):
            pred = self.prediction
            
            cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
                                        logits=pred, 
                                        labels=tf.one_hot(self.target, self.config.n)))
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
        
        
class MNISTModel(BasicModel):
    pass  # Tomorrow :)
    