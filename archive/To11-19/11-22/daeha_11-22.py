#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" collections.UserDict를 상ㅎ속하여 오버라이드 문제를 해결하는 예제
    
    pages 439~443
"""


import collections

class DoppeDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)
        
        
class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42

    
if __name__ == "__main__":
    dd = DoppeDict2(one=1)
    print(dd)  # {'one': [1, 1]}
    
    dd['two'] = 2
    print(dd)  # {'one': [1, 1], 'two': [2, 2]}
    
    dd.update(three=3)
    print(dd)  # {'one': [1, 1], 'two': [2, 2], 'three': [3, 3]}
    
    ad = AnswerDict2(a='foo')
    print(ad['a'])  # 42
    
    dic = {}
    dic.update(ad)
    print(dic['a'])  # 42
    
    print(dic)  # {'a': 42}