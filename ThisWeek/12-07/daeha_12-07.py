#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" `iter` function을 공부해보는 예제
    
    pages 499~503; 한글 기준
"""
from collections import abc

import re
import reprlib

class Foo:
    def __iter__(self):
        pass
    
issubclass(Foo, abc.Iterable)  # True

f = Foo()
isinstance(f, abc.Iterable)  # True


RE_WORD = re.compile('\w+')

class Sentence:
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        return SentenceIterator(self.words)
    
    
class SentenceIterator:
    
    def __init__(self, words):
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
    
s3 = Sentence('Attack and Defence')
it = iter(s3)
it

next(it)
next(it)
next(it)

list(it)
list(iter(s3))  # ['Attack', 'and', 'Defence']
