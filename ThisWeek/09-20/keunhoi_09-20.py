#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class StrkKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys() # 메모: 재귀적 호출을 피하기 위함. 명시적으로 키를 조회.

d = StrkKeyDict0([('2', 'two'), ('4', 'four')])
print(type(d))
print(d['2'])
print(d.get('3'))
print(d.get('2', 'N/A'))
print(d.get('3', 'N/A'))
print(d) # no change

# 스크립트를 끝까지 돌리기 위해서 try 처리함.
try:
    print(d['3']) # KeyError: '3'
except KeyError as e:
    print('Passing KeyError by except.')

print('='*50)

import collections

ct = collections.Counter(d)
print(ct)
d_odict = collections.OrderedDict(d)
d_odict.popitem()
print(d_odict)
d_odict = collections.OrderedDict(d)
d_odict.popitem(last=False) # 책과는 다른 것 같습니다(아마도 오타). last=True로 하면 odict.popitem()과 같은 결과가 나옵니다.
print(d_odict)

print('='*50)

import builtins
pylookup = collections.ChainMap(locals(),globals(),vars(builtins))
print(pylookup)

print('='*50)

ct = collections.Counter('안녕하세요. 저는 코딩의 노예입니다.')
print(ct)
ct.update('노예의 삶은 힘이 들지요. 하지만 내일도 찬란한 해가 뜬답니다.')
print(ct)
del ct[' '], ct['.']
print(ct)

print('='*50)

class StrkKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data # 저장된 key가 모두 str형이므로, 명시적으로 조회하지 않고 바로 조회할 수 있다.

    def __setitem__(self, key, item):
        self.data[str(key)] = item

d = StrkKeyDict([('2', 'two'), ('4', 'four')])
print(d['2'])
print(type(d))