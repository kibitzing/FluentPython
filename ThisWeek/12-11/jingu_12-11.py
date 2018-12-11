#!/anaconda3/envs/tensorflow/bin/python
# -*- coding: utf-8 -*-
"""
    Created by Jingu Kang on 11/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION:
        When to use Generate function?
        How to use more effieciently with itertools?

"""


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


ap = ArithmeticProgression(0, 1, 4)
print(list(ap))

ap2 = aritprog_gen(0, 1, 4)
print(list(ap2))

import itertools

gen = itertools.count(0, 1)
gen_list = []
i = 0
while i < 4:
    gen_list.append(next(gen))
    i += 1
print(gen_list)

gen2 = itertools.takewhile(lambda n: n < 4, itertools.count(0, 1))
print(list(gen2))
