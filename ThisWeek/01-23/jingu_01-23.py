# Created by Jingu Kang on 01-23
# reference: Fluent Python by Luciano Ramalho
# learned how to add docs to property, use vars, set getter and setter in a different way. 

class Foo:
    @property
    def bar(self):
        '''The bar attribute'''
        return self.__dict__['bar']

    @bar.setter
    def bar(self, value):
        self.__dict__['bar'] = value

def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]
    def qty_setter(instance, value):
        if value > 0 :
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)

class LineItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


nutmeg = LineItem('Moluccan nutmag', 8 , 13.4)
print(nutmeg.weight)
print(nutmeg.subtotal())
print(sorted(vars(nutmeg).items())) # [('description', 'Moluccan nutmag'), ('price', 13.4), ('weight', 8)]
