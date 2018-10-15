#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    map(), filter(), reduce()를 사용하는 keras 예제
"""

import keras
print('keras version is', keras.__version__)

import keras.backend as K

def pow_tensor(tensor):
    return K.pow(tensor, 2)

K.get_session()  # It runs like tf.Session()

group_a = list(map(pow_tensor, filter(lambda n: n % 2, range(10))))

print(K.get_value(group_a[0]))  # 1
print(K.get_value(group_a[1]))  # 9
print(K.get_value(group_a[4]))  # 81


group_b = [pow_tensor(n) for n in range(10) if n % 5]

print(K.get_value(group_b[0]))  # 1
print(K.get_value(group_b[5]))  # 49
print(K.get_value(group_b[7]))  # 81

