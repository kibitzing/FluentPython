#!/usr/bin/envs python3
# -*- coding: utf-8 -*- --> 파이썬 3부터는 utf-8이 기본 인코딩임

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_09_19_Fluent_Python
@Author Sanghong.Kim
이름순 정리 프로그램
sanghong_09-19_Text 라는 파일 추가 첨부
금일은 예제만 적용하였음
"""

# Import Modules
import os
import collections
import re

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)
with open('sanghong_09-19_Text') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)

# List 형 TEXT 생성
text = []

for word in sorted(index, key=str):
    text.append(word)

# 두개의 차이 -> 당연하지만 자료형이 다름
ty1 = type(index)
ty2 = type(text)

# Sorted 된 text 프린트
print(text)