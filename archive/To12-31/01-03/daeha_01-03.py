#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 기본적인 threading 개념을 이해해보는 예제

"""
import threading
import time

def response(msg):
    for i in range(5):
        time.sleep(1)
        print(msg)
        

for msg in ['THREAD1', 'THREAD2', 'THREAD3']:
    t = threading.Thread(target=response, args=(msg, ))  # args option is essential!!
    t.start()
    
    
class MyThread(threading.Thread):
    def __init__(self, msg, c):
        threading.Thread.__init__(self)
        self.msg = msg
        self.c   = c
    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)
            print('c is {}'.format(self.c))
            
            self.c += 1
            if self.c == 10:
                print('Oh~ see you next time!')
                break
            
msg = ['Knok', 'Knowknok', 'Mewmew~']
count = 1

t = MyThread(msg, c=count)
t.start()
t.is_alive()  # True
"""
            ['Knok', 'Knowknok', 'Mewmew~']
            c is 1
            ['Knok', 'Knowknok', 'Mewmew~']
            c is 2
            ['Knok', 'Knowknok', 'Mewmew~']
            c is 3
            ['Knok', 'Knowknok', 'Mewmew~']
            c is 4
            ['Knok', 'Knowknok', 'Mewmew~']
            c is 5
            ['Knok', 'Knowknok', 'Mewmew~']
            c is 6
            ['Knok', 'Knowknok', 'Mewmew~']
            c is 7
            ['Knok', 'Knowknok', 'Mewmew~']
            c is 8
            ['Knok', 'Knowknok', 'Mewmew~']
            c is 9
            Oh~ see you next time!
"""

t.is_alive()  # False