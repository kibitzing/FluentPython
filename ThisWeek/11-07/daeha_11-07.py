#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" class에서 __slots__를 사용하여 공간을 절약하는 예제

    우리는 tensorflow_probability library를 사용하여 \
    Gamma distribution에서 sampling을 수행한다.
    
    pages 343-347
"""

import tensorflow as tf
import numpy as np
import tensorflow_probability as tfp
import matplotlib.pyplot as plt

tfd = tfp.distributions
tf.enable_eager_execution()


class Gamma_mean(object):
    
    def __init__(self, num_components, var_dim):
        self.__num_components = int(num_components)
        self.__var_dim = int(var_dim)
        
    @property  #TODO():
    def num_components(self):
        return self.__num_components
    
    @property
    def var_dim(self):
        return self.__var_dim
    
    def __str__(self):
        return "Function of this class is to get uniform sampling :)"
    
    def __repr__(self):
        component_mean = tfd.Gamma(concentration=.1,rate=.001).sample([self.num_components, self.var_dim])
        return str(component_mean)
    
    def sample(self):
        component_mean = tfd.Uniform().sample([self.num_components, self.var_dim])
        return component_mean
    
    
class Gamma_mean_slot(object):

    __slots__ = ('__num_components', '__var_dim')  #TODO():
    
    def __init__(self, num_components, var_dim):
        self.__num_components = int(num_components)
        self.__var_dim = int(var_dim)

    @property
    def num_components(self):
        return self.__num_components
    
    @property
    def var_dim(self):
        return self.__var_dim
    
    def __str__(self):
        return "Function of this class is to get uniform sampling :)"
    
    def __repr__(self):
        component_mean = tfd.Gamma(concentration=.1,rate=.001).sample([self.num_components, self.var_dim])
        return str(component_mean)
    
    def sample(self):
        component_mean = tfd.Uniform().sample([self.num_components, self.var_dim])
        return component_mean

# from https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python/450034
import sys
from numbers import Number
from collections import Set, Mapping, deque

try: # Python 2
    zero_depth_bases = (basestring, Number, xrange, bytearray)
    iteritems = 'iteritems'
except NameError: # Python 3
    zero_depth_bases = (str, bytes, Number, range, bytearray)
    iteritems = 'items'

def getsize(obj_0):
    """Recursively iterate to sum size of object & members."""
    _seen_ids = set()
    def inner(obj):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size = sys.getsizeof(obj)
        if isinstance(obj, zero_depth_bases):
            pass # bypass remaining control flow and return
        elif isinstance(obj, (tuple, list, Set, deque)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, Mapping) or hasattr(obj, iteritems):
            size += sum(inner(k) + inner(v) for k, v in getattr(obj, iteritems)())
        # Check for custom object instances - may subclass above too
        if hasattr(obj, '__dict__'):
            size += inner(vars(obj))
        if hasattr(obj, '__slots__'): # can have __slots__ with __dict__
            size += sum(inner(getattr(obj, s)) for s in obj.__slots__ if hasattr(obj, s))
        return size
    return inner(obj_0)

#print("{0!s} {0!r}".format(Gamma_mean(10, 1)))

sample_mean = Gamma_mean(100, 5).sample()
plt.plot(np.array(sample_mean[:]))
getsize(Gamma_mean(100, 5))  # 369

sample_mean_slot = Gamma_mean_slot(100, 5).sample()
plt.plot(np.array(sample_mean_slot[:]))
getsize(Gamma_mean_slot(100, 5))  # 56
                                  # Wow! Size of class reduced :)
