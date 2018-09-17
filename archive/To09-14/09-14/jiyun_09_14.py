# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:32:30 2018

@author: jiyun
"""
import bisect
import sys

HAYSTACK = [0,5,10,15,20,25,30]
NEEDLES = [0,1,3,4,25,7,9,11,14,18,20,21,23,24,28,20,33]
NEEDLES.sort()

ROW_FMT = '{0:2d} @ {1:2d}     {2}{0:2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO:', bisect_fn.__name__)
    print('haystack -> ',' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
    
################################################################

def tier(score, breakpoints = [1500,2000,2500,3000], grades = 'BSGPD'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print([tier(score) for score in [847,1840,2100,2502,2850,3400]])
#['B', 'S', 'G', 'P', 'P', 'D']

################################################################

import random
SIZE = 5

random.seed(0)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*4)
    if(new_item >= 8):
        bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

################################################################
from array import array
from random import random

floats = array('d', (random() for i in range(10**5)))
print(floats[0]) #0.48592769656281265
fp = open('floats.bin','wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,10**5)
fp.close()
print(floats2[0]) #0.48592769656281265
print(floats2 != floats) #False



