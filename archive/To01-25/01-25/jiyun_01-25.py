class Quantity:
    # 디스크립터 클래스
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        # self : 디스크립터 객체
        # instance : 관리 대상 객체
        # value : 할당할 값
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('음수는 안돼요')


class LineItem:
    # 관리 대상 클래스
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
        # 디스크립터 객체가 각각 weight, price 속성에 바인딩

    def subtotal(self):
        return self.weight * self.price
