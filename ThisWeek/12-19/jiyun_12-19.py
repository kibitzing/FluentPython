# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:36:15 2018

@author: jiyun
"""
from inspect import getgeneratorstate

print('------------예제 16-1----------------')
def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received :',x)
    

my_coro = simple_coroutine()
print(my_coro)
#my_coro.send(55) # 활성화해주어야함
next(my_coro) # 활성화
my_coro.send('12월 19일') # 값 전달 가능

print('------------예제 16-2----------------')
def simple_coroutine2(a):
    print('-> Started : a =', a)
    b = yield a
    print('-> Received : b =',b)
    c = yield a+b
    print('-> Received : c =',c )
    print(getgeneratorstate(my_coro2)) #GEN_RUNNING
    
    
my_coro2 = simple_coroutine2(12) 
print(getgeneratorstate(my_coro2)) #GEN_CREATED

next(my_coro2)
print(getgeneratorstate(my_coro2)) # #GEN_SUSPENDED

my_coro2.send(19)

my_coro2.send(None) # 코루틴 끝까지 실행 
#-> Received : c = None #GEN_RUNNING

# print(getgeneratorstate(my_coro2))
# GEN_CLOSED