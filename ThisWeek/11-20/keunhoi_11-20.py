#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p327-331
# Example 11-10 ~ 13
'''


'''

import abc
import random

class Tombola(abc.ABC):

	@abc.abstractmethod # abstractmethod 와 def 사이에는 어느것도 올 수 없다.
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

class BingoCage(Tombola):

	def __init__(self, items):
		self._randomizer = random.SystemRandom()
		self._items = []
		self.load(items)

	def load(self, items):
		self._items.extend(items)
		self._randomizer.shuffle(self._items)

	def pick(self):
		try:
			return self._items.pop()
		except IndexError:
			raise LookupError('pick from empty BingoCage')

	def __call__(self):
		self.pick()

class LotteryBlower(Tombola):

	def __init__(self, iterable):
		self._balls = list(iterable)

	def load(self, iterable):
		self._balls.extend(iterable)

	def pick(self):
		try:
			position = random.randrange(len(self._balls))
		except ValueError:
			raise LookupError('pick from empty BingoCage')
		return self._balls.pop(position)

	@property
	def loaded(self):
		return bool(self._balls)

	def inspect(self):
		return tuple(sorted(self._balls))


def main():

	print('='*50)
	B = BingoCage
	print(B(range(100)).pick())

	print('=' * 50)
	L = LotteryBlower
	print(L(range(1,46)).pick())

	print('=' * 50)
	print(B([]).loaded(), L([]).loaded)

if __name__ == '__main__':
	main()
