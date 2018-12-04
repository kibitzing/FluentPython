# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:29:59 2018

@author: jiyun
"""
import itertools
import random
import abc


class Tombola(abc.ABC):
    
    @abc.abstractmethod
    def load(self, iterable):
        """
        """
    
    @abc.abstractmethod
    def pick(self): # 객체가 비어있을 때 실행하면 LookupError
        """
        """
    
    def loaded(self):
        return bool(self.inspect())
    
    def inspect(self):
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
                msg = "right operand in += must be {!r} or an interable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self
    

vowels = ''
globe = AddableBingoCage(vowels)
print(globe.inspect()) # ()
#print(globe.pick() in vowels) # LookupError
vowels = 'AEIOU'
globe = AddableBingoCage(vowels)
print(globe.pick() in vowels) #True
globe2 = AddableBingoCage('PYTHON')
globe3 = globe + globe2
print(len(globe3.inspect())) # 10

"""
+= 연산자 사용
"""

globe_orig = globe
print(len(globe.inspect()))
globe += globe2
print(len(globe.inspect()))
globe += ['W','Y']
print(len(globe.inspect()))

print(globe is globe_orig) #True : globe는 globe_orig 참조 중
#globe += 1 # 비 반복형이므로 TypeError  




