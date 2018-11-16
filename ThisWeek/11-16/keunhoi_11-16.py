#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p317-321

'''
예제 위주로 작성
'''

import collections
from random import shuffle
from copy import deepcopy

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(collections.MutableSequence):
	ranks = [str(n) for n in range(2,11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits
					   					for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]

	def __setitem__(self, position, value):
		self._cards[position] = value

	def __delitem__(self, position):
		del self._cards[position]

	def insert(self, position, value):
		self._cards.index(position, value)

	def guessing(self):
		l1 = deepcopy(self._cards)
		l2 = deepcopy(self._cards)

		shuffle(l1)
		card_guest = self._cards[0]
		number_chance = 10

		for i in range(number_chance):
			shuffle(l2)
			if l2[0] == card_guest:
				if i == 0:
					fmt = 'Your {0}st Guess is Correct.'
				elif i == 1:
					fmt = 'Your {0}nd Guess is Correct.'
				elif i == 2:
					fmt = 'Your {0}rd Guess is Correct.'
				else:
					fmt = 'Your {0}th Guess is Correct.'
				print(fmt.format(i + 1))
				break
			else:
				if i == (number_chance - 1):
					print('All of Your Guess Fails')

FrenchDeck2().guessing()