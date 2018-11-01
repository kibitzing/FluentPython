#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" WeakValueDictionary에 관한 예제
"""

class Cheese:
    
    def __init__(self, kind):
        self.kind = kind
        
    def __repr__(self):
        return 'cheese(%r)' % self.kind
    
    
import weakref
stock = weakref.WeakValueDictionary()

bag = [Cheese('Red Leicester'), Cheese('Parmasan'),
       Cheese('Tilsit'), Cheese('Brie')]


for cheese in bag:
    stock[cheese.kind] = cheese
    
sorted(stock.keys())  # ['Brie', 'Parmasan', 'Red Leicester', 'Tilsit']

del bag
sorted(stock.keys())  # ['Brie']

del cheese
sorted(stock.keys())  # []
