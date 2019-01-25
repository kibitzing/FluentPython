#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p625-629
# Example 20-1

"""
	예제 위주로 작성
	프로퍼티 문서화

"""

# Example 20-1
class Quantity:

	def __init__(self):
		self.storage_name = storage_name

	def __set__(self, instance, value):
		if value > 0:
			instance.__dict__[self.storage_name] = value
		else:
			raise ValueError('value must be > 0')

class LineItem:
	weight = Quantity('weight')
	price = Quantity('price')

	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price


# if __name__ == "__main__":