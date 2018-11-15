#!/usr/bin/envs python3
# -*- coding: utf-8 -*-

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_11-14_Fluent_Python
@Author Sanghong.Kim
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
from array import array
import math

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                 bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]

import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


class FrenchDeckSelf:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card
        return self._cards[position]

def set_card(deck, position, card):
    deck._cards[position] = card

def set_repr(deck):
    fmt = 'Cards in deck : {}'
    return fmt.format(deck._cards)

@clock
def main(args):
    print("Add Your Code Below")
    v1 = Vector2d(3,4)
    print(v1)
    f = Foo()
    print(f[1])
    from random import shuffle
    l = list(range(10))
    shuffle(l)
    print(l)
    deck = FrenchDeck()
    # monkey patching 으로 구현
    FrenchDeck.__setitem__ = set_card
    shuffle(deck)
    print(deck[:5])
    # __setitem__ 으로 구현
    deck2 = FrenchDeckSelf()
    shuffle(deck2)
    print(deck2[:5])
    # 특정 class에 원하는 method 가 없을 때 monkey patching을 사용하면 매우 유용할 것으로 보인다.
    FrenchDeck.__repr__ = set_repr
    print(deck)


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
