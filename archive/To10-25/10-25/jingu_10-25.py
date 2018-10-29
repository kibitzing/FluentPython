#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 25/10/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        단일 디스패치를 이용한 데코레이터 연습
        예제 7-21 에 실수 들어올 때 소수점 2자리만 남기는 것 추가하였음.

"""

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(obj)

@htmlize.register(numbers.Real)
def _(f):
    return  '<pre> {0} -> {0:.2f}</pre>'.format(f)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li' + inner + '</li>\n<ul>'


print(htmlize(42.2324))
print(htmlize(3.141592653589793238462))
print(htmlize(2.718281828459045235360287))

print('----###이하 예제###----')
print(htmlize(42.232))

print(htmlize(abs))
print(htmlize({1,2,3}))

print(htmlize(42))
print(htmlize("Heimlich & Co.\n - a game"))
