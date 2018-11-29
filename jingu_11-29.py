#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 29/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        
"""
import numpy as np
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (np.sqrt(np.square(self.x) + np.square(self.y)))


    def __neg__(self):
        return (-self.x, -self.y)

    def __pos__(self):
        return (+self.x, +self.y)

    def __str__(self):
        return(str((self.x, self.y)))

    
a = Vector(1,2)
b = Vector(-1,3)
c = Vector(-4,-2)

print(a,b,c)

d = abs(a)
e = +c
f = -a
print(d,e,f)

