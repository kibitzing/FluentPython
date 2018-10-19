#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
"""
    Created by Jingu Kang on 30/09/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.
    
    DESCRIPTION:
    
    """
from collections import namedtuple
import inspect
import jingu_promotions

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

def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

promos = [globals()[name] for name in globals() if name.endswith('_promo') and name != 'best_promo']
promos2 = [func for name, func in inspect.getmembers(jingu_promotions, inspect.isfunction)]

def best_promo(order):
    return max(promo(order) for promo in promos)

def best_promo2(order):
    return max(promo(order) for promo in promos2)


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
print('if buy with large order promo:',Order(jingu, food_cart, large_order_promo))
print('if buy with fidelity promo:',Order(jingu, food_cart, fidelity_promo))
print('if buy with best promo:' ,Order(jingu, food_cart, best_promo))
print('if buy with best promo2:' ,Order(jingu, food_cart, best_promo2))

print(better_person_to_buy(jingu, sanghong, cart), 'should buy this')

print("promos:" ,promos)
print("promos2:", promos2)
print("promos==promos2:", promos==promos2)
# False
print('try it with set')
print("promos==promos2:", {i for i in promos}=={j for j in promos2})
# 여전히 False 왜냐하면 다른 곳에 정의되어 있기 때문, promos 는 여기에 함수로, promos2 는 jingu_promotions에
