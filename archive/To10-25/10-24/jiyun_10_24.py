# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:20:42 2018

@author: jiyun
"""

def Averager():
    
    def __init__(self):
        self.series = []
        
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)
    
    return __call__
    
avg = Averager()

print(avg.__code__.co_varnames) #('self', 'new_value', 'total')
print(avg.__code__.co_freevars) #()


def make_averager():
    count = 0
    total = 0 # 없으면 
    
    def averager(new_value):
        nonlocal count, total #여기서 에러 no binding for nonlocal 'count' found
        count += 1
        total += new_value
        return total / count
    
    return averager
avg = make_averager()

print(avg(10))

print(avg.__code__.co_varnames) #('new_value',)
print(avg.__code__.co_freevars) #('count', 'total')

import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

@clock
def Sum(n):
    return sum(range(n+1))

def minus(a,b):
    return a - b

if __name__=='__main__':
    print('*'*40, 'Calling snooze(5)')
    snooze(5) #[4.98722323s] snooze(5) -> None
    print('*'*40, 'Calling factorial(6)')
    print('6 != ', factorial(6))
    Sum(3) #[0.00000894s] Sum(3) -> 6
    minus(3,1) #print 하기전엔 X

