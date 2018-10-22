#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

""" python decorator를 다뤄보는 예제
"""

# 데코레이터에게 인자 넘기기
def add_tags(tag_name):
    print("Generate decorator")
    
    def set_decorator(func):
        def wrapper(username):
            return "<{0}>{1}</{0}>".format(tag_name, func(username))
        return wrapper
    return set_decorator

@add_tags("div")
def greeting(name):
    return "Hello " + name

print(greeting("kdh"))


# Class로 데코레이터 만들기

class Admin(object):
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        name = kwargs.get('name').upper()
        id = kwargs.get('id').lower()
        self.func(name, id)
        
        
@Admin
def greeting(name, id):
    print("Hello {} {}".format(name, id))
    
greeting(name='daeha', id='0123456789')


