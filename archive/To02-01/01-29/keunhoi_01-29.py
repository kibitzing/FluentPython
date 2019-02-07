#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p635-639
# Example 20-3~5

"""
  예제 위주로 작성
"""

# Example 20-3
class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)
            
    def __set__(self, instance, val):
        if val > 0:
            setattr(instance, self.storage_name, val)
        else:
            raise ValueError('value must be > 0')


# Example 20-4
import model_v4c as model


class LineItem:
    weight = model.Quantity()
    price = model.Quantity()
    
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


# Example 20-5
def quantity():
    try:
        quantity.counter += 1
    except AttibuteError:
        quantity.counter = 0
        
    storage_name = '_{}:{}'.format('quantity', quantity.counter)
    
    def qty_getter(instance):
        return getattr(instance, storage_name)
    
    def qty_setter(instance, val):
        if val > 0:
            setattr(instance, storage_name, val)
        else:
            raise ValueError('value must be > 0 ')
            
    return property(qty_getter, qty_setter)
        

# if __name__ == "__main__":
