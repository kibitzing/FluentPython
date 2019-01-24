#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 프로퍼티 속성을 이용한 예제

    refer link:
    https://stackoverflow.com/questions/3681272/can-i-get-a-reference-to-a-python-property

"""

def get_dict_attr(obj, attr):
    for obj in [obj] + obj.__class__.mro():
        if attr in obj.__dict__:
            return obj.__dict__[attr]
    raise AttributeError
    

class Foo(object):
    
    def __init__(self, x):
        self.x = x
        
    def bar(self, x):
        print("bar")
        return x
        
    @property
    def bat(self):
        return 0
    
    
foo = Foo(29)
print(get_dict_attr(foo, 'x'))  # 29
print(get_dict_attr(foo, 'y'))  # AttributeError

print(get_dict_attr(foo, 'bar'))  # <function Foo.bar at 0x117b4a730>
print(get_dict_attr(foo, 'bat'))  # <property object at 0x117b2d3b8>


f = foo.bar(10)
print(f)  # 10

f = foo.bat
print(f)  # 0

f = get_dict_attr(foo, 'bar')
print(f)