#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

# initialize weights layer by layer
weights1 = np.random.rand(32,9)
weights2 = np.random.rand(64,9)
weights3 = np.random.rand(64,9)

# initialize weights by slice()
weights = np.random.rand(32*9+64*9*2)
slice1 = slice(0,32*9)
slice2 = slice(32*9,32*9 + 64*9)
slice3 = slice(32*9 + 64*9, None)

weight_1 = weights[slice1]
weight_2 = weights[slice2]
weight_3 = weights[slice3]

Weights = [weight_1, weight_2, weight_3]

layer1_weights = [['_'] * (32*9)]
layer23_weights = [['_'] * (64*9) for i in range(2)]
layer_weights = [layer1_weights[0], layer23_weights[0], layer23_weights[1]]

for i in range(len(Weights)):
    for j in range(len(Weights[i])):
        if Weights[i][j] < 0.001:
            layer_weights[i][j] = 'X'