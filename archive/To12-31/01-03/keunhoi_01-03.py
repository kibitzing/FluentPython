#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p515-519
# Example 17-6~(7)

'''
   예제 위주 작성
'''

# Example 17-6
from time import sleep, strftime
from concurrent import futures

def display(*args):
	print(strftime('[&H:&M:&S]'), end=' ')
	print(*args)

def loiter(n):
	msg = '{}loiter({}): doing nothing for {}s...'
	display(msg.format('\t'*n, n, n))
	sleep(n)
	msg = '{}loiter({}): done.'
	display(msg.format('\t'*n, n))
	return n * 10

def main_176():
	display('Script starting.')
	executor = futures.ThreadPoolExecutor(max_workers=3)
	results1 = executor.map(loiter, range(5))
	display('results:', results1)
	display('Waiting for individual results:')
	for i, result in enumerate(results1):
		display('result {}: {}'.format(i, result))

	results2 = executor.map(loiter, range(10))
	display('results:', results2)
	display('Waiting for individual results:')
	for i, result in enumerate(results2):
		display('result {}: {}'.format(i, result))

	results3 = executor.map(loiter, (1,2,3,4,10,11,22,33))
	display('results:', results3)
	display('Waiting for individual results:')
	for i, result in enumerate(results3):
		display('result {}: {}'.format(i, result))



if __name__ == '__main__':
	print('{0:=<50}'.format("Example 17-6"))
	main_176()
