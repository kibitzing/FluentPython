# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 18:29:04 2018

@author: jiyun
"""


dict1 = dict([('one', 1), ('two', 2)])
dict2 = dict([('two', 2),('one', 1)])
print(dict1 == dict2) #True

print(hash(frozenset(dict1))) #946168193661718782
print(hash(frozenset(dict2))) #946168193661718782

dict1 = tuple(dict1)
dict2 = tuple(dict2)

print(hash(dict1)) #-4615220839215464269
print(hash(dict2)) #6022524136612728435
