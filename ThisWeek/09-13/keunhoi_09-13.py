#!/usr/bin/env python3
# -*- coding: utf-8 -*-

t = (1,2,(3,4,5, [30,40]))
try:
    t[2][3] += [50, 60]
except TypeError as e:
    print('There is TypeError, and t is ', t)
else:
    print('There is no error and t is', t)

print("="*50)

import dis
dis.dis('s[a] += b')

print("="*50)

sports = ['soccer', 'basketball', 'baseball', 'swimming', 'golf']
dis.dis('sorted((sports))')
print("="*50)
dis.dis('sports.sort()')
