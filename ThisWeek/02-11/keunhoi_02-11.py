#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p670-674
# Example 21-14~15

"""
    예제 위주로 작성

"""

import model_v7 as model

class LineItem(model.Entity):
	description = model.NonBlank()
	weight = model.Quantity()
	price = model.Quantity()

	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price

class EntityMeta(type):

	def __init__(cls, name, bases, attr_dict):
		super().__init__(name, bases, attr_dict)
		for key, attr in attr_dict.items():
			if isinstance(attr, Validated):
				type_name = type(attr).__name__
				attr.storage_name = '_{}#{}'.format(type_name, key)

class Entity(metaclass=EntityMeta):


# if __name__ == "__main__":
