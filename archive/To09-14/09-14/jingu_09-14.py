"""
created by Jingu Kang on 09-14-2018
"""

import bisect

softmax_result = [0.12, 0.35, 0.22, 0.89, 0.66, 0.90, 0.98, 0.11, 0.24]
classifier_param = [0.33, 0.66, 0.90]
classes = ['white noise', 'pink noise', 'babble noise', 'speech']
my_answer = []
for result in softmax_result:
    position = bisect.bisect(classifier_param, result)
    print('just bisect: ', position)
    my_answer.append(classes[position])
    
    position = bisect.bisect_left(classifier_param, result)
    print('bisect left: ', position)
    position = bisect.bisect_right(classifier_param, result)
    print('bisect right: ', position)
    # only different when needle = haystack, bisect = right, left는 왼쪽을 뱉어줌.

print(' '.join('%11s' % prob for prob in softmax_result[1:6]))
print(' '.join('%11s' % ans for ans in my_answer[1:6]))

#result:       0.35        0.22        0.89        0.66         0.9
#        pink noise white noise babble noise babble noise      speech
 
#import bisect 
#import sys
#import random 
#
#HAYSTACK = [1,4,5,6,8,12,15,20,21,23,26,29,30]
#NEEDLES = [0,1,2,5,8,10,22,23,29,30,31]
#
#ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'
#
#def demo(bisect_fn):
#    for needle in reversed(NEEDLES):
#        position = bisect.bisect_right(HAYSTACK, needle)
#        offset = position * '  |'
#        print(ROW_FMT.format(needle, position, offset))
#        
#
#if __name__ == '__main__':
#    if sys.argv[-1] == 'left':
#        bisect_fn = bisect.bisect_left
#    else:
#        bisect_fn = bisect.bisect_right
#        
#    print('DEMO: ' ,bisect_fn.__name__)
#    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
#    demo(bisect_fn)
#
#def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect.bisect(breakpoints, score)
#     print(i)
#     return grades[i]
# 
#print([grade(score) for score in  [33,99,77,70,89,90,100]])
#
#SIZE = 7
#random.seed(1729)
#my_list = []
#for i in range(SIZE):
#    new_item = random.randrange(SIZE*2)
#    bisect.insort(my_list, new_item)
#    print('%2d -> ' % new_item, my_list)
