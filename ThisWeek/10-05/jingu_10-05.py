"""
created by Jingu Kang on 2018-10-05
coding: utf-8
"""

import sys, locale

expressions ="""
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
    print(expression.rjust(30), '->' , repr(value))

hello = 'hi'

print(repr(hello))
print(hello)

import numpy as np

npA = np.array([[1, 0],[2, 0]])
npB = np.array([[1, 2],[2, 3],[3,4]])

a = 'np.concatenate((npA,npB), axis=0)'
b = 'npA.shape'
k = "b = 'npB.shape'"
print(eval(a))
print(eval(b)) #(2, 2)

print(exec(k))
print(eval(b)) #(3, 2) 


##
#    locale.getpreferredencoding() -> 'UTF-8'
#                 type(my_file) -> <class '_io.TextIOWrapper'>
#              my_file.encoding -> 'UTF-8'
#           sys.stdout.isatty() -> False
#           sys.stdout.encoding -> 'UTF-8'
#            sys.stdin.isatty() -> False
#            sys.stdin.encoding -> 'UTF-8'
#           sys.stderr.isatty() -> False
#           sys.stderr.encoding -> 'UTF-8'
#      sys.getdefaultencoding() -> 'utf-8'
#   sys.getfilesystemencoding() -> 'utf-8'
    
# spyder 에서 돌려서 그런지,  false라고 뜸.