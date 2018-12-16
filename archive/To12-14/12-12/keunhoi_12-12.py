#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p426~430
# Example 14-15~20

'''
   예제 위주 작성
'''

if __name__ == '__main__':

    sample = [5,4,2,7,8,6,3,0,9,1]
    import itertools
    list(itertools.accumulate(sample))
    list(itertools.accumulate(sample, min))
    list(itertools.accumulate(sample, max))
    import operator
    list(itertools.accumulate(sample, operator.mul))
    list(itertools.accumulate(range(1,11), operator.mul))

    list(enumerate('albatroz', 1))
    list(map(operator.mul, range(11), range(11)))
    list(map(operator.mul, range(11), [3,5,7]))
    list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))
    list(itertools.starmap(lambda a, b: b / a,
                           enumerate(itertools.accumulate(sample), 1)))

    list(itertools.chain('ABC', range(2)))
    list(itertools.chain(enumerate('ABC')))
    list(itertools.chain.from_iterable(enumerate('ABC')))
    list(zip('ABC', range(5)))
    list(zip('ABC', range(5), [10, 20, 30, 40]))
    list(itertools.zip_longest('ABC', range(5)))
    list(itertools.zip_longest('ABC', range(5), fillvalue='?'))

    list(itertools.product('ABC', range(2)))
    suits = 'spades hearts diamonds clubs'.split()
    list(itertools.product('AK', suits))
    list(itertools.product('ABC'))
    list(itertools.product('ABC', repeat=2))
    list(itertools.product(range(2), repeat=3))
    rows = itertools.product('AB', range(2), repeat=2)
    for row in rows: print(row)

    ct = itertools.count()
    next(ct)
    next(ct), next(ct), next(ct)
    list(itertools.islice(itertools.count(1, .3), 3))
    cy = itertools.cycle('ABC')
    next(cy)
    list(itertools.islice(cy, 7))
    rp = itertools.repeat(7)
    next(rp), next(rp)
    list(itertools.repeat(8, 4))
    list(map(operator.mul, range(11), itertools.repeat(5)))

    list(itertools.combinations('ABC', 2))
    list(itertools.combinations_with_replacement('ABC', 2))
    list(itertools.permutations('ABC', 2))
    list(itertools.product('ABC', repeat=2))