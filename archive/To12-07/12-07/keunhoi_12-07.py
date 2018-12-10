#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p411~415
# Example 14-5~6

'''
    예제 위주의 작성
'''

# Example 14-5
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


def gen_123():
    yield 1
    yield 2
    yield 3

def gen_1234():
    yield 1
    yield 2
    yield 3
    yield 4
    return

# Example 14-6
def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


if __name__ == '__main__':

    print("{0:=<50}".format("Example 14-5 : gen_123 & gen_1234 "))
    gen_123()
    gen_1234()

    print(hasattr(Sentence, '__iter__'))
    print(hasattr(Sentence, '__next__'))

    print("\n{0:=<50}".format("Example 14-5 : gen_123 & gen_1234 for gate "))
    for i in gen_123():
        print(i)

    print(next(gen_123()))  # 1
    next(gen_123())         # print 안에 들어가지 않은 next 내장함수를 끼워 넣어도 그대로임
    print(next(gen_123()))  # 1 1
    print(next(gen_123()))  # 1 1 1
    print(next(gen_1234())) # 1 1 1 1
    print(next(gen_1234())) # 1 1 1 1 1
    print(next(gen_1234())) # 1 1 1 1 1 1
    print(next(gen_1234())) # 1 1 1 1 1 1 1

    print("\n{0:=<50}".format("Example 14-6 : gen_AB "))
    for c in gen_AB():
        print('-->', c)