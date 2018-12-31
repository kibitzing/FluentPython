# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 17:53:58 2018

@author: jiyun
"""
# 전부 디폴트 값으로 대입

import collections
import queue
import random

Event = collections.namedtuple('Event','time proc action')

def taxi_process(ident, trips, start_time = 0):
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up')
        time = yield Event(time, ident, 'drop off')
        
    yield Event(time, ident, 'going home')

class Simulator:
    
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)
        
    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)
            
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi :', proc_id, proc_id*'  ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time : {} events pending ***'
            print(msg.format(self.events.qsize()))
            
def compute_duration(previous_action):
    if previous_action in ['leave garage', 'drop off']:
        interval = 5
    elif previous_action == 'pick up':
        interval = 20
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action : %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1

taxis = {i: taxi_process(i, (i+1)*2, i *5)
        for i in range(3)}
sim = Simulator(taxis)
sim.run(180)

"""
taxi : 0  Event(time=0, proc=0, action='leave garage')
taxi : 0  Event(time=2, proc=0, action='pick up')
taxi : 0  Event(time=4, proc=0, action='drop off')
taxi : 1    Event(time=5, proc=1, action='leave garage')
taxi : 0  Event(time=6, proc=0, action='pick up')
taxi : 1    Event(time=8, proc=1, action='pick up')
taxi : 2      Event(time=10, proc=2, action='leave garage')
taxi : 1    Event(time=18, proc=1, action='drop off')
taxi : 2      Event(time=19, proc=2, action='pick up')
taxi : 1    Event(time=20, proc=1, action='pick up')
taxi : 2      Event(time=20, proc=2, action='drop off')
taxi : 0  Event(time=21, proc=0, action='drop off')
taxi : 1    Event(time=21, proc=1, action='drop off')
taxi : 0  Event(time=22, proc=0, action='going home')
taxi : 1    Event(time=23, proc=1, action='pick up')
taxi : 2      Event(time=29, proc=2, action='pick up')
taxi : 2      Event(time=38, proc=2, action='drop off')
taxi : 2      Event(time=42, proc=2, action='pick up')
taxi : 1    Event(time=60, proc=1, action='drop off')
taxi : 1    Event(time=61, proc=1, action='pick up')
taxi : 1    Event(time=85, proc=1, action='drop off')
taxi : 1    Event(time=90, proc=1, action='going home')
taxi : 2      Event(time=121, proc=2, action='drop off')
taxi : 2      Event(time=122, proc=2, action='pick up')
taxi : 2      Event(time=126, proc=2, action='drop off')
taxi : 2      Event(time=127, proc=2, action='pick up')
taxi : 2      Event(time=142, proc=2, action='drop off')
taxi : 2      Event(time=156, proc=2, action='pick up')
taxi : 2      Event(time=171, proc=2, action='drop off')
taxi : 2      Event(time=177, proc=2, action='going home')
*** end of events ***
"""