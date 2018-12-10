# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:18:52 2018

@author: jiyun
"""
# 원서 기준 408~412p

from abc import ABCMeta, abstractmethod
from Sentence import Sentence

s = 'ABC' # 반복형 s
it = iter(s) # 반복자 it
for char in s:
    print(char)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it # 반복자 객체 제거
        break
    

class Iterable(metaclass = ABCMeta):
    
    __slots__ = ()
    
    @abstractmethod
    def __iter__(self):
        while False:
            yield None
            
    @classmethod
    def __subclasshook__(cls,C):
        if cls is Iterable:
            if any("__iter__"in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
    
class Iterator(Iterable):
    
    __slots__ = ()
    
    @abstractmethod
    def __next__(self):
        return StopIteration
    
    def __iter__(self):
        return self
    
    @classmethod
    def __subclasshook__(cls,C):
        if cls is Iterator:
            if (any("__next__" in B.__dict__ for B in C.__mro__) and any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
            
        return NotImplemented
    
    
s3 = Sentence('Pig and Pepper')
it = iter(s3)
print(next(it))
print(next(it))
print(next(it))
#    print(next(it)) # StopItertation
print(list(it)) # []
print(list(iter(s3)))
it2 = iter(s3)
print(next(it2)) # Pig    

"""
고전적인 반복자
"""

import re
import reprlib

RE_WORD = re.compile('\w+')

    
class Sentence:
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __repr__(self):
        return 'Sentence(%s)' %reprlib.repr(self.text) # 30자로 제한 
    
    def __iter__(self): # 반복형이 됨
        return SentenceIterator(self.words)
    
class SentenceIterator:
    
    def __init__(self,words):
        self.words = words
        self.index = 0
        
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
    
    def __iter__(self):
        return self

# 예제 14-2    
s = Sentence('"The time has come," the Walrus said')
print(s) #Sentence('"The time ha...e Walrus said')

for word in s:
    print(word)

print(list(s))    

