#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 오버라이딩 예제

"""
def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))
    
    
def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))
    
    
### essential classses for this example ###
class Overriding:
    """a.k.a. data descriptor or enforced descriptor"""
    
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)
        
    def __set__(self, instance, value):
        print_args('set', self, instance, value)
        

class OverridingNoGet:
    """an overriding descriptor without ``__get__``"""
    
    def __set__(self, instance, value):
        print_args('set', self, instance, value)
        
        
class NonOverriding:
    """a.k.a. non-data or shadowable descriptor"""
    
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)
        
        

class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()
    
    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))
        
        
obj = Managed()
obj.over
Managed.over

obj.over = 7
obj.over

obj.__dict__['over'] = 8
vars(obj)
obj.over