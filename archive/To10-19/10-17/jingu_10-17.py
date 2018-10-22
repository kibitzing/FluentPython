from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return  self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}'
        return fmt.format(self.total(), self.due())
    
    class Promotion(ABC):
        @abstractmethod
        def discount(self, order):
            """return discount"""
    
    class FidelityPromo(Promotion):
        def discount(self, order):
            return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0
    
    class BulkItemPromo(Promotion):
        def discount(self, order):
            discount = 0
            for item in order.cart:
                if item.quantity >= 20:
                    discount += item.total() * .1
            return discount
    class LargeOrderPromo(Promotion):
        def discount(self, order):
            distinct_items = {item.product for item in order.cart}
            if len(distinct_items) >= 10:
                return order.total() * 0.07
            return 0


jingu = Customer('Jingu Kang', 0)
daeha = Customer('Daeha Kim', 1200)
cart = [LineItem('banana', 4, .5),LineItem('apple',10,1.5), LineItem('watermelon',5, 5.0)]

print(Order(jingu, cart, Order.FidelityPromo()))
print(Order(daeha, cart, Order.FidelityPromo()))

banana_cart = [LineItem('banana', 30, .5),LineItem('apple',10,1.5), LineItem('watermelon',5, 5.0)]

print(Order(jingu, banana_cart, Order.BulkItemPromo()))

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

print(Order(jingu, long_order, Order.LargeOrderPromo()))
