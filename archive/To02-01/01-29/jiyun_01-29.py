## 프로퍼티 팩토리 사용 예제
def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    storage_name = '_{}:{}'.format('quantity', quantity.counter)

    def qty_getter(instance):
        return getattr(instance, storage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('음수 안돼요')

    return property(qty_getter, qty_setter)

## 리팩토링한 디스크립터 클래스 model_v5.py
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

    @abc.abstractclassmethod
    def validate(self, instance, value):
        """ 검증된 값을 반환하거나 ValueError를 발생시킨다 """


class Quantity(Validated):
    """ 0보다 큰 수 """

    def validate(self, instance, value):
        if value <= 0:
            raise ValueError("음수는 안돼요")
        return value


class NonBlank(Validated):
    """ 최소 하나 이상의 비공백 문자가 들어 있는 문자열 """

    def validate(self, inatance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('비어있거나 공백은 안돼요')
        return value

## 디스크립터를 사용한 LineItem
import model_v5 as model


class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

# >>> br_nuts = LineItem('Brazil nuts', 10, 34.95)
# >>> br_nuts.price
# 34.95