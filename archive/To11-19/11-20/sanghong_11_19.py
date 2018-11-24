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
2018_11-19_Fluent_Python
@Author Sanghong.Kim
16일에 못 본 내용과 오늘 내용을 추가하여 올립니다.
책 내용을 보아 개념은 알겠으나 abc module 에 대한 이해가 더 필요할 것 같다.
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import abc
import random

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

class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """iterable의 항목들을 추가한다."""

    @abc.abstractmethod
    def pick(self):
        """무작위로 항목을 하나 제거하고 반환한다.
        객체가 비어 있을 때 이 메서드를 실행하면 'LookupError'가 발생한다.
        """

    def loaded(self):
        """최소 한개의 항목이 있으면 True를, 아니면 False를 반환한다."""
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

    def __init__(self,iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))

@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

@clock
def main(args):
    print("Add Your Code Below")
    t = BingoCage(range(500))
    print(t.pick())
    l = LotteryBlower(range(500))
    print(l.pick())
    t1 = TomboList(range(500))
    print(isinstance(t1, Tombola))

# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
