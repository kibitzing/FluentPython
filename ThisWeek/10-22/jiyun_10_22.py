# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:00:53 2018

@author: jiyun
"""
k = 0

def deco(func):
    def inner():
        print('running inner()')
    return inner
    
@deco
def target():
    print('running target()')
 
target() #deco 없을 때 running target(), 있을 때 running inner()
print(target) # <function target at 0x000001752D7D9B70>
              # <function deco.<locals>.inner at 0x000001752D7D9EA0>

registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

if k == 1:
    @register #따로 조건문으로는 X
    def f1():
        print('running f1()')
    
@register
    
def main():
    print('running main()')
    print('registry ->', registry)

if __name__ == '__main__':
    k = 3
    main() #f2만 포함
def f2():
    print('running f2()')
    
def f3():
    print('running f3()')