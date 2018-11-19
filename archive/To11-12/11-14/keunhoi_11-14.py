#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p307-311
'''
예제 코드가 예전 코드만 있어서, 이전 예제인 timefn 코드를 데코레이터로 작성하여 추가
'''

from array import array
import reprlib
import math
import functools
import operator
import itertools
from functools import wraps
import timeit

# import numpy as np
from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# 이건 왜 안 되었을까
# def timer(f):
# 	def wrapper(*args, **kwargs):
# 		import timeit
# 		start = timeit.default_timer()
# 		f
# 		end = timeit.default_timer()
# 		t = end - start
# 		print(t)
# 		# print(t)
# 		# print("{0}'s running  time is {1}".format(f().__name__(), t))
# 		return f()
# 	return wrapper

def timefn(fn):
	@wraps(fn)
	def measure_time(*args, **kwargs):
		start = timeit.default_timer()
		result = fn(*args, **kwargs)
		end = timeit.default_timer()
		print("@timefn: {} took {}".format(fn.__name__, end-start))
		return result
	return measure_time

class Vector:
	typecode = 'd'

	def __init__(self, components):
		self._components = array(self.typecode, components)

	# example 9-2 Vector2ddd 공개 속성의 예시
	# def __init__(self, x, y):
	# 	self.x = float(x)
	# 	self.y = float(y)

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

	# def __eq__(self, other):
	# 	if len(self) != len(other):
	# 		return False
	# 	for a, b in zip(self, other):
	# 		if a != b:
	# 			return false
	# 	return True

	def __eq__(self, other):
		return len(self) == len(other) and all(a == b for a, b in zip(self, other))

	def __hash__(self):
		hashes = map(hash, self._components)
		return functools.reduce(operator.xor, hashes)

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

	shortcut_names = 'xyzt'

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


	def angle(self, n):
		r = math.sqrt(sum(x*x for x in self[n:]))
		a = math.atan2(r, self[n-1])
		if (n == len(self) - 1 ) and (self[-1] < 0):
			return math.pi * 2 - a
		else:
			return a

	def angles(self):
		return (self.angle(n) for n in range(1, len(self)))

	def __format__(self, fmt_spec=''):
		if fmt_spec.endswith('h'):
			fmt_spec = fmt_spec[:-1]
			coords = itertools.chain([abs(self)], self.angles())
			outer_fmt = '<{}>'
		else:
			coords = self
			outer_fmt = '({})'
		components = (format(c, fmt_spec) for c in coords)
		return outer_fmt.format(', '.join(components))

	@property # property 와 timefn의 순서가 바뀌어서 작성되면 '<bound method...' 결과로 나타난다.
	@timefn
	def one_norm_reduce(self):
		return functools.reduce(lambda a,b: a+b, [element for element in self._components])

	@property
	@timefn
	def one_norm_sum(self):
		return sum(abs(element) for element in self._components)

	@property
	@timefn
	def two_norm_reduce(self):
		squred_components = (element **2 for element in self._components)
		result = functools.reduce(lambda a,b: a+b, squred_components)
		return result**(1/2)

	@property
	@timefn
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
# print(v3.visualize) # Should be fixed.
#
# print(v2.__format__(fmt_spec='h'))
# print(v3.__format__(fmt_spec='h'))
# print(v4.__format__(fmt_spec='h'))