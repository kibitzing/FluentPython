#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 프로퍼티 속성을 이용한 예제

"""
import abc


class AutoStorage:
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
        
    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)
        
        
class Validated(abc.ABC, AutoStorage):
    
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)
        
    @abc.abstractmethod
    def validate(self, instance, value):
        """return validated value or raise ValueError"""
        
        
class Quantity(Validated):
    """a number greater than zero"""
    
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('[INFO] value must be > 0')
        return value
    
    
class NonBlank(Validated):
    """a string with at least one non-space character"""
    
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('[INFO] value cannot be empty or blank')
        return value


###    
class LineItem:
    description = NonBlank()
    weight = Quantity()
    price = Quantity()
    
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
        
    def subtotal(self):
        return self.weight * self.price
    

coconuts = LineItem('', 20, 17.95)  # ValueError: [INFO] value cannot be empty or blank
coconuts = LineItem('Brazilian coconut', -20, 17.95)  # ValueError: [INFO] value must be > 0

coconuts = LineItem('Brazilian coconut', 20, 17.95)
print(coconuts.description, coconuts.weight, coconuts.price)  # Brazilian coconut 20 17.95