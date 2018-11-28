#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p362-ch12end
#
'''
상속 사용한 에제
'''

class Databook(object):

	def __init__(self, d=None):
		if d == None:
			self._data = {}
		else:
			self._data = d

	def append_data(self, key, val):
		self._data.update({key:val})
		return self._data

	def pick_value_by_key(self, key):
		return self._data[key]

	def pick_key_by_value(self, val):
		keys = set()
		for k, v in self._data.items():
			if v == val:
				keys.update([k]) # k로만 하면 TypeError: 'int' object is not iterable
		return keys

	def remove_by_key(self, key):
		del self._data[key]
		return self._data

	def remove_by_value(self, val):
		Keys = []
		for k, v in self._data.items():
			if v == val:
				# del self._data[k] # RuntimeError: dictionary changed size during iteration
				Keys.append(k)
		for i in range(len(Keys)):
			del self._data[Keys[i]]

		return self._data

class Databook2(Databook):

	def find_number_of_same_value(self):
		D = {}
		inv_d = {v:k for k,v in self._data.items()}
		D.update(inv_d)
		if len(D) != len(self._data):
			return len(self._data) - len(D)
		else:
			return 0

if __name__ == '__main__':
	d = {1:2, 2:4, 3:6,4:8, 5:10, 6:10, 7:8, 8:6, 9:4, 10:2}
	Databook(d)
	print(Databook(d)._data)
	print(Databook(d).append_data(11, 12))
	print(Databook(d).pick_value_by_key(2))
	print(Databook(d).pick_key_by_value(10))
	print(Databook(d).remove_by_key(3))
	print(Databook(d).remove_by_value(10))
	print(Databook2(d).find_number_of_same_value())
	print(Databook2(d).remove_by_value(2))




