#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p312-316

'''
생각한 숫자 맞추기 놀이
'''
from random import shuffle

number_guest = 7
number_chance = 10

for i in range(number_chance):
	l = list(range(20))
	shuffle(l)
	if l[0] == number_guest:
		if i == 0:
			fmt = 'Your {0}st Guess is Correct.'
		elif i == 1:
			fmt = 'Your {0}nd Guess is Correct.'
		elif i == 2:
			fmt = 'Your {0}rd Guess is Correct.'
		else:
			fmt = 'Your {0}th Guess is Correct.'
		print(fmt.format(i+1))
		break
	else:
		if i == (number_chance-1):
			print('All of Your Guess Fails')

