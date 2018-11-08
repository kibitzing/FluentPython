#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p262-ch9end

'''
__slots__에 대해 배우지만, 실질적으로 쓰기에는 애매할 것으로 판단된다.
이후 타인의 코드에 __slots__이 나오는 경우에 당황하지 않을 듯하다.
'''

import math
from matplotlib import pyplot as plt
from array import array
# 9-6 custom

class Vector2d:
	# __slots__ = ('__x', '__y')

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

class ShortVector2d(Vector2d):
	typecode = 'f'


v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)
print(len(dumpd))
v1.typecode = 'f' # Vector2d에 __slots__의 주석처리를 풀면, type is read-only를 이유로 error를 뱉는다.
dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))
print(v1.typecode)
print(Vector2d.typecode)

sv = ShortVector2d(1/11, 1/27)
print(sv)
print(len(bytes(sv)))