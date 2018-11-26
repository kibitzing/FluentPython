#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p357-361
# Example 12-8
'''
	좀 더 큰 다이아몬드 상속 문제 실험
				A
			B		C
		D		E		F
			G		H
				I
'''



class A:
	def greeting(self):
		print('Hello by greeting A', self)
		return 'A'

class B(A):
	def greeting(self):
		super().greeting()
		print('Hello by greeting B:', self)
		return 'B'

class C(A):
	def greeting(self):
		super().greeting()
		print('Hello by greeting C:', self)
		return 'C'

class D(B):

	def greeting(self):
		super().greeting()
		print('Hello by greeting D:', self)
		return 'D'

class E(B, C):
	def greeting(self):
		super().greeting()
		print('Hello by greeting E:', self)
		return 'E'

class F(C):
	def greeting(self):
		super().greeting()
		print('Hello by greeting F:', self)
		return 'F'

class G(D,E):
	def greeting(self):
		super().greeting()
		print('Hello by greeting G:', self)
		return 'G'

class H(E,F):
	def greeting(self):
		super().greeting()
		print('Hello by greeting H:', self)
		return 'H'

class I(G,H):
	def greeting(self):
		super().greeting()
		print('Hello by greeting I:', self)
		return 'I'

def print_mro(cls):
	print(', '.join(c.__name__ for c in cls.__mro__))

def main():

	print(A().greeting())
	print(B().greeting())
	print(C().greeting())
	print(D().greeting())
	print(E().greeting())
	print(F().greeting())
	print(G().greeting())
	print(H().greeting())
	print(I().greeting())

	print('='*50)
	print_mro(A)
	print_mro(B)
	print_mro(C)
	print_mro(D)
	print_mro(E)
	print_mro(F)
	print_mro(G)
	print_mro(H)
	print_mro(I)

if __name__ == '__main__':
	main()
