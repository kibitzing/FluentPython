#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    조회할 때 키를 문자열로 변환하는 StrKeyDict0
    오늘은 파이썬 문법에서 상당히 흥미로운 내용을 배워서 일단 손수 옮겨서 그대로 코딩해 보았습니다ㅎㅎ
"""



class StrKeyDict0(dict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return '웁쓰~~!'#default
        
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
    
d = StrKeyDict0([('2', 'two'), ('4', 'four')])

print(d['2'])  # two
print(d['3'])  # KeyError: '3'

print(d[4])  # four
print(d['4'])

print(2 in d)  # True
print(3 in d)  # False
print(4 in d)  # True

print(d.get('2'))  # two
print(d.get('3'))  # 웁쓰~~!