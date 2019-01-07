#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p525-ch17end
# Example 17-12~14

'''
	concurrent 문서 참고.
'''

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import copy
import random
import time

t1 = time.time()
NUMS = list(range(10**7))
t2 = time.time()
print('Total time caculated by time.time() is', str(t2 - t1))

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
	print('There are %s unchanged numbers' % k)
	print('Total time caculated by time.time() is', str(t2-t1))
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
	print('{0:=<50}'.format("Custom Example"))
	main1()

	with ThreadPoolExecutor(max_workers=5) as executor:
		future = executor.submit(list, range(10**7))
		t1 = time.time()
		print(future.result())
		t2 = time.time()
		print('Total time caculated by time.time() is', str(t2-t1))

	with ProcessPoolExecutor(max_workers=5) as executor:
		future = executor.submit(list, range(10**7))
		t1 = time.time()
		print(future.result())
		t2 = time.time()
		print('Total time caculated by time.time() is', str(t2 - t1))