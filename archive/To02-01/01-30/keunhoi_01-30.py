#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p640-644
# Example 20-8

"""
	예제 위주로 작성
	프로퍼티 문서화

"""

# Example 20-8
def cls_name(obj_or_cls):
	cls = type(obj_or_cls)
	if cls is type:
		cls = obj_or_cls
	return cls.__name__.split('.')[-1]

def display(obj):
	cls = type(obj)
	if cls is type:
		return '<class {}>'.format(obj.__name__)
	elif cls in [type(None), int]:
		return repr(obj)
	else:
		return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
	pseudo_args = ', '.join(display(x) for x in args)
	print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))

class Overriding:

	def __get__(self, instance, owner):
		print_args('get', self, instance, owner)

	def __set__(self, instance, value):
		print_args('set', self, instance, value)

class OverridingNoGet:

	def __set__(self, instance, value):
		print_args('set', self, instance, value)

class NonOverriding:

	def __get__(self, instance, owner):
		print_args('get', self, instance, owner)

class Managed:
	over = Overriding()
	over_no_get = OverridingNoGet()
	non_over = NonOverriding()

	def spam(self):
		print('-> Managed.spam({})'.format(display(self)))

# if __name__ == "__main__":