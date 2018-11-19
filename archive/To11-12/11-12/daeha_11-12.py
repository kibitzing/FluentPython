#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" class의 다양한 기능을 사용하는 예

    우리는 tensorflow_probability library를 사용하여 \
    Probability_box class를 하나 만들어서 다양하게 다루도록 한다.
    
    pages 361-365; 한글 기준
"""

import numpy as np
import matplotlib.pyplot as plt
import reprlib
import numbers

import tensorflow as tf
from tensorflow_probability import distributions as tfd
from tensorflow_probability import positive_semidefinite_kernels as tfk
    
    
class Probability_box_upgrade(object):
    
    def __init__(self, num_components, var_dim,
                 amplitude, length_scale):
        self._num_components = num_components
        self._var_dim = var_dim
        self._amplitude = amplitude
        self._length_scale = length_scale

    @property
    def num_components(self):
        return self._num_components
    
    @property
    def var_dim(self):
        return self._var_dim
    
    def __bytes__(self):
        return (bytes(self._num_components) + 
                bytes(self._var_dim) + 
                bytes(self._amplitude) + 
                bytes(self._length_scale))
    
    def __str__(self):
        return "Function of this class is to get uniform sampling :)"
            
    def __len__(self):
        return len(self._num_components)
    
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._num_components[index])
        elif isinstance(index, numbers.Integer):
            return self._num_components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))
    
    def __repr__(self):
        component_mean = reprlib.repr(tfd.Gamma(concentration=.1,rate=.001).sample([self.num_components, self.var_dim]))
        return str(component_mean)
    
    def sample(self):
        component_mean = tfd.Uniform().sample([self.num_components, self.var_dim])
        return component_mean
    
    def kernel(self):
        kernel = tfk.ExponentiatedQuadratic(self._amplitude, self._length_scale)
        return kernel


if __name__ == "__main__":
    
    def reset_session():
        """Creates a new global, interactive session in Graph-mode."""
        global sess
        try:
            tf.reset_default_graph()
            sess.close()
        except:
            pass
        sess = tf.InteractiveSession()

    reset_session()
    
    # Load the MNIST data set and isolate a subset of it.
    (x_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data()
    N = 100
    small_x_train = x_train[:N, ...].astype(np.float64) / 256.
    small_y_train = y_train[:N]
    
    prob_box_up = Probability_box_upgrade(([1,2,3,4,5,6,7]),1,1,1)
    print(len(prob_box_up._num_components))  # 7
    print(prob_box_up._num_components[1:4])  # [2,3,4]
    prob_box_up._num_components.__getitem__(1)  # 2
