# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:50:44 2018

@author: jiyun
"""
# 원서 기준 14장 ~ 504p


import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __getitem__(self, index): # __iter__ 구현하지 않아도 반복자 생성
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    
    def __repr__(self):
        return 'Sentence(%s)' %reprlib.repr(self.text) # 30자로 제한 
    

s = Sentence('"The time has come," the Walrus said')
print(s) #Sentence('"The time ha...e Walrus said')

for word in s:
    print(word)

print(list(s))    
    



