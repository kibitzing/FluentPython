#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#p224-228

# 8-5
t1 = (1,2, [30, 40])
t2 = (1,2, [30, 40])
print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(t1 == t2)

print('='*50)

l1 = [3, [55,44], (7,8,9)]
l2 = list(l1)
print(l2)
print(l2 == l1)
print(l2 is l1)

print('='*50)

# 8-6
l1 = [3, [66,55,44],(7,8,9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33,22]
l2[2] += (10,11)
print('l1:', l1)
print('l2:', l2)

# 8-8

class Bus:

	def __init__(self, passengers=None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = list(passengers)

	def pick(self, name):
		self.passengers.append(name)

	def drop(self, name):
		self.passengers.remove(name)

# 8-9
print('='*50)
import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))
bus1.drop('Bill')
print('bus2.passangers:', bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print('bus3.passangers:', bus3.passengers)

# custom example
# b는 a의 deepcopy이다. 그렇다면 이러한 b에다가 c라는 메모(변수)를 붙이면 어떻게 될까?
print('='*50)
a = [1,2,3,[4,5,6]]
b = copy.deepcopy(a)
c = b

print(id(a), id(b), id(c)) # 결과: c는 b의 얕은 복사. a의 깊은 복사에 얕은 복사를 겹칠 경우, 새로운 깊은 복사가 생기진 않음.
a[-1].append(7)
print('After a[-1].append(7), \na is : ', a), print('b is : ', b), print('c is : ', c)
print(id(a), id(b), id(c))