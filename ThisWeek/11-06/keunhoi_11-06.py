#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p257-261

'''
Hashable
'''

import datetime
import math
from matplotlib import pyplot as plt


# 9-4

class Demo:
	@classmethod
	def klassmeth(*args):
		return args

	@staticmethod
	def statmeth(*args):
		return args

print(Demo.klassmeth())
print(Demo.klassmeth('spam'))
print(Demo.statmeth())
print(Demo.statmeth('spam'))

print("="*50)

br1 =1/2.43
print(format(br1, '0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=br1))

print("="*50)
now = datetime.datetime.now()
format(now, '%H%M%S')
print("It's now {:%I:%M %p}".format(now))



# 9-6 custom

class Vector2d:

	typecode = 'd'

	def __init__(self, x, y):
		self.__x = float(x)
		self.__y = float(y)

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	@property
	def angle(self):
		return math.atan2(self.y, self.x)

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

	def __format__(self, fmt_spec=''):
		if fmt_spec.endswith('p'):
			fmt_spec = fmt_spec[:-1]
			coords = (abs(self), self.angle())
			outer_fmt = '<{}, {}>'
		else:
			coords = self
			outer_fmt = '({}, {})'
		components = (format(c, fmt_spec) for c in coords)
		return outer_fmt.format(*components)

	def __hash__(self):
		return hash(self.x) ^ hash(self.y)

	@property
	def visualize(self):
		plt.figure()
		plt.title('Visualized Vector')
		plt.xlim(-(self.x+3), self.x+3)
		plt.ylim(-(self.y+3), self.y + 3)
		ax = plt.axes()
		ax.arrow(0,0,*(self.x,self.y),head_width=0.1)
		plt.show()

	@classmethod
	def frombytes(cls, octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(*memv)

v1 = Vector2d(3,4)
v2 = Vector2d(3.1,4.2)
print(hash(v1))
print(hash(v2))
vectors = set([v1,v2])
print(vectors)
