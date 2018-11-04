# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:33:35 2018

@author: jiyun
"""

import weakref

s1 = {1,2,3}
s2 = s1
def bye():
    print('Bye...')
ender = weakref.finalize(s1,bye)
print(ender.alive) #True
s2 = {1,2,3}
print(ender.alive) #True
del s1 #Bye...
print(ender.alive) #False

##################################################

class Cheese:
    
    def __init__(self, kind):
        self.kind = kind
        
    def __repr__(self):
        return 'Cheese(%r)' % self.kind
    
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese
    print(cheese)
    
print(sorted(stock.keys())) #['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']
del cheese
print(sorted(stock.keys())) #['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']
del catalog
print(sorted(stock.keys())) #[]


