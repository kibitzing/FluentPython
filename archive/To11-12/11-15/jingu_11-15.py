#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 15/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        Duck typing, 꽥꽥 거리면 오리일 것이다.!?
"""
from textwrap import wrap
import abc
field_names = '진구, 대하, 승현, 상홍, 근회, 지윤, 성빈'

print('before process:')
for member in field_names:
    print(member)

try:
    field_names = field_names.replace(',',' ').split()
except AttributeError:
    print('Attribute Error')

field_names = tuple(field_names)

print('after process:')
for member in field_names:
    print(member)

"""
멍키 패칭 예제
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


from random import shuffle

deck = FrenchDeck()


def set_card(self, position, card):
    self._cards[position] = card


FrenchDeck.__setitem__ = set_card
print(deck[:5])
shuffle(deck)
print(deck[:5])
