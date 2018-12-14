#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 14/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        simple variations of itertools.groupby
"""
import itertools
l1= list(itertools.groupby('LLLLAGGG'))
print(l1)

for char, group in itertools.groupby('LLLaaaagggGG'):
    print(char, '->', list(group))

for char, group in itertools.groupby('LLLaaaagggGG'.lower()):
    print(char, '->', list(group))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin','shark','lion']
animals.sort(key=len)
print(animals)

for length , group in itertools.groupby(animals, len):
    print(length, '->', list(group))

for length , group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))

names = ['이준', '이강','강진구', '조인성','강다니엘','황우슬혜']
for length , group in itertools.groupby(names, len):
    print('name length:', length, '->', list(group))
# name length: 2 -> ['이준', '이강']
# name length: 3 -> ['강진구', '조인성']
# name length: 4 -> ['강다니엘', '황우슬혜']
