#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 동적 속성을 이용한 데이터 랭글링

"""
class cls:
    a = 1
    def b(self):
        pass

hasattr(cls, 'b')
getattr(cls, 'a')

setattr(cls, 'a', 29)
print(cls.a)  # 29