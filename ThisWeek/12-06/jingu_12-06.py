#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 05/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        while 과 next를 사용하여 for문으로 했던 것 구현
"""

import re
import reprlib

RE_WORD = re.compile('\w+')

class Plurals:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item] + 's'

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Plural words(%s)' % reprlib.repr(['four ' + word + 's' for word in self.words])

    # def __iter__(self):
    #     yield from ['two ' + word + 's' for word in self.words]

singulars = "cat dog student ball cup"
plurals = Plurals(singulars)

print(plurals)
# Plural words(['four cats', 'four dogs', 'four students', 'four balls', 'four cups'])

for plural_word in plurals:
    print(plural_word)

it = iter(plurals)
print('### From here using While: ')
counter = 1
while True:
    try:
        print('what is for now?', next(it))
        print('what is left?', list(it))
    except StopIteration:
        del it
        break

    it = iter(plurals)
    for i in range(counter):
        a = next(it)
    counter += 1
