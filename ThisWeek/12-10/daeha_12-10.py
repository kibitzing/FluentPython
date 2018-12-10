#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Generator function example

"""
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for word in self.words:
            yield word
            
        return 


sentence = Sentence('KDH and KJG')
it = iter(sentence)  # <generator object Sentence.__iter__ at 0x113fd0a40>

next(it)  # 'KDH'
next(it)  # 'and'
next(it)  # 'KJG'
next(it)  # StopIteration

list(it)  # []
list(iter(sentence))  # ['KDH', 'and', 'KJG']