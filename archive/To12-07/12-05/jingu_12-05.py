#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 05/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        Simple modificaion of example to see how it works
        __iter__ 이 구현되어 있으면 __getitem__이 설자리가 오직 subscription?할 때만이지만
        __iter__이 없으면 그 자리까지 __getitem__이 차지할 수 있다.
        근데 __iter__ 이 없으면 isinstance(o, abc.Iterable) 했을 때 단호하게 False라고 한다 ㅠ
"""

import re
import reprlib

RE_WORD = re.compile('\w+')

class Plurals:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item] + 's'

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Plural words(%s)' % reprlib.repr(['four ' + word + 's' for word in self.words])

    # def __iter__(self):
    #     yield from ['two ' + word + 's' for word in self.words]

singulars = "cat dog student ball cup"
plurals = Plurals(singulars)

print(plurals)
# Plural words(['four cats', 'four dogs', 'four students', 'four balls', 'four cups'])

for plural_word in plurals:
    print(plural_word)
# two cats
# two dogs
# two students
# two balls
# two cups

print(list(plurals))
# ['two cats', 'two dogs', 'two students', 'two balls', 'two cups']

print(plurals[0])
# cats

from collections import abc
print(isinstance(plurals, abc.Iterable)) # True, but False when no __iter__ is implemented
