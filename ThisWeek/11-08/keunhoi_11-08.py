#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p275-279
# ex ~10-3
'''

'''

from array import array
import reprlib
import math
import collections

class Vector:
	typecode = 'd'

	def __init__(self, components):
		self._components = array(self.typecode, components)

	def __iter__(self):
		return iter(self._components)

	def __repr__(self):
		components = reprlib.repr(self._components)
		components = components[components.find('['):-1]
		return 'Vector({})'.format(components)

	def __str__(self):
		return str(tuple(self))

	def __bytes__(self):
		return (bytes([ord(self.typecode)]) +
				bytes(self._components))

	def __eq__(self, other):
		return tuple(self) == tuple(other)

	def __abs__(self):
		return math.sqrt(sum(x * x for x in self))

	def __bool__(self):
		return bool(abs(self))

	@classmethod
	def frombytes(cls, octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:].cast(typecode))
		return cls(memv)

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
	ranks = [str(n) for n in range(2,11)] + list('JQKA')
	suits = 'spades diamonds clubs heart',split()

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits
					   					for rank in self.ranks]

	def __len__(self): # 반복 지원시 not necessary.
		return len(self._cards)

	def __getitem__(self, position): # 반복 지원시 필요
		return self._cards[position]

