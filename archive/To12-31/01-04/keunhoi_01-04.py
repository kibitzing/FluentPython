#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p520-524
# Example 17-8~9

'''
   concurrent.futures.ThreadPoolExecutor 를 사용한 간단한 에제 시도.
'''

import concurrent.futures
import copy
import random
import time

NUMS = list(range(10**7))
NUMS2 = copy.deepcopy(NUMS)
random.shuffle(NUMS2)
NUMS_DICT = dict(zip(NUMS, NUMS2))

# Custom Example 1
def main1(): # 안 섞인 숫자 개수 구하기
	t1 = time.time()
	k = 0
	for i,j in NUMS_DICT.items():
			if i == j:
				k += 1
	t2 = time.time()
	del_t = t2-t1
	print('There are %s unchanged numbers' % k)
	print('Total time caculated by time.time() is', str(del_t))
	return k


# Custom Example 2
def main2(): # 안 섞인 숫자 개수 구하기
	t1 = time.time()
	with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executer:
		k = 0
		for i,j in NUMS_DICT.items():
				if i == j:
					k += 1
	t2 = time.time()
	del_t = t2-t1
	print('There are %s unchanged numbers' % k)
	print('Total time caculated by time.time() is', str(del_t))
	return k


if __name__ == '__main__':
	print('{0:=<50}'.format("Custom Example 1"))
	main1()


	print('{0:=<50}'.format("Custom Example 2"))
	main2()	# 별 차이 없음..

