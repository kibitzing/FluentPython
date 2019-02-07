#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 메타프로그래밍

"""
class Dog:
    
    def __init__(self, name, weight, owner):
        self.name = name
        self.weight = weight
        self.owner = owner
        
        
def record_factory(cls_name, field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:  # no .replace or .split
        pass  # assume it's already a sequence of identifiers
    field_names = tuple(field_names)
    
    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)
            
    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)
            
    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i) for i
                           in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)
    
    cls_attrs = dict(__slots__ = field_names,
                     __init__ = __init__,
                     __iter__ = __iter__,
                     __repr__ = __repr__)
    
    return type(cls_name, (object,), cls_attrs)

        
rex = Dog('Rex', 30, 'Bob')
print(rex)  # <__main__.Dog object at 0x1176557f0>

Dog = record_factory('Dog', 'name weight owner')
rex = Dog('Rex', 30, 'Bob')
print(rex)  # Dog(name='Rex', weight=30, owner='Bob')

name, weight, _ = rex
name, weight

"{2}'s dog weights {1}kg".format(*rex)  # "Bob's dog weights 30kg"

rex.weight = 50
rex  # Dog(name='Rex', weight=50, owner='Bob')

Dog.__mro__  # (__main__.Dog, object)
