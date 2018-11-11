# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:34:42 2018

@author: jiyun
"""
# 원서 기준 277~281

import math
from array import array
import reprlib

class Vector:
   
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components) #벡터 요소 배열로 저장
    
    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components) #제한된 길이로 표현하기 위함, array 'd' 노출하지 않기 위함
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._cmoponents))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))
   
    def __bool__(self):
        return bool(abs(self))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv) # '*'로 언패킹 할 필요 없음, 바로 생성자에 전달

print(Vector([3.1,4.2]))
print(Vector(range(5)))


"""
프로토콜과 덕 타이핑
"""

import collections

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
        

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]  # 파이썬 시퀀스 프로토콜이 동반하는 메서드
        



  