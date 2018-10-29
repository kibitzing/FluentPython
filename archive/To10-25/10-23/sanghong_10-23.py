#!/usr/bin/envs python3
# -*- coding: utf-8 -*-

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_10_23_Fluent_Python
@Author Sanghong.Kim
오른손을 다쳐서 2손가락을 목요일 까지 사용하기 힘들다.
타이핑에 정말 오랜 시간이 걸려서 슬프다.
손목이 자꾸 꺽이는데 아프다...
"""

# Import Modules
import time
import os
import sys
import argparse
from collections import namedtuple
from dis import dis

Customer = namedtuple('Customer', 'name fidelity')

promos = []

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
        self.cart = list(cart)
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
        fmt = 'Order total: {:.2f}, due: {:.2f}'

        return fmt.format(self.total(), self.due())


def time_cal(program):
    # Started Time
    st=time.time()
    # Running Program
    print(program)
    # Ended Time
    et=time.time()
    # Running Time
    return et-st

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total * .07
    return 0

def best_promo(order):
    return max(promo(order) for promo in promos)

def main(args):
    print("Add Your Code Below")
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)

    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon',5,5.0)]

    print(Order(joe, cart,best_promo))
    print(Order(ann, cart,best_promo))

    dis(Order)



# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
