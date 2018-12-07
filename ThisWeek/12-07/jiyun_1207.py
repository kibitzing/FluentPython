# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 17:07:53 2018

@author: jiyun
"""
import re
import reprlib

# 원서 기준 413~417p

RE_WORD = re.compile('\w+')

class Sentence:
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
        
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self): # 제너레이터 함수
        for word in self.words:
            yield word 
        return
    # 반복자 클래스 필요 x
    
def gen_123():
    yield 1
    yield 2
    yield 3
    
print(gen_123) # 함수 객체
print(gen_123()) # 호출하면 제너레이터 객체 반환
for i in gen_123():
    print(i)
    
g = gen_123()
print(next(g))
print(next(g))
print(next(g))
#print(next(g))  # StopIteration

def gen_AB():
    print('start')
    yield 'A' # 값을 생성
    print('continue')
    yield 'B' # 값을 생성
    print('end.')
    
for c in gen_AB(): # for문에서 StopIteration 예외 잡아준다.
    print('-->', c)



