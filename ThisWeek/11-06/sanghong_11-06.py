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
2018_11-06_Fluent_Python
@Author Sanghong.Kim
__slot__ 사용시 메모리 사용량이 감소
gpu를 사용해도 먹는가 궁금 -> 당연히 먹겠지?
오늘거는 코드가 별로 없어서... 블랙잭 게임을 만들었다.
Ace를 1 or 11로 사용하는 것은 아직 구현 못했다.
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import math
from array import array
from datetime import datetime
import collections
from random import choice

class Vector2d:
    __slots__ = ('__x', '__y')
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
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.x, self.y)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        componets = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*componets)

    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamond clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

class BlackJackDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamond clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks
                       for suit in self.suits]*6

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        if self._cards[position][0] == 'J' or self._cards[position][0] == 'Q' or  self._cards[position][0] == 'K':
            value = 10
        elif self._cards[position][0] == 'A':
            value = 11
        else:
            value = self._cards[position][0]
        return str(value)


class BlackJackGame:
    deck = BlackJackDeck()
    def __init__(self, hand):
        self.hand = hand

    def dealer(self):
        print("Delar have :", self.hand)
        self.hit()
        if self.hand == 21:
            return 'bj'
        if self.hand > 21:
            print("Dealer Busted")
            exit(0)
        return self.hand

    def player(self):
        self.hit()
        if self.hand == 21:
            return 'bj'
        else:
            self.question()
        return self.hand

    def blackjack(self):
        self.hit()
        if self.hand == 21:
            return 'bj'
        return 'nbj'

    def question(self):
        print("Your Hand :", self.hand)
        dummy = input("Do you want to [H]it, [D]ouble, or [S]tand: ").lower()
        if dummy == "h":
            print("Your Choice is Hit")
            self.hit()
            if self.hand > 21:
                print("Busted, You Lose")
                sys.exit(0)
            self.question()
        elif dummy == "d":
            print("Your Choice is Double")
            self.hit()
        else:
            print("Your Choice is Stand")

    def hit(self):
        self.hand = int(self.hand) + int(choice(self.deck))


    def __getitem__(self):
        print(self.hand)
        return self.hand

class flow:
    def __init__(self, dealer, player):
        self.dealer = dealer
        self.player = player


    def check(self):
        while self.dealer <= 17:
            self.dealer = str(self.dealer)
            self.dealer = BlackJackGame(self.dealer)
            self.dealer = self.dealer.dealer()
            self.dealer = int(self.dealer)
        if self.dealer <= 21 and self.player <= 21 and self.dealer > self.player:
            print("Dealer Have : {}, You Have : {}".format(self.dealer,self.player))
            print("You Lose")
            return 0
        elif self.dealer <= 21 and self.player <= 21 and self.dealer == self.player:
            print("Dealer Have : {}, You Have : {}".format(self.dealer, self.player))
            print("Draw")
            return 0
        elif self.dealer <= 21 and self.player <= 21 and self.dealer < self.player:
            print("Dealer Have : {}, You Have : {}".format(self.dealer, self.player))
            print("You Win!")
            return 0


def main(args):
    print("Add Your Code Below")
    deck = BlackJackDeck()
    dealer = BlackJackGame(choice(deck))
    player = BlackJackGame(choice(deck))
    a = dealer.dealer()
    if a == 'bj':
        b = player.blackjack()
        if b == 'bj':
            print("Draw")
        else:
            print("Dealer Have Black Jack")
    else:
        b = player.player()
        print("Last Card Sum :", b)
        if b == 'bj':
            print("Black Jack!")
        else:
            game = flow(a,b)
            game.check()

# Arguments Settings
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
