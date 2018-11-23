class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key,[value]*2)


dd = DoppelDict(one=1)
print(dd)
dd['two'] = 2
print(dd)
dd.update(three =3)
print(dd)

class AnswerDict(dict):
    def __getitem__(self, item):
        return 42

ad = AnswerDict(a='foo')
print(ad['a'])
d = {}
d.update(ad)
print(d['a'])
print(d)

import collections

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key,[value]*2)


dd2 = DoppelDict2(one=1)
print(dd2)
dd2['two'] = 2
dd2.update(three=3)
print(dd2)

class AnswerDict2(collections.UserDict):
    def __getitem__(self, item):
        return 42

ad2 = AnswerDict2(a='foo')
print(ad2['a'])
d2 = {}
d2.update(ad2)
print(d2['a'])
print(d)
