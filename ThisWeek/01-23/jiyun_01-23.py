# 원서 기준 612~616p

class Foo:

    @property
    def bar(self):
        '''The bar attribute'''
        return self.__dict__['bar']

    @bar.setter
    def bar(self, value):
        self.__dict__['bar'] = value

    def subtotal(self):
        return self.weight * self.price


class LineItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # 0이나 음수가 되지 않게 보장
        self.price = price


def quantity(storage_name):  # storage_name : 어디에 저장할 건지 결정

    def qty_getter(instance):
        # 메서드가 클래스 본체에 있지 않으므로 저장할 객체를 가리킴 (ex. LineItem 객체)
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('음수는 안돼요')

    return property(qty_getter, qty_setter)


if __name__ == '__main__':
    nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    print(nutmeg.weight, nutmeg.price)
    print(sorted(vars(nutmeg).items()))