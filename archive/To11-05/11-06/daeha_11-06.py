#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" class에서 property 속성을 사용하는 예제

    우리는 tensorflow_probability library를 사용하여 \
    Gamma distribution에서 sampling을 수행한다.
"""

import tensorflow as tf
import numpy as np
import tensorflow_probability as tfp
import matplotlib.pyplot as plt
import seaborn as sns

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


print("{0!s} {0!r}".format(Gamma_mean(10, 1)))

sample_mean = Gamma_mean(100, 5).sample()
plt.plot(np.array(sample_mean[:]))  # plots different figure everytime.
                                    # because random sampling.