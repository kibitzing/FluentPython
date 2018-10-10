#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:23:16 2018

@author: jingu
"""

import unicodedata
import locale
import pyuca
coll = pyuca.Collator()

안녕 = '안녕하세요'
print(안녕) # 안녕하세요

print(locale.setlocale(locale.LC_COLLATE, 'ko_KR.UTF-8'))
문자열들 = ['안녕', 'ㅋㅋ','ㅎㅎ', '흐흐', '영어코딩','가위바위보', '한국어코딩', '냠냠', 'hello', 'bye']
# ['bye', 'hello', 'ㅋㅋ', 'ㅎㅎ', '냠냠', '안녕', '흐흐', '영어코딩', '가위바위보', '한국어코딩']
# 글자 수가 더 중요한 팩터, 잘 되지 않은 경우

정렬된문자열들 = sorted(문자열들, key=locale.strxfrm)
print(정렬된문자열들)
print(sorted(문자열들, key=coll.sort_key))
# ['bye', 'hello', '가위바위보', '냠냠', '안녕', '영어코딩', 'ㅋㅋ', 'ㅎㅎ', '한국어코딩', '흐흐']
# 잘 됐다.

