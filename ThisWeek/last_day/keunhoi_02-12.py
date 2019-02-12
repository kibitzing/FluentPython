#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p675-ch21end
# Example 21-16

"""
    예제 위주로 작성

"""

class EntityMeta(type):

	@classmethod
	def __prepare__(cls, name, bases):
		return collections.OrderedDict()

	def __init__(cls, name, bases, attr_dict):
		super().__init__(name, bases, attr_dict)
		cls._field_names = []
		for key, attr in attr_dict.items():
			if isinstance(attr, Validated):
				type_name = type(attr).__name__
				attr.storage_name = '_{}#{}'.format(type_name, key)
				cls._field_names.append(key)


class Entity(metaclass=EntityMeta):

	@classmethod
	def field_names(cls):
		for name in cls._field_names:
			yield name

# if __name__ == "__main__":
