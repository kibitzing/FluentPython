#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p352-356 (actually 352)
# Example 12-5 ~ 8
'''
__setitem__과 collections.UserDict에 대한 내용. + 클래스 상속
'''

import numbers
import io
import numpy
import tensorflow

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

def print_mro(cls):
	print(', '.join(c.__name__ for c in cls.__mro__))
def main():

	d = D()
	d.ping()
	d.pong()
	d.pingpong()
	C.pong(d)
	print(bool.__mro__)

	print_mro(bool)
	print_mro(numbers.Integral)
	print_mro(io.BytesIO)
	print_mro(numpy.bool)
	# print_mro(numpy.array()) # TypeError: Required argument 'object' (pos 1) not found
	# print_mro(tensorflow.layers) # AttributeError: module 'tensorflow._api.v1.layers' has no attribute '__mro__'

if __name__ == '__main__':
	main()
