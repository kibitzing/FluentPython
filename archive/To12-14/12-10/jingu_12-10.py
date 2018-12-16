#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 10/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        generator 연습

"""

import random


x_database = [3 * i for i in range(100)]
y_database = [random.random() > 0.5 for i in range(100)]

def batch_generator(database, label, batch_size):
    for start_idx in range(int(len(database)/batch_size)):
        start_idx *= batch_size
        yield database[start_idx:start_idx+batch_size], label[start_idx:start_idx+batch_size]


for j in batch_generator(x_database, y_database, 5):
    print(j)

print('#################################')

genFac = (i for i in batch_generator(x_database, y_database, 3))

for i in genFac:
    print(i)
