#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p347-351 (actually 352)
# Example 12-1 ~ 5
'''
__setitem__과 collections.UserDict에 대한 내용. + 클래스 상속
'''

import collections

class DoppelDict(dict):
	def __setitem__(self, key, value):
		super().__setitem__(key, [value] * 2)

class AnswerDict(dict):
	def __getitem__(self, key):
		return 42

class DoppelDict2(collections.UserDict):
	def __setitem__(self, key, value):
		super().__setitem__(key, [value] * 2)

class whatdidyouchoose(collections.UserDict):
	def __getitem__(self, key):
		if key in self:
			if type(key) == int:
				print('You choose a number.')
			if type(key) == str:
				print('You choose a character.')
		else:
			print('Please choose a key in your dict.')

class A:
	def ping(self):
		print('ping:', self)

class B(A):
	def pong(self):
		print('pong:', self)

class C(A):
	def pong(self):
		print('PONG:', self)

class D(B, C):

	def ping(self):
		super().ping()
		print('post-ping:', self)

	def pingpong(self):
		self.ping()
		super().ping()
		self.pong()
		super().pong()
		C.pong(self)

def main():
	dd = DoppelDict(one=1)
	print(dd)
	dd['two'] = 2
	print(dd)
	dd.update(three=3)
	print(dd)

	ad = AnswerDict(a='foo')
	print(ad['a'])
	d = {}
	d.update(ad)
	print(d['a'])
	print(d)

	dd = DoppelDict2(one=1)
	print(dd)
	dd['two'] = 2
	print(dd)
	dd.update(three=3)
	print(dd)

	d = D()
	d.pong()
	C.pong(d)
	print(D.__mro__)

	d = {'a':1, 'b':2, 2:4, 4:6,}
	wdy = whatdidyouchoose(d)
	wdy['a']
	wdy[2]
	wdy[99]


if __name__ == '__main__':
	main()
