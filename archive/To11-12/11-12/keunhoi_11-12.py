#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p285-289
# 10-8 ~ 10-7
'''
visualize 3d 부분 차후 수정 예정
__getattr__() 사용 유의점
__setattr__() 을 사용한 수정
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

	def __getattr__(self, name): # 속성이 있는지, 그리고 __class__과 상속 클래스에 있는지 보고 나서 검색하는 거면, 속도 저하가 있지 않을까?
		cls = type(self)
		if len(name) == 1:
			pos = cls.shortcut_names.find(name)
			if 0 <= pos < len(self._components):
				return self._components[pos]

		msg = '{.__name__!r} object has no attribute {!r}'
		raise AttributeError(msg.format(cls, name))

	def __setattr__(self, name, value):
		cls = type(self)
		if len(name) == 1:
			if name in cls.shortcut_name:
				error = 'readonly attribute {atttr_name!r}'
			elif name.islower(): # 단일 소문자로 되어 있는 속성의 설정을 막음.
				error = "can't set attributes 'a' to 'z' in {cls_name!r}"
			else:
				error = ''
			if error:
				msg = error.format(cls_name=cls.__name__, attr_name=name)
				raise AttributeError(msg)
		super().__setattr__(name, value)


	@property
	def one_norm_reduce(self):
		import functools
		return functools.reduce(lambda a,b: a+b, [element for element in self._components])

	@property
	def one_norm_sum(self):
		return sum(abs(element) for element in self._components)

	@property
	def two_norm_reduce(self):
		import functools
		squred_components = (element **2 for element in self._components)
		result = functools.reduce(lambda a,b: a+b, squred_components)
		return result**(1/2)

	@property
	def two_norm_sum(self):
		return (sum(element**2 for element in self._components))**(1/2)

	@property
	def visualize(self):
		if len(self._components) == 1:
			error = "1-D vector needn't be visualized."
			raise ValueError(error)

		if len(self._components) == 2:
			plt.figure()
			plt.title('Visualized 2-D Vector')
			plt.xlim(-(self._components[0] + 3), self._components[0] + 3) # 사실 이 코드는 xlim과 ylim에 따라서 결과가 엉망진창으로 나오긴 함..
			plt.ylim(-(self._components[1] + 3), self._components[1] + 3) # ex: self._component[i]+3 = 0 인 경우
			ax = plt.axes()
			ax.arrow(0, 0, *(self._components[0], self._components[1]), head_width=0.1)
			plt.show()
			pass
		if len(self._components) == 3:
			# origin = [0, 0, 0]
			# X = np.arange(-(self._components[0] + 3), self._components[0] + 3, 0.25)
			# Y = np.arange(-(self._components[1] + 3), self._components[1] + 3, 0.25)
			# Z = np.arange(-(self._components[2] + 3), self._components[2] + 3, 0.25)
			# XX, YY, ZZ = np.meshgrid(X, Y, Z)
			#
			# fig = plt.figure()
			# ax = Axes3D(fig)
			# ax.set_title('Visualized 3-D Vector')
			#
			# plt.show()
			pass

		if len(self._components) >= 4:
			error = "4-D vector can't be visualized."
			raise ValueError(error)


	@classmethod
	def frombytes(cls, octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:].cast(typecode))
		return cls(memv)

v1 = Vector([1])
v2 = Vector(range(1,3))
v3 = Vector(range(1,4))
v4 = Vector(range(5))


print(v4.one_norm_sum)
print(v4.one_norm_reduce)
print(v4.two_norm_sum)
print(v4.two_norm_reduce)
# print(v4.visualize) # ValueError: 4-D vector can't be visualized.
# print(v1.visualize) # ValueError: 1-D vector needn't be visualized.
# print(v2.visualize) # Work fine
print(v3.visualize) # Should be fixed.