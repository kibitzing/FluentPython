#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 파이썬 중위 연산자 @를 사용하는 예제
    
    pages 499~503; 한글 기준
"""
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
s = Sentence('"The winter is coming," the KDH said,')
print(s)  # Sentence('"The winter ...the KDH said,')
          # 실제로는 reprlib.repr()이 생성한 것

for word in s:
    print(word)
list(s)  # ['The', 'winter', 'is', 'coming', 'the', 'KDH', 'said']