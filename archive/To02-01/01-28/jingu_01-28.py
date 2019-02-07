# Created by Jingu Kang on 01-28
# reference: Fluent Python by Luciano Ramalho
# ~page 636

# applying functional programming patterns to avoid repetitive coding

class Quantity:
    __counter = 0  # class attribute of Quantity, counting the number of Quantity

    def __init__(self):
        cls = self.__class__  # reference to Quantity Class
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)  # unique because of index
        cls.__counter += 1

    def __get__(self, instance, owner):  # the name of the managed attribute is not the same as the storage_name.
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()
    price = Quantity()

    # 원래는 이랬음.
    #    weight = Quantity('weight')
    #    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

print(LineItem.weight)
coconuts = LineItem('Brazilian coconut', 20, 18.25)
print(coconuts.weight, coconuts.price)

raisins = LineItem('Golden raisins', 10, 8)
print(getattr(raisins,'_Quantity#0'), '*',getattr(raisins,'_Quantity#1'),'=', raisins.subtotal())
