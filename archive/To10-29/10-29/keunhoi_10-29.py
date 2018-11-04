#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#p219-223

a = 1
b = a
a = 2
if b != 1:
	print('int b is changed.')

a = 1
b = a
a += 1
if b != 1:
	print('int b is changed.')

a = [1,2,3]
b = a
a.append(4)
if b != [1,2,3]:
	print('list b is changed.')

a = (1,2,[3,4])
b = a
a[2].append(5)
if b != (1,2,[3,4]):
	print('tuple b is changed.') # 튜플 안에서 결코 변경되지 않는 것은 튜플이 담고 있는 항목들의 정체성뿐이다.

class Gizmo:
	def __init__(self):
		print('Gizmo id: %d' % id(self))

Gizmo()
# Gizmo() * 10


charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis)
id(charles),id(lewis)
lewis['balance'] = 950
print(charles)

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print('alex == charles:', alex == charles)
print('alex is not charles:', alex is not charles) # 정체성은 다르다.

t1 = (1,2,[30,40])
t2 = (1,2,[30,40])
print(id(t1), id(t2))
