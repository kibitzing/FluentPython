#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    tensorflow keras에서 layer shape을 내장함수를 쓰지 않고 확인하는 예제
"""

import keras
print('keras version is:', keras.__version__)  # 2.2.0

classes = 2  # binary

def output_shape(inbound_nodes):
    all_output_shapes = set(
            [str(node.output_shapes) for node in inbound_nodes])
    if len(all_output_shapes) == 1:
        output_shapes = inbound_nodes[0].output_shapes
        if len(output_shapes) == 1:
            return output_shapes[0]
        else:
            return output_shapes
        
# simple keras model
input = keras.layers.Input(shape=(32, 32, 3))
l0 = keras.layers.Dense(10, activation='relu')(input)
l1 = keras.layers.Dense(20, activation='relu')(l0)
l2 = keras.layers.Dense(20, activation='relu')(l1)
l3 = keras.layers.Dense(classes, activation='sigmoid')(l2)
model = keras.models.Model(input, l3)

inbound_nodes = model._inbound_nodes

# check model's output shape
layer_shape = output_shape(inbound_nodes)

print(layer_shape)

assert layer_shape[3] == classes

