#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Abstract class(ABC)를 사용하는 예
    
    pages 409~413; 한글 기준
"""

import numpy as np
import matplotlib.pyplot as plt
import reprlib
import numbers
import functools
import operator
import math

import tensorflow as tf
from tensorflow_probability import distributions as tfd
from tensorflow_probability import positive_semidefinite_kernels as tfk


from abc import ABCMeta, ABC, abstractmethod

class Sub_prob_box(ABC):  #TODO(): add abstract class
    
    @abstractmethod
    def sample(self):
        """Sample uniform distribution."""

    @abstractmethod
    def kernel(self):
        """Define the kernel."""


class Probability_box_upgrade(Sub_prob_box):
    
    def __init__(self, num_components, var_dim, amplitude, length_scale):
        self._num_components = num_components
        self._var_dim = var_dim
        self._amplitude = amplitude
        self._length_scale = length_scale

    @property
    def num_components(self): return self._num_components
    
    @property
    def var_dim(self): return self._var_dim
    
    @property
    def amplitue(self): return self._amplitude
    
    @property
    def length_scale(self): return self._length_scale
    
    def __bytes__(self):
        return (bytes(self._num_components) + 
                bytes(self._var_dim) + 
                bytes(self._amplitude) + 
                bytes(self._length_scale))
        
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))
        
    def __eq__(self, other):
        if len(self) != len(other):
            return False+"Hello, your wrong"
        for a, b, in zip(self, other):
            if a != b:
                return False
        return True
    
    def __hash__(self):
        hashes = (hash(x) for x in self._num_components)
        return functools.reduce(operator.xor, hashes, 0)
   
    def __len__(self):
        return len(self._num_components)

    """
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._num_components[index])
        elif isinstance(index, numbers.Integral):
            return self._num_components[index]
        else:
            msg = '{cls.__name__} indices must be integers :)'
            raise TypeError(msg.format(cls=cls))
    """
    
    def __getitem__(self, var_dim):
        return range(0, 30, 10)[var_dim]
    
    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)
    
    def __repr__(self):
        components = reprlib.repr(self._num_components)
        components = components[components.find('['):-1]+']'
        return 'Probability_box_upgrade({},{},{},{})'.format(components, self._var_dim,
                                       self._amplitude, self._length_scale)
    
    def sample(self):
        component_mean = tfd.Uniform().sample([self._length_scale, self._var_dim])
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
    
    prob_box1 = Probability_box_upgrade(([1,2,3]),100,1,1)
    for i in prob_box1: print(i)  # 0\ 10\ 20