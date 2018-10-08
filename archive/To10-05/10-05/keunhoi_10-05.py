#!/usr/bin/env python3
# -*- coding: utf-8 -*-

open('cafe.txt', 'w', encoding='utf_8').write('café')
print(open('cafe.txt').read()) # caf챕이라고 나오네요..?

fp = open('cafe.txt','w',encoding='utf_8')
fp.write('café')
# print(fp.read())
fp.close

import os
os.stat('cafe.txt')
fp2 = open('cafe.txt')
print(fp2.encoding)
print(fp2.read())

fp3 = open('cafe.txt', encoding='utf_8')
print(fp3.read())

fp4 = open('cafe.txt', 'rb')
print(fp4.read())

import sys, locale

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

print('='*50)

my_file = open('dummy', 'w',encoding='utf_8')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))