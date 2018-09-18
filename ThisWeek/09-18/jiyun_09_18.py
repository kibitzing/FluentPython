# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:43:46 2018

@author: jiyun
"""
my_dict = {}
import collections
print(type(my_dict)) #<class 'dict'>
print(isinstance(my_dict, collections.abc.Mapping)) #True

###########################################################

tt = (1,2,(30,40))
print(hash(tt)) #8027212646858338501
tl = (1,2,(30,40))

def __eq__(self, other):
    return hash(self) == hash(other)

print(__eq__(tt,tl)) #True

tf = (1,2,[30,40])

try : 
    hash(tf)
except TypeError:
    print('unhashable type')

###########################################################
    
a = dict(one = 1, two = 2, three = 3) #{'two': 2, 'one': 1, 'three': 3}
b = {'one' : 1, 'two' : 2, 'three' : 3} #{'two': 2, 'one': 1, 'three': 3}
c = dict(zip(['one','two','three'], [1,2,3])) #{'two': 2, 'one': 1, 'three': 3}
d = dict([('two',2),('one',1),('three',3)]) #{'two': 2, 'one': 1, 'three': 3}
e = dict({'three':3, 'one':1, 'two' : 2}) #{'two': 2, 'one': 1, 'three': 3}

###########################################################

Code = [(1,'one'),(2,'two'),(3,'three')]
code = {value: key for key, value in Code} 
print(code) #{'two': 2, 'one': 1, 'three': 3}

for key,value in code.items():
    if(value >= 2):
        print({value : key.upper()})
        # {2: 'TWO'}
        # {3: 'THREE'}

###########################################################

print(code.popitem()) #('two', 2)
print(code) #{'one': 1, 'three': 3}
print(code.values()) #dict_values([1, 3])
        

