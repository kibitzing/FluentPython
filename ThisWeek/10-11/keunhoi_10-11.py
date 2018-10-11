#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from functools import reduce
from operator import add

def factorial(n):
	'''returns n!'''
	return 1 if n < 2 else n * factorial(n-1)

print('□42! =', factorial(42))
print('□doc of factorial :', factorial.__doc__)
print('□type of factorial :', type(factorial))
print('□"help" of factorial :', help(factorial)) # help가 뒤에 있음에도 먼저 출력되는 부분이 있다.

print('=' * 50)

fact = factorial
print('□type of factorial :', type(fact))
print(map(factorial, range(11)))
print(list(map(fact, range(11))))

print('=' * 50)

people = ['daeha','jingu','sanghong','seongbin','jiyun','seunghyun','keunhoi']
print('□Print people :', people)
people = sorted(people, key=len)
print('□Print people sorted by length :', people)
# 책에서 sorted()는 일급 함수라고 오타가 난 듯 하다. 함수를 인자로 받을 수 있기에 sorted()는 고위 함수가 맞다.

print('=' * 50)

start = time.clock()
list(map(fact,range(6)))
elapsed1 = (time.clock() - start)

start = time.clock()
[fact(n) for n in range(6)]
elapsed2 = (time.clock() - start)

start = time.clock()
list(map(factorial, filter(lambda n: n % 2, range(6))))
elapsed3 = (time.clock() - start)

start = time.clock()
[factorial(n) for n in range(6) if n % 2]
elapsed4 = (time.clock() - start)

print(list(map(fact,range(6))))
print('list-map\'s time is :', elapsed1)
print([fact(n) for n in range(6)])
print('list comprehension\'s time is :', elapsed2)
print('=' * 50)
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print('list-map-lambda\'s time is :', elapsed3)
print([factorial(n) for n in range(6) if n % 2])
print('list comprehension\'s time is :', elapsed4)
print('list comprehension is more easy to read and faster than lambda in this example!')



print('=' * 50)

print(reduce(add,range(100)))
print(sum(range(100)))

print('(True == bool([])) ==', True == bool([]))
print('(True == bool([1])) ==', True == bool([1]))
print('all([]) ==', all([]))
print('any([]) ==', any([]))
print('What the...')

print('=' * 50)

def reverse(word):
	return word[::-1]

print(reverse('testing_example_codes'))

people = sorted(people, key=reverse)

start = time.clock()
sorted(people, key=reverse)
elapsed5 = (time.clock() - start)

print('□Print people sorted after being reversed :', people)
print('sorted by reverse function\'s time is :', elapsed5)

start = time.clock()
sorted(people, key=lambda word: word[::-1])
elapsed6 = (time.clock() - start)

print('□Print people sorted after being reversed by lambda :', sorted(people, key=lambda word: word[::-1]))
print('sorted by lambda\'s time is :', elapsed6)
print('Again, lambda is nothing better this time!')