#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p247-251
''''
학회에 와 있어서... 우선 예제완성코드 업로드 해 놓았습니다.
'''
# 9-1
# # 1-2 for review
import math
from array import array

class Vector:
	'''
	생각보다 스스로 사용할 수 있을 정도로 숙련되지 않은 부분..
	'''
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Vector(%r, %r)' % (self.x, self.y)

	def __abs__(self):
		return math.hypot(self.x, self.y)

	def __bool__(self):
		return bool(abs(self))

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)

print(help(Vector))
class Vector2d:
	typecode = 'd'

	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def __iter__(self):
		return (i for i in (self.x, self.y))

	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r}, {!r})'.format(class_name, *self)

	def __str__(self):
		return str(tuple(self))

	def __bytes__(self):
		return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

	def __eq__(self, other):
		return tuple(self) == tuple(other)

	def __abs__(self):
		return math.hypot(self.x, self.y)

	def __bool__(self):
		return bool(abs(self))


v1 = Vector2d(3,4)
print(v1.x, v1.y)
x,y = v1 # TypeError: 'Vector' object is not iterable
print('x, y = ', x,y)
v1
v1_clone = eval(repr(v1))
print('v1 == v1_clone :', v1 == v1_clone)
print(v1)
octets = bytes(v1)
print(octets)
print(abs(v1))
print(bool(v1), bool(Vector2d(0,0)))

print('='*50)

# 9-3
@classmethod
def frombytes(cls, octets):
	typecode = chr(octets[0])
	memv = memoryview(octets[1:]).cast(typecode)
	return cls(*memv)

# 9-4
class Demo:
	@classmethod
	def klassmeth(*args):
		return args

	@staticmethod
	def statmeth(*args):
		return args

Demo.klassmeth()
Demo.klassmeth('spam')
Demo.statmeth()
Demo.statmeth('spam')
