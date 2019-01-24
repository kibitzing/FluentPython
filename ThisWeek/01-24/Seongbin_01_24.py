class Foo:

    @property
    def bar(self):
        '''The bar attribute'''
        return self.__dict__['bar']

    @bar.setter
    def bar(self, value):
        self.__dict__['bar'] = value





class LineItem:
    def quantity(storage_name):
        def qty_getter(instance):
            return instance.__dict__[storage_name]

        def qty_setter(instance, value):
            if value > 0:
                instance.__dict__[storage_name] = value
            else:
                raise ValueError('value must be > 0')

        return property(qty_getter, qty_setter)

    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    weight = quantity('weight')

nutmeg = LineItem('Moluccan nutmeg',8,13.95)
print(nutmeg.weight, nutmeg.price)
print(sorted(vars(nutmeg).items()))

class BlackKnight:
    def __init__(self):
        self.members = ['an arm', 'another arm', 'a leg', 'another leg']
        self.phrases = ["'Tis but a scratch.", "It's just a flesh wound.", "I'm invincible!", "All right, we'll call it a draw."]

    @property
    def member(self):
        print('next member is:')
        return self.members[0]

    @member.deleter
    def member(self):
        text = 'BLACK KNIGHT (loses {})\n-- {}'
        print(text.format(self.members.pop(0), self.phrases.pop(0)))


knight = BlackKnight()
knight.member
del knight.member
del knight.member
del knight.member
del knight.member
