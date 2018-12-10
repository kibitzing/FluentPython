#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 07/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION:
        Iterator 와 Iterable을 구별해야 하는 이유 line by line으로 설명
"""

from collections import abc
import re
import reprlib

RE_WORD = re.compile('\w+')

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        self.index = 0

    def __getitem__(self, item):
        return self.words[item]

    def __iter__(self):
        return self
        # for word in self.words:
        #     yield word
        # return

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word
    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
a = Sentence('hi hello bye')

for ab in a: # (1)
    for b in a:
        print('b in b:',b) # (2)
        print('ab in ab:', ab) # (3)
"""
## 결과물 ##
(1) 에서 a[0]인 을 ab가 채감
b in b: hello  # 그래서 (2)에서 hi가 아닌 hello가 출력됨.
ab in ab: hi # (3)에서는 ab가 채간 hello가 출력됨 
b in b: bye # 그다음인 bye가 나오고
ab in ab: hi
# 원래 더 반복 돼야하지만 : 9번 3X3X2
bye 까지 나와서 더 return될 게 없으므로 종료.
이걸 Iterator와 Iterable 구별해서 돌리면.
#########################################################
b in b: hi
ab in ab: hi
b in b: hello
ab in ab: hi
b in b: bye
ab in ab: hi
b in b: hi
ab in ab: hello
b in b: hello
ab in ab: hello
b in b: bye
ab in ab: hello
b in b: hi
ab in ab: bye
b in b: hello
ab in ab: bye
b in b: bye
ab in ab: bye
"""

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        self.index = 0

    def __getitem__(self, item):
        return self.words[item]

    def __iter__(self):
        # return self
        for word in self.words:
            yield word
        return

    # def __next__(self):
    #     try:
    #         word = self.words[self.index]
    #     except IndexError:
    #         raise StopIteration
    #     self.index += 1
    #     return word
    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
a = Sentence('hi hello bye')
print('#########################################################')
for ab in a: # (1)
    for b in a:
        print('b in b:',b) # (2)
        print('ab in ab:', ab) # (3)
