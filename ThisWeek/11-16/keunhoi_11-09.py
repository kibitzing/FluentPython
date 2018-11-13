#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p280-284
# 10-4 ~ 10-7
'''
visualize 부분을 2d 3d로 차후 수정 예정
'''

from array import array
import reprlib
import math
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Vector:
	typecode = 'd'

	def __init__(self, components):
		self._components = array(self.typecode, components)
		# print('self._components is :', self._components)
		# print('len of self._components is :', len(self._components))

	def __iter__(self):
		return iter(self._components)

	def __repr__(self):
		components = reprlib.repr(self._components)
		components = components[components.find('['):-1]
		return 'Vector({})'.format(components)

	def __str__(self):
		return 'Vector({})'.format(str(list(self))) # replace 'tuple' in 11-08 sanghong's code
		# return str(tuple(self))

	def __bytes__(self):
		return (bytes([ord(self.typecode)]) +
				bytes(self._components))

	def __eq__(self, other):
		return tuple(self) == tuple(other)

	def __abs__(self):
		return math.sqrt(sum(x * x for x in self))

	def __bool__(self):
		return bool(abs(self))

	def __len__(self):
		return len(self._components)

	def __getitem__(self, index):
		import numbers
		cls = type(self)
		print(cls)
		if isinstance(index, slice):
			return cls(self._components[index])
		elif isinstance(index, numbers.Integral):
			return self._components[index]
		else:
			msg = '{cls.__name__} indices must be integers'
			raise TypeError(msg.format(cls=cls))

	@classmethod
	def frombytes(cls, octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:].cast(typecode))
		return cls(memv)

v1 = Vector([3, 4, 5])
v2 = Vector([-4, 3])
print(len(v1))
print(v1[0], v1[-1])
v7 = Vector(range(7))
print(v7[1:4])


