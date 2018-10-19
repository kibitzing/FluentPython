"""
    creatd by Jingu Kang on 10-18
"""

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
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:2f} due: {:2f}>'
        return fmt.format(self.total(), self.due())

def fidelity_promo(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_prom(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

promos = [fidelity_promo, bulk_item_promo, large_order_prom]

def best_promo(order):
    return max(promo(order) for promo in promos)

def better_person_to_buy(p1, p2, cart):
    order1 = Order(p1, cart, best_promo)
    order2 = Order(p2, cart, best_promo)
    if order1.due() < order2.due():
        return p1[0]
    else:
        return p2[0]

jingu = Customer('Jingu Kang', 1200)
sanghong = Customer('Sanghong Kim', 600)
cart = [LineItem('Macbook', 2, 2000), LineItem('iMac', 3, 1500), LineItem('Surface', 3, 2200)]
print('if jingu buy:' , Order(jingu, cart, fidelity_promo))
print('if sanghong buy:', Order(sanghong, cart, fidelity_promo))

MicroSoftStore = [LineItem('Window10', 100, 100), LineItem('window7', 19, 80)]
print('if buy with fidelity promo:', Order(jingu, MicroSoftStore, fidelity_promo))
print('if buy with bulk promo:', Order(jingu, MicroSoftStore, bulk_item_promo))

food_list = ['banana', 'apple', 'rice', 'cherry', 'strawberry', 'grape', 'egg', '김치찌개', '된장찌개','삼겹살','부대찌개']
food_cart = [LineItem(food, 2, 1) for food in food_list]
print('if buy with large order promo:',Order(jingu, food_cart, large_order_prom))
print('if buy with fidelity promo:',Order(jingu, food_cart, fidelity_promo))
print('if buy with best promo:' ,Order(jingu, food_cart, best_promo))

print(better_person_to_buy(jingu, sanghong, cart), 'should buy this')
