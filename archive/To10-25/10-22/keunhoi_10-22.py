#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#p183~187

# 핵심 특징: 정의된 직후 실행, 즉 임포트 타임에 실행.
def deco(func):
	def inner():
		print('running inner()')
	return inner()

@deco
def target1():
	print('running target()')

# 번역본 코드
@deco
def target2():
	print('running target()')

def target3():
	print('running target()')

# ===============================================================
registry = []

def register(func):
	print('running register(%s)' % func)
	registry.append(func)
	return func

@register
def f1():
	print('running f1()')

@register
def f2():
	print('running f2()')

def f3():
	print('running f3()')

def main():
	print('running main()')
	print('registry ->', registry)
	f1()
	f2()
	f3()

# ===============================================================

promos = []

def promotion(promo_func):
	promos.append(promo_func)
	return promo_func

@promotion
def fidelity(order):
	"""충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인 적용
	"""
	print('fidelity promotion is applied')
	return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
	"""20개 이상의 동일 상품을 구입하면 10% 할인 적용
	"""
	discount = 0
	for item in order.cart:
		if item.quantity >= 20:
			discount += item.total()
	print('bulk_item promotion is applied')
	return discount

@promotion
def large_order(order):
	"""10 종류 이상의 상품을 구입하면 전체 7% 할인 적용
	"""
	distinct_items = {item.product for item in order.cart}
	if len(distinct_items) >= 10:
		return order.total() * .07
	print('large_order promotion is applied')
	return 0

def best_promo_example(order):
	"""최대로 할인 받을 금액을 반환한다.
	"""
	return max(promo(order) for promo in promos)

def best_promo(order):
	"""최대로 할인 받을 금액을 반환한다.
	"""
	bestpromo_index = list(promo(order) for promo in promos).index(max(list(promo(order) for promo in promos)))
	return {promos[bestpromo_index].__name__ : max(promo(order) for promo in promos)}


if __name__ == '__main__':
	main()