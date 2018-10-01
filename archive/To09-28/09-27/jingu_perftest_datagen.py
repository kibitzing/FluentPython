#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:49:05 2018

@author: jingu
"""

import random 
import array

MAX_EXPONENT = 7
HAYSTACK_LEN = 10 ** MAX_EXPONENT
NEEDLES_LEN = 10 ** (MAX_EXPONENT - 1)
SAMPLE_LEN = HAYSTACK_LEN + NEEDLES_LEN // 2

needles = array.array('d')

sample = {1/random.random() for i in range(SAMPLE_LEN)}

print('initial sample: %d elements' % len(sample))

while len(sample) < SAMPLE_LEN:
    sample.add(1/random.random())
    
print('complete sample: %d elements' % len(sample))

sample = array.array('d', sample)
random.shuffle(sample)

not_selected = sample[:NEEDLES_LEN // 2]
print('not selected: %d samples' % len(not_selected))
print(' writing not_selected.arr')

with open('not_selected.arr', 'wb') as fp:
    not_selected.tofile(fp)
    
selected = sample[NEEDLES_LEN //2 :]
print('selected: %d samples' % len(selected))
print(' writing selected.arr')
with open('selected.arr','wb') as fp:
    selected.tofile(fp)