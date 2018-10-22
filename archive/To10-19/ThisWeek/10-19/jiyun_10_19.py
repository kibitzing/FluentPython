# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:19:16 2018

@author: DMSL-6
"""


from collections import namedtuple

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
    
def Point_promo(order): #적립금 사용 2000원 부터 가능
    if order.customer.point >= 2000:
        discount = order.customer.point
    else:
        discount = 0
    return discount

def total_promo(order): #50000원 이상 구매시 배송비 차감
    if order.total() >= 50000:
        discount = 2500
    else: 
        discount = 0
    return discount


def oneplusone_promo(order): # 특정 상품 1+1 이벤트
    for item in order.cart:
        if item.product == 'white tshirt':
            if item.quantity >= 2:   
                discount = item.price
    return discount


promos = [globals() [name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo']

def best_promo(order):
    return max(promo(order) for promo in promos)

Park = Customer('python',3000)
Kim = Customer('fluent',100)
cart = [LineItem('Blue Tshirt',1,20000), LineItem('Pants',1, 20000), LineItem('white tshirt',2,5000)]

print(Order(Park, cart, best_promo)) #<Order total : 52500 due: 50000>


##############################################################
class MacroCommand:

	def __init__(self, commands):
		self.commands = list(commands)

	def __call__(self):
		for command in self.commands:
			command(3000)

def pointOX(input):
    if input >= 2000:
        print("적립금을 사용하실 수 있습니다.")
    return input

command = [pointOX]

print(MacroCommand(command) ) # <__main__.MacroCommand object at 0x000001FDC4CF62B0>
M = MacroCommand(command) 
M() #적립금을 사용하실 수 있습니다.




