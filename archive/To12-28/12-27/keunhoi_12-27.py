#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p488-492
# Example 16-18~19

'''
   예제 위주 작성
'''

import collections

# Example 16-20
Event = collections.namedtuple('Event', 'time proc action')

def taxi_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')

if __name__ == '__main__':
    print('{0:=<50}'.format("Example 16-20"))
    taxi_process(15, 'James')
