#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 27/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        collections.abc 에서 하나 상속해서 사용해보기.
        Iterator 골라서 __next__작성, __iter__ 오버라이드
"""
from collections.abc import Iterator
class MyIterator(Iterator):
    def __init__(self, list):
        self.list = list
        self.i = 0

    def __iter__(self):
        return iter(self.list + [i + self.list[-1] for i in self.list])

    def __next__(self):
        if self.i >= len(self.list):
            self.list += self.list
        idx = self.i
        self.i += 1
        return self.list[idx]

myIter = MyIterator([1,2,3,4])

print(myIter.list)

for i in myIter:
    print('i:', i)
    print('next(myIter):',next(myIter))
print('myIter.list:', len(myIter.list))
