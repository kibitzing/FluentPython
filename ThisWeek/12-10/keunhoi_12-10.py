#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p416~420
# Example 14-7~10

'''
    큰 데이터 나눠서 받기
'''

# Example 14-7
import re
import reprlib

import numpy as np

RE_WORD = re.compile('\w+')

class Sentence_14_7:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


# Example 14-9
class Sentence_14_9:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text)) # T.C로 for 반복문을 구현함


# Example 14-8
def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


# Custom Code

DATA = np.array(range(10**6))

def data_generator(DATA, batch_size=1):
    for i in range(0,len(DATA),batch_size):
        yield DATA[i:i+batch_size]

if __name__ == '__main__':

    print("\n{0:=<50}".format("Example 14-8"))
    res1 = [x*3 for x in gen_AB()]
    print('res1 is :', res1)

    for i in res1:
        print('-->', i)

    res2 = (x*3 for x in gen_AB())
    print(res2)
    for i in res2:
        print('-->', i)

    # print("\n{0:=<50}".format("Example 14-9"))
