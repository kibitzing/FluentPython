# Created by Jingu Kang on 01-25
# reference: Fluent Python by Luciano Ramalho
# tried to implement __get__ as well, need more study :)

# applying functional programming patterns to avoid repetitive coding


class Quantity: #protocol based feature
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0 :
            print('hi setting, ', value)
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')

    def __get__(self, obj, cls):
        print("You've got everything.")
        return 12

class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

raisins = LineItem('Golden raisins', 10, 8)
print(raisins.subtotal())

# truffle = LineItem('White truffle', 100,0)
# print(truffle)
