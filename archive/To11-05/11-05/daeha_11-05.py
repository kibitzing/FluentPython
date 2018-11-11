#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" .format()을 사용하는 tensorflow example
    pip install tensorflow-gpu==1.11.0
    pip install tensorflow-probability==0.4.0
"""

import tensorflow as tf
import numpy as np
import tensorflow_probability as tfp
import matplotlib.pyplot as plt
import seaborn as sns

tfd = tfp.distributions
tf.enable_eager_execution()


class Uniform_mean(object):
    
    def __init__(self):
        self.num_components = 10
        self.var_dim = 1
    
    def __str__(self):
        return "Function of this class is to get uniform sampling :)"
    
    def __repr__(self):
        component_mean = tfd.Uniform().sample([self.num_components, self.var_dim])
        return str(component_mean)
    
    def sample(self):
        component_mean = tfd.Uniform().sample([self.num_components, self.var_dim])
        return component_mean


print("{0!s} {0!r}".format(Uniform_mean()))  #TODO(): `format`을 사용하는 부분

sample_mean = Uniform_mean().sample()
plt.plot(np.array(sample_mean[:]))  # plots different figure everytime.
                                    # because random sampling.