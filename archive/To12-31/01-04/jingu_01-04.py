#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 04/01/2019.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        learn to use tqdm package
"""

import time
from tqdm import tqdm


# Just bar
for i in tqdm(range(1000)):
    time.sleep(0.01)

# Add name before test
for i in tqdm(range(1000),'TEST'):
    time.sleep(0.01)

# Set Max Value
for i in tqdm(range(1000),'TEST', 10000):
    time.sleep(0.01)

# Can control refresh rate
for i in tqdm(range(1000), 'TEST', 1000, True, mininterval=1):
    time.sleep(0.01)

# control format with bar_format
for i in tqdm(range(1000), 'TEST', 1000, True, mininterval=1, bar_format='{n}{r_bar}'):
    time.sleep(0.01)



