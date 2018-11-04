#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p234-ch.8
# + 10/31 assignment

'''
제주도에 놀러갈 겸, 조그마한 학회 포스터를 준비하다가 어제는 도저히 시간이 안 났네요 ㅎㅎ..
오늘 어제 분량까지 포함하여 작성했습니다.
'''

# 8-11
# 함수는 전달받은 가변 객체를 수정할 수 있다.
print('='*50)

def f(a,b):
	a += b
	print(a)
	return a

x, y = 1, 2
f(x,y)
a = [1,2]
b = [3,4]
f(a,b)

print(a,b)
t = (10,20)
u = (30,40)
f(t,u)
print(t,u)

# 8-12
# 그렇기 때문에 가변의 빈 리스트를 인자로 정하게 되면, 동일한 인자를 공유하게 되는, 그야말로
# 디버깅하기도 어려운 오류를 내재한 코드가 되어버린다.

print('='*50)
class HauntedBus:

	def __init__(self, passengers=[]):
		self.passengers = passengers
		print('Initial passengers are :', self.passengers)

	def pick(self, name):
		self.passengers.append(name)
		print('After pick %s, passengers are : ' % name,self.passengers)

	def drop(self, name):
		self.passengers.remove(name)
		print('After drop %s, passengers are : ' % name, self.passengers)

bus1 = HauntedBus(['Alice', 'Bill'])
bus1.passengers
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)

bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick('Dave')
print(bus2.passengers)
print('bus2.passengers is bus3.passengers : ', bus2.passengers is bus3.passengers)
print(bus1.passengers)

# 8-14,15

print('='*50)

class Twilightbus:
	"""
	승객이 사라지게 만드는 버스 모델
	"""

	def __init__(self, passengers=None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = passengers

	def pick(self,name):
		self.passengers.append(name)

	def drop(self,name):
		self.passengers.remove(name)

python_team = ['jingu','daeha','keunhoi','sanghong','seongbin','jiyun','seonghyun']
bus = Twilightbus(python_team)
bus.drop('jingu')
bus.drop('keunhoi')
print(python_team)

# 8-16
print('='*50)

import weakref
s1 = {1,2,3}
s2 = s1

def bye():
	print('Gone with the wind...')

ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
print(ender.alive)

s2 = 'spam'
print(s2)
print(ender.alive)

# 8-17
# 약한 참조
print('='*50)

a_set = {0,1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2,3,4}
# print(wref()) # 왜 이게 none 이 나오지? 이걸 주석처리해도 None이 나오네..
print(wref() is None)
print(wref() is None)

# 8-18,19
print('='*50)

class Cheese:

	def __init__(self, kind):
		self.kind = kind

	def __repr__(self):
		return 'Cheese(%r)' % self.kind


import weakref

stock = weakref.WeakValueDictionary()

catalog = [Cheese('Red Leicester'), Cheese('Parmasan'), Cheese('Tilsit'), Cheese('Brie')]

for cheese in catalog:
	stock[cheese.kind] = cheese

print(sorted(stock.keys()))

del catalog
print(sorted(stock.keys()))

del cheese
print(sorted(stock.keys()))

# 8-20
print('='*50)

t1 = (1,2,3)
t2 =tuple(t1)
print('t2 is t1 : ', t2 is t1)

t3 = t1[:]
print('t3 is t1 : ', t3 is t1)

# 8-20
print('='*50)

t1 = (1, 2, 3)
t3 = (1, 2, 3)
print('t3 is t1 : ', t3 is t1)

s1 = 'ABC'
s2 = 'ABC'
print('s2 is s1 : ', s2 is s1)

