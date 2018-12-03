#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 30/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        elementwise multiplication,
        scalr division 구현
"""

import numpy as np
import itertools
import numbers
class Vector:
    def __init__(self, component_list):
        self.component = component_list

    def __iter__(self):
        return iter(self.component)


    # def __add__(self, other):
    #     pairs = itertools.zip_longest(self, other, fillvalue=0.0)
    #     return Vector(a+b for a,b in pairs)

    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector([i+j for i,j in pairs])

    #elementwise mul
    def __mul__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector([i*j for i,j in pairs])

    #sclar division
    def __truediv__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector([i/scalar for i in self.component])
        else:
            return NotImplemented

    def __str__(self):
        return str(self.component)

v1 =Vector([1,2,3])
v2 =Vector([1,2])
print(v1)
v3 = v1+v2
print(v3)
v4 = v1*v1
v5 = v1/2
print(v4) #[1, 4, 9]
print(v5) #[0.5, 1.0, 1.5]



