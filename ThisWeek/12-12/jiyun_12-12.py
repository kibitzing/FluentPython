# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:32:03 2018

@author: jiyun
"""

# 원서 기준 428~432p

import itertools
import operator

"""
itertools.accumulate() 제너레이터 함수 예
"""
sample = [9,8,1,6,5,4,3,2,10]

list(itertools.accumulate(sample))
list(itertools.accumulate(sample,min)) #[9, 8, 1, 1, 1, 1, 1, 1, 1]
list(itertools.accumulate(sample,max)) #[9, 9, 9, 9, 9, 9, 9, 9, 10]
list(itertools.accumulate(sample,operator.mul))

"""
매핑 제너레이터 함수 예
"""

list(enumerate('albatroz',1))
list(map(operator.mul, range(1,10), [2,3,4])) # 짧은 반복형 끝나면 생성 중단 [2, 6, 12]
list(map(lambda a,b : (a,b), range(1,10), [2,3,4])) # [(1, 2), (2, 3), (3, 4)]
list(itertools.starmap(operator.mul, enumerate('albatroz',2)))
#['aa', 'lll', 'bbbb', 'aaaaa', 'tttttt', 'rrrrrrr', 'oooooooo', 'zzzzzzzzz']

"""
병합 생성자 함수 예
"""

list(itertools.chain('ASD', range(5)))
list(itertools.chain(enumerate('ASD'))) #[(0, 'A'), (1, 'S'), (2, 'D')]
#list(zip(range(5),'ASD')) #[(0, 'A'), (1, 'S'), (2, 'D')] 동일
list(itertools.chain.from_iterable(enumerate('ASD'))) # 반복형이어야 연결
list(zip('ASD', range(5))) #[('A', 0), ('S', 1), ('D', 2)]
list(itertools.zip_longest('ASD', range(5))) #[('A', 0), ('S', 1), ('D', 2), (None, 3), (None, 4)]
list(itertools.zip_longest('ASD', range(5), fillvalue = '**')) #[('A', 0), ('S', 1), ('D', 2), ('**', 3), ('**', 4)]

"""
itertools.product() 제너레이터 함수 예
"""
suits = 'spades hearts diamonds clubs'.split()
list(itertools.product('AB', suits)) #[('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'), ('B', 'spades'), ('B', 'hearts'), ('B', 'diamonds'), ('B', 'clubs')]
list(itertools.product('AB', repeat = 2)) #[('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]

"""
count(), cycle(), repeat() 사용 예
"""

ct = itertools.count(2)
next(ct) #2
next(ct) #3
next(ct) #4 
list(itertools.islice(itertools.count(1, .3),3)) #[1, 1.3, 1.6]
list(itertools.takewhile(lambda n:n<1.7, itertools.count(1, .3))) #[1, 1.3, 1.6]
list(map(operator.mul, range(5), itertools.repeat(3))) #[0, 3, 6, 9, 12]






