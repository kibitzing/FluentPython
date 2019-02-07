# p637 ~ p641
# created by Jingu Kang on 01-29
# reference: Fluent Python by Luciano Ramalho

# very abstract version of LineItem

import abc
class AutoStorage: # this class does the most things that Quantity does
    __counter = 0
    def __init__(self):
        cls =self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return  getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

class Validated(abc.ABC, AutoStorage): #abstract clas
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
            """return validated value or raise ValueError"""

class Quantity(Validated):
    """ a number greater than zero"""
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0 ')
        return value

class NonBlank(Validated):
    """ a string with at least one non-space character """
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0 :
            raise ValueError('value cannot be empty or blank.')
        return value

class LineItem:
    descriptoin = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price ):
        self.descriptoin = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

hihi = LineItem('hello', 144, 12)
print(hihi.subtotal())
