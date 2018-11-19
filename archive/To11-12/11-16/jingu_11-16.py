#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 16/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        try using another abstract class from collections
"""
# 꼭 구현해야하는 abstractmethods 알아보기
# In[]: collections.MutableSet.__abstractmethods__
# Out[]: frozenset({'__contains__', '__iter__', '__len__', 'add', 'discard'})

# MutableSet이란?
# class MutableSet(Set)
#  |  A mutable set is a finite, iterable container.
#  |
#  |  This class provides concrete generic implementations of all
#  |  methods except for __contains__, __iter__, __len__,
#  |  add(), and discard().
#  |
#  |  To override the comparisons (presumably for speed, as the
#  |  semantics are fixed), all you have to do is redefine __le__ and
#  |  then the other operations will automatically follow suit.
#  |

import collections
class DeepLearningStudy(collections.MutableSet):
    def __init__(self, memberList):
        self._members = set(member for member in memberList)
        print(self._members)

    def __contains__(self, item):
        if item in self._members:
            return True
        else:
            return False

    def __iter__(self):
        yield from self._members

    def __len__(self):
        return len(self._members)

    def add(self, value):
        self._members.add(value)

    def discard(self, value):
        self._members.discard(value)

a = DeepLearningStudy('a b c'.split())

print('a' in a)
print('2' in a)
for i in a:
    print(i)


class PythonStudy(collections.Set):
    def __init__(self, memberList):
        self._members = set(member for member in memberList)
        print(self._members)

    def __contains__(self, item):
        if item in self._members:
            return True
        else:
            return False

    def __iter__(self):
        yield from self._members

    def __len__(self):
        return len(self._members)
    #
    # def add(self, value):
    #     self._members.add(value)
    #
    # def discard(self, value):
    #     self._members.discard(value)
    #
    # it is possible to not implementing these two because it inherits only collections.Set
    # implementing it is also possible of course
    
b = PythonStudy('진구 대하 승현 성빈 상홍 지윤 근회'.split())
# b.add('hi')
print(b._members)

