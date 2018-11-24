#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p322-326
# ~ Example 11-9
'''
예제를 제대로 실행해보기 위해선 자식 클라스를 작성하는 수밖에 없었다고 한다...
'''

import abc
import random

class Tombola(abc.ABC):

	@abc.abstractmethod
	def load(self, iterable):
		"""iterable의 항목들을 추가한다."""

	@abc.abstractmethod
	def pick(self):
		"""무작위로 항목을 하나 제거하고 반환한다.
		객체가 비어 있을 때 이 매세드를 실행하면 'LookupError가 발생한다.
		"""

	def loaded(self):
		"""최소 한 개의 항목이 있으면 True를, 아니면 False를 반환한다."""
		return bool(self.inspect())

	def inspect(self):
		"""현재 안에 있는 항목들로 구성된 정렬된 튜플을 반환한다."""
		items = []
		while True:
			try:
				items.append(self.pick())
			except LookupError:
				break
		self.load(items)
		return tuple(sorted(items))

class Tombola_2(Tombola):

	def __init__(self, l=[]):
		self.l = l

	def load(self, iterable):
		self.l += list(iterable)
		print(self.l)

	def pick(self):
		if len(self.l) != 0:
			k = random.randrange(len(self.l))
			r = self.l[k]
			del self.l[k]
			print('Picked number is :', r)
			return r
		else:
			print('Not allowed to pick a number from zero length list.')
			return None


T2 = Tombola_2
T2().pick()
T2().load([3,4,5,6])
print(T2().l)
T2().pick()

