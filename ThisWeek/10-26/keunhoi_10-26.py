#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#p203~ch7end
'''
memo:
데코레이터를 사용해서 기존에 쓰던 vgg16 모델을 꾸며보려고 했는데, 에러도 에러지만, 어디를 어떻게 고쳐봐야할지 감이 안 잡힌다.
이후 코드 작성하는 과정 중에서 다시 한 번 시도해봐야 할 것 같다.
'''
# examples in book
from functools import singledispatch
from collections import abc
import numbers
import html

# ===============================================================
@singledispatch
def htmlize(obj):
	content = html.escape(repr(obj))
	return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
	content = html.escape(text).replace('\n', '\<br>\n')
	return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
	return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li' + inner + '</li>\n<ul>'

# ===============================================================
registry = set()

def register(active=True):
	def decorate(func):
		print('running register(active=%s)->decorate(%s)' % (active, func))
		if active:
			registry.add(func)
		else:
			registry.discard(func)

		return func
	return decorate

@register(active=False)
def f1():
	print('running f1()')

@register()
def f2():
	print('running f2()')

def f3():
	print('running f3()')
# ===============================================================
def main():
	print(htmlize(1))
	print(htmlize('apple'))
	print('='*50)

	print('running main()')
	print('registry ->', registry)
	f3()
	print('='*50)


if __name__ == '__main__':
	main()
