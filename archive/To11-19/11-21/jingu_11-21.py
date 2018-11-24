#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 21/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        @register
        abc
"""

# abc.MutableSequence.__abstractmethods__
# Out[9]: frozenset({'__delitem__', '__getitem__', '__len__', '__setitem__', 'insert'})
from collections import abc
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

@abc.MutableSequence.register
class MutSeq1:
    def __init__(self):
        pass
    # def __delitem__(self, key):
    #     pass
    # def __getitem__(self, item):
    #     pass
    # def __len__(self):
    #     pass
    def __setitem__(self, key, value):
        pass
    def insert(self):
        pass

class MutSeq2(abc.MutableSequence):
    def __init__(self):
        pass
    def __delitem__(self, key):
        pass
    def __getitem__(self, item):
        pass
    def __len__(self):
        pass
    def __setitem__(self, key, value):
        pass
    def insert(self):
        pass

class MutSeq3():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)

ms1 = MutSeq1()
ms2 = MutSeq2()
ms3 = MutSeq3()
print(issubclass(MutSeq1, abc.MutableSequence)) #True
print(issubclass(MutSeq2, abc.MutableSequence)) #True
print(issubclass(MutSeq3, abc.MutableSequence)) #False

print(isinstance(ms1, abc.MutableSequence)) #True
print(isinstance(ms2, abc.MutableSequence)) #True
print(isinstance(ms3, abc.MutableSequence)) #False


## __abstractmethods__ 를 모두 구현하지 않아도 등록(register 했으면 섭클래스로 인식
## 등록 안했어도 상속했으면 섭클래스로 인식
## __abstractmethods__ 모두 구현했어도 상속 안 하고 등록 안했으면 섭클래스로 인식 안함..?
## 오리처럼 걷는데.. 왜?!
