#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 22/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        collections.UserDict를 사용한간단한 상속 개념 연습
"""

import collections
class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key,[value] * 2)

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd1 = DoppelDict(one = 1)
dd2 = DoppelDict2(one = 1)

print(dd1) # {'one': 1}
print(dd2) # {'one': [1, 1]}


class AnswerDict(dict):
    def __getitem__(self, item):
        return 42
class AnswerDict2(collections.UserDict):
    def __getitem__(self, item):
        return 42


ad =AnswerDict(a = 'foo')
ad2 =AnswerDict2(a = 'foo')

print( ad['a']) # 42
print( ad2['a']) # 42

print(ad) # {'a': 'foo'}
print(ad2) # {'a': 'foo'}

d1 = {}
d2 = {}
d3 = collections.UserDict()

d1.update(ad)
d2.update(ad2)
d3.update(ad)

print(d2) # {'a': 42}
print(d1) # {'a': 'foo'}
print(d3) # {'a': 42}

# UserDict를 상속 받거나, UserDict object로 만들거나.
