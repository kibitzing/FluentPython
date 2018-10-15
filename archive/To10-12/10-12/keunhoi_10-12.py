#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
print([callable(obj) for obj in (abs, str, int, float, 13, 'str', math)])

import random

class Lotto:

	def __init__(self, items):
		self._items = list(items)
		random.shuffle(self._items)

	def pick(self):
		self.numbers = []
		for i in range(6):
			self.numbers.append(self._items.pop())

		return self.numbers

	def __call__(self):
		return self.pick()

print("="*100)

lotto = Lotto(range(1,46))
print('The lotto numbers of this week:', lotto.pick())

print("="*100)

class Fail: pass
obj = Fail()
def Failfunc(): pass
print(sorted(set(dir(Failfunc))))
print(sorted(set(dir(obj))))
print(sorted(set(dir(Failfunc)) - set(dir(obj))))
print("="*100)

# example 5-10
def tag(name, *content, cls=None, **attrs):
	"""Generate one or more HTML tags"""
	if cls is not None:
		attrs['class'] = cls
	if attrs:
		attr_str = ''.join(' %s="%s"' % (attr, value)
						   for attr, value
						   in sorted(attrs.items()))
	else:
		attr_str = ''
	if content:
		return '\n'.join('<%s%s>%s</%s>' %
						 (name, attr_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attr_str)

# example 5-11
t = ('hello', 'world')
l = list(t)
print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', ('hello', 'world')))
print(tag('p', *('hello', 'world')))
print(tag('p', t))
print(tag('p', *t))
print(tag('p', l))
print(tag('p', *l))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name="img"))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))


