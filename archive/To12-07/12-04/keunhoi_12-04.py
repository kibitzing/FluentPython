#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p393~ch13end
# Example 13-18~19

'''
    ch13 마무리
'''

import abc
import numpy as np
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


class AddableBingoCage(BingoCage):

    def __add__(self, other):
        if isinstance(other, AddableBingoCage):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, AddableBingoCage):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable."
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self


if __name__ == '__main__':
    print("{0:=^20}".format("Example 13-18"))
    vowels = 'AEIOU'
    globe = AddableBingoCage(vowels)
    print(globe.inspect())
    print(globe.pick() in vowels)
    print(len(globe.inspect()))

    globe2 = AddableBingoCage('XYZ')
    globe3 = globe + globe2
    print(globe3.inspect())
    print(type(globe3.inspect()))
    print(len(globe3.inspect()))

    globe_orig = globe
    print(len(globe_orig.inspect()))
    globe += globe2
    print(len(globe.inspect()))
    globe += ['M', 'N']
    print(len(globe.inspect()))
    print(globe is globe_orig)

    # 부가로 이번 챕터에서 알게 된 @ 연산자 테스트
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[1, 2], [3, 4], [5, 6]])
    result1 = a @ b
    result2 = np.matmul(a,b)
    print(result1 == result2)




