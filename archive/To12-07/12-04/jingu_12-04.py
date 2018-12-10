#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 04/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION:
        Implement __imul__
        
"""
import abc
import random
import numbers

class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """iterable 항목들을 추가한다"""

    @abc.abstractmethod
    def pick(self):
        """
        무작위로 항목을 하나 반환, 동시에 제거
        객체가 비어있으면 LookupError 발생
        :return:
        """

    def loaded(self):
        """최소 한 개의 항목이 있으면 True, or False"""
        return bool(self.inspect())

    def inspect(self):
        """현재 안에 있는 항목들로 구성된 정렬된 튜플을 반환한다"""
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
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()

        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))

        self.load(other_iterable)
        return self

    def __imul__(self, other):
        if isinstance(other, numbers.Real):
            self.__init__([i * other for i in self.inspect()])
        else:
            NotImplemented
        return self
vowels = 'AEIOU'
globe = AddableBingoCage(vowels)
print(len(globe.inspect()))
print(globe.inspect())
print(globe.pick() in vowels)

print(len(globe.inspect()))

globe2 = AddableBingoCage('XYZ')
globe3 = globe+globe2
print(len(globe2.inspect())) # 3

globe_orig = globe
print(len(globe.inspect())) # 4
globe += globe2 # 4 + 3
print(len(globe.inspect())) # 7
globe += ['M', "n"]
print(len(globe.inspect())) # 9
print(globe is globe_orig) # True

print(globe.inspect()) # ('A', 'E', 'M', 'O', 'U', 'X', 'Y', 'Z', 'n')
globe *= 4
print(globe.inspect()) # ('AAAA', 'EEEE', 'MMMM', 'OOOO', 'UUUU', 'XXXX', 'YYYY', 'ZZZZ', 'nnnn')
print(globe is globe_orig) # True
