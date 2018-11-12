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
2018_11-08_Fluent_Python
@Author Sanghong.Kim
오늘 내용 중 11월 06일에 블랙잭 게임에서 참고하였던 예제 1-1의 코드가 나왔다.
눈에 띄는 부분은 _cards와 지능형 리스트 정도가 있었고 해당 코드가 시퀀스 처럼 동작한다는 것에 대해서 잘 이해하지 못하였으나
__len__과 __getitem__ 부분에서 self._cards를 불러와서 그런 것인가 싶다.
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
from array import array
import reprlib
import math
import collections

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

Card = collections.namedtuple('Card', ['rank', 'suit'])

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

class Vector:
    typecode = 'd'

    # 전 장에서 _name으로 보호된 속성을 부여하는 것을 배웠다.
    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    # str을 정의 하였을 때는 print의 결과가 __str__이 되고 정의하지 않았을 때는 __repr__ 이 된다.
    def __str__(self):
        return 'Vector({})'.format(str(tuple(self)))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                 bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x* x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

@clock
def main(args):
    print("Add Your Code Below")

    Vector1 = Vector((3, 4, 5))
    print(Vector1)
    print(Vector((3, 4, 5)))
    print(Vector1.__repr__())
    print(Vector1.__str__())
    print(Vector1._components)
    Vector1._components = array('d', [1, 2, 7])
    print(Vector1)
    print(Vector1._components)


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
