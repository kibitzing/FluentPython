#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 12/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        try using functions in itertools
"""

def vowel(c):
    return c.lower() in 'aeiou'

print(list(filter(vowel, 'Aardvark')))
# ['A', 'a', 'a']

import itertools
print(list(itertools.filterfalse(vowel, 'Aardvark')))
# ['r', 'd', 'v', 'r', 'k']
print(list(itertools.dropwhile(vowel, 'Aaerdvaeirk')))
# ['r', 'd', 'v', 'a', 'e', 'i', 'r', 'k']
print(list(itertools.takewhile(vowel, 'Aeardvaaerk')))
# ['A', 'e', 'a']
print(list(itertools.compress('Aardvark', (1,0,1,1,0,1))))
# ['A', 'r', 'd', 'a']
print(list(itertools.islice('Aardvark',4)))
# ['A', 'a', 'r', 'd']
print(list(itertools.islice('Aardvark', 4, 7)))
# ['v', 'a', 'r']
print(list(itertools.islice('AbAdApAgArAk', 0, 12, 2)))
# ['A', 'A', 'A', 'A', 'A', 'A']

sample = [5,4,2,8,7,6,3,0,9,1]
print(list(itertools.accumulate(sample))) # 뒤로 다 더해짐
# [5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
print(list(itertools.accumulate(sample,min))) # 최소값만 남김
# [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
print(list(itertools.accumulate(sample,max))) # 최대값만 남김
# [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]

import operator
print(list(itertools.accumulate(sample, operator.mul)))
# [5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0] # 다 곱함
print(list(itertools.accumulate(range(1,11), operator.mul)))
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

print(list(enumerate('albatroz', 2)))
# [(2, 'a'), (3, 'l'), (4, 'b'), (5, 'a'), (6, 't'), (7, 'r'), (8, 'o'), (9, 'z')]

print(list(map(operator.mul, range(11), range(2,13))))

print(list(map(lambda a,b :(a,b), range(11), [2,4,8])))
# [(0, 2), (1, 4), (2, 8)]
print(list(map(lambda a,b : a*b, range(11), [2,4,8])))
# [0, 4, 16]

print(list(itertools.starmap(operator.mul, enumerate('albatroz',1))))
# ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']

# sample = [5,4,2,8,7,6,3,0,9,1]
print(list(itertools.starmap(lambda a,b : b/a, enumerate(itertools.accumulate(sample), 1))))
# [5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333, 5.0, 4.375, 4.888888888888889, 4.5]

print(list(itertools.chain('ABC', range(2)))) # 뒤로 붙여줌
# ['A', 'B', 'C', 0, 1]

print(list(itertools.chain(enumerate('abc'), [11,22,33])))
# [(0, 'a'), (1, 'b'), (2, 'c'), 11, 22, 33]

print(list(itertools.zip_longest('Abc', [1,2,3,5,7])))
# [('A', 1), ('b', 2), ('c', 3), (None, 5), (None, 7)]
print(list(itertools.zip_longest('Abc', [1,2,3,5,7], fillvalue= '^_^')))
# [('A', 1), ('b', 2), ('c', 3), ('^_^', 5), ('^_^', 7)]
