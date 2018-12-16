#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 09/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        learn how to use itertools fluently.
        simple variations.
        
"""
import operator
import itertools
print(list(itertools.product('ABC', range(2))))
print(list(itertools.product('ABC', 'MF')))

suits = 'spades hearts diamonds clubs'.split()
print(list(itertools.product(suits, 'KQJ')))

print(list(itertools.product('ABC', repeat=3)))
print(len(list(itertools.product('ABC', repeat=3))))

print(list(itertools.product(range(2), repeat=3)))

rows = itertools.product('AB', range(2), repeat=2)
for row in rows:
    print(row)


counter = itertools.count()
print(next(counter), next(counter), next(counter))
counter2 = itertools.islice(itertools.count(1,.3),3)
print(next(counter2), next(counter2), next(counter2))

cy = itertools.cycle('abc')
print(next(cy),next(cy),next(cy),next(cy))

eight_four = (itertools.repeat(8,4))
print(next(eight_four), next(eight_four), next(eight_four), next(eight_four))
# print(next(eight_four), next(eight_four), next(eight_four), next(eight_four), next(eight_four))

print(list(map(operator.mul, range(11), itertools.repeat(5))))

print(list(itertools.combinations('abcd',2)))
print(list(itertools.combinations('abcd',3)))

print(list(itertools.combinations_with_replacement('abcd',2)))
print(list(itertools.permutations('abc',2)))
print(list(itertools.product('abc',repeat=2)))
print(set(itertools.product('abc',repeat=2)) - set(itertools.permutations('abc',2)))

