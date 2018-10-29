# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:15:31 2018

@author: jiyun
"""

from collections import namedtuple
from datetime import datetime

year = datetime.today().year        
month =datetime.today().month      
day = datetime.today().day      

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

promos = []

Customer = namedtuple('ID','name point')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
        
    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion = None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

        
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total + 2500
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else :
            discount = self.promotion(self)
        return self.total() - discount + 2500
    
    def __repr__(self):
        fmt = '<Order total : {:d} due: {:d}>'
        return fmt.format(self.total(), self.due())
    
@promotion    
def Point_promo(order): #적립금 사용 2000원 부터 가능
    if order.customer.point >= 2000:
        discount = order.customer.point
    else:
        discount = 0
    return discount
@promotion   
def total_promo(order): #50000원 이상 구매시 배송비 차감
    if order.total() >= 50000:
        discount = 2500
    else: 
        discount = 0
    return discount

@promotion   
def oneplusone_promo(order): # 특정 상품 1+1 이벤트
    for item in order.cart:
        if item.product == 'white tshirt':
            if item.quantity >= 2:   
                discount = item.price
    return discount

@promotion
def event_promo(order): ### 그냥 이벤트 ###
    if((year == 2018) and (month == 10) and (day == 23)):
        discount = 20000
    else:
        discount = 0
    return discount


def best_promo(order):
    return max(promo(order) for promo in promos)


Park = Customer('python',3000)
Kim = Customer('fluent',100)
cart = [LineItem('Blue Tshirt',1,20000), LineItem('Pants',1, 20000), LineItem('white tshirt',2,5000)]

print(Order(Park, cart, best_promo)) #<Order total : 52500 due: 35000>

###############################################################################
b = 5
def f1(a):
    global b
    print(a)
    print(b)
    b=9
f1(3) #3,5
print(b) #9
f1(3) #3,9

###############################################################################

class Averager():
    
    def __init__(self):
        self.series = []
        
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)
    
avg = Averager()

for i in range(11):
    print(avg(i))
  





