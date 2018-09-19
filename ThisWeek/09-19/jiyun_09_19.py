# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:17:27 2018

@author: jiyun
"""

import sys
import re
import collections


WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)

# 이름으로 자리 찾기
with open('09_19.txt') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)
            

for word in sorted(index, key=str.upper):
    if(word == 'Park'):
        print(word, index[word]) #Park [(1, 5)]

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default = None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self,key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('12151245','Jim'),('12141245','Kim'),('12128455','Amy')])
print(d['12151245']) #Jim
print(d['Jim']) #KeyError : Jim
print(d.get('Jim')) #None
print(d.get('12141245')) #Kim
