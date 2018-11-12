#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" class의 다양한 기능을 사용하는 예

    우리는 tensorflow_probability library를 사용하여 \
    Gamma distribution에서 sampling을 수행한다.
    
    We refer below code
    https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/Gaussian_Process_Latent_Variable_Model.ipynb
    
    pages 355-359; 한글 기준
"""

import numpy as np
import matplotlib.pyplot as plt
import reprlib

import tensorflow as tf
from tensorflow_probability import distributions as tfd
from tensorflow_probability import positive_semidefinite_kernels as tfk


class Probability_box(object):
    
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
                bytes(self._observation))
    
    def __str__(self):
        return "Function of this class is to get uniform sampling :)"
    
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
    
    amplitude = np.finfo(np.float64).eps + tf.nn.softplus(
            tf.get_variable(name='amplitude',
                            dtype=tf.float64,
                            initializer=np.float64(1.)))

    length_scale = np.finfo(np.float64).eps + tf.nn.softplus(
            tf.get_variable(name='length_scale',
                            dtype=tf.float64, 
                            initializer=np.float64(1.)))

    observation_noise_variance = np.finfo(np.float64).eps + tf.nn.softplus(
            tf.get_variable(name='observation_noise_variance',
                            dtype=tf.float64, 
                            initializer=np.float64(1.)))

    observations_ = small_x_train.reshape(N, -1).transpose()

    init_ = np.random.normal(size=(N, 2))
    latent_index_points = tf.get_variable(
            name='latent_index_points',
            dtype=tf.float64,
            initializer=init_)
    
    kernel = tfk.ExponentiatedQuadratic(amplitude, length_scale)
    kernel_ = Probability_box(100, 10, amplitude, length_scale).kernel  # some errors...!

    gp_= tfd.GaussianProcess(
            kernel=kernel_,
            index_points=latent_index_points,
            observation_noise_variance=observation_noise_variance)

    log_probs = gp_.log_prob(observations_, name='log_prob')

    loss = -tf.reduce_mean(log_probs)
    optimizer = tf.train.AdamOptimizer(learning_rate=.1)
    train_op = optimizer.minimize(loss)
    
    # Initialize variables and train!
    sess.run(tf.global_variables_initializer())
    num_iters = 100
    log_interval = 20
    lips_ = np.zeros((num_iters, N, 2), np.float64)
    for i in range(num_iters):
        _, loss_, lips_[i] = sess.run([train_op, loss, latent_index_points])
        if i % log_interval == 0 or i + 1 == num_iters:
            print("Loss at step %d: %f" % (i, loss_))