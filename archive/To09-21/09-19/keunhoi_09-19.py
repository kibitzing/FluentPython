#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 어제 혼자 공부하다가 끄적거렸는데 마침 오늘 분량 내용과 겹쳐서 첨부.
from collections import defaultdict

d = defaultdict(object)
print(d['one'])
print(d['two'])

d = defaultdict(lambda : 0)
print(d['one'])
print(d['two'])
print(d)

d = defaultdict(lambda : 0, a=1,b=2,c=3)
print(d['a'])
print(d['b'])
print(d['c'])
print(d['d'])

print('='*50)
# ==================================================================

def default_factory():
    return 1
d = defaultdict(default_factory, a=2,b=3,c=4)
print(d['a'])
print(d['b'])
print(d['c'])
print(d['d'])

print('='*50)
# ==================================================================
import sys
import re

WORD_RE = re.compile(r'\w+')
index = {}

with open('09-19_keunhoi.txt') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1 # 이렇게 하는게 초보자들에게는 보기 편할듯
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

print(index)

for word in sorted(index, key=str.upper):
    print(word, index[word])

print(index)