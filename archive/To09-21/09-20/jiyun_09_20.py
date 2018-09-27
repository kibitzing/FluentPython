# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 19:11:51 2018

@author: jiyun
"""

import collections

class StrKeyDict0(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default = None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self,key):
        return key in self.keys() or str(key) in self.keys()

########################################################################
        
ct = collections.Counter('python collections')
print(ct)
ct.update('python')
print(ct)
print(ct.most_common(3)) #[('o', 4), ('n', 3), ('t', 3)]

persons = [('Jim', 12121215), ('Kim', 12141215), ('Amy', 12151845)]
mydict = dict(persons)
print(mydict) 
#{'Kim': 12141215, 'Amy': 12151845, 'Jim': 12121215}
mydict.update({'홍길동':12121514,'김철수':12147152})
print(mydict) 
#{'홍길동': 12121514, 'Kim': 12141215, 'Amy': 12151845, 'Jim': 12121215, '김철수': 12147152}


mydict = collections.OrderedDict(persons)
print(mydict) 
#OrderedDict([('Jim', 12121215), ('Kim', 12141215), ('Amy', 12151845)])
mydict.update({'홍길동':12121514,'김철수':12147152})
print(mydict) 
#OrderedDict([('Jim', 12121215), ('Kim', 12141215), ('Amy', 12151845), ('홍길동', 12121514), ('김철수', 12147152)])

a = [{'one':1,'two':2,'three':3}]
chainmap = collections.ChainMap(*a)
print(chainmap['one']) #1

########################################################################

b = {}
b['x'] = 1;
b['y'] = 2;
b['z'] = 3;
print(b.popitem()) #('z', 3)
for key,value in b.items():
   print(key, value)
    # y 2
    # x 1

c = collections.OrderedDict()
c['x'] = 1;
c['y'] = 2;
c['z'] = 3;

#print(c.popitem(last=True)) #('z', 3)
print(c.popitem(last=False)) #('x', 1)
for key,value in c.items():
    print(key, value)
    # y 2
    # z 3

