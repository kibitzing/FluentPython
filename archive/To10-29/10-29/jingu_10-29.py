#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
"""
    Created by Jingu Kang on 29/10/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.
    
    DESCRIPTION:
    deep comprehension about 'is','==' and 'id'
    """

t1 = (1,2,[30,40])
t2 = (1,2,[30,40])
t3 = t1

print('t1==t2:' ,t1 == t2)

print('id(t1):', id(t1))
print('id(t2):', id(t2))

print('t1 is t2:',t1 is t2)

print('id(t1[-1]):',id(t1[-1]))
print('id(t3[-1]):',id(t3[-1]))
t1[-1].append(99)

print('id(t1):',id(t1))
print('id(t2):',id(t2))
print('id(t3):',id(t3))

print('t1:',t1)
print('t2:',t2)
print('t3:',t3)

print('t1==t2:',t1 == t2)
print('t1 is t2:',t1 is t2)
#
# t1==t2: True
# id(t1): 4488092264
# id(t2): 4488113680
#
# t1 is t2: False
#
# id(t1[-1]): 4507960584
# id(t3[-1]): 4507960584
#
# id(t1): 4488092264
# id(t2): 4488113680
# id(t3): 4488092264
#
# t1: (1, 2, [30, 40, 99])
# t2: (1, 2, [30, 40])
# t3: (1, 2, [30, 40, 99])
#
# t1==t2: False
# t1 is t2: False
