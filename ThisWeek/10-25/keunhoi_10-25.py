#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#p198~202
import time
import tracemalloc
from functools import wraps, lru_cache
import html
# ===============================================================
def clock(func):
	@wraps(func)
	def clocked(*args, **kwargs):
		t0 = time.perf_counter() #perf_counter과 예제에 나온 time.time()은 다른 결과 값을 가진다.
		result = func(*args, **kwargs)
		elapsed = time.perf_counter() - t0
		name = func.__name__
		arg_lst = []
		if args:
			arg_lst.append(', '.join(repr(arg) for arg in args))
		if kwargs:
			pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
			arg_lst.append(', '.join(pairs))
		arg_str = ', '.join(arg_lst)
		print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
		return result
	return clocked

def memory(func):
	@wraps(func)
	def memory_checked(*args, **kwargs):
		result = func(*args, **kwargs)
		result_memory = tracemalloc.get_traced_memory(result)
		name = func.__name__
		arg_str = ', '.join(repr(arg) for arg in args)
		print('[%0.8fs] %s(%s) -> %r' % (result_memory, name, arg_str, result))
		return result
	return memory_checked

@clock
def snooze(seconds):
	time.sleep(seconds)

@clock
# @memory
def factorial(n):
	return 1 if n<2 else n*factorial(n-1) # 내가 시도한 memory는 데코레이터로 사용이 불가했다. (TypeError: get_traced_memory() takes no arguments (1 given))

@lru_cache()
@clock
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-2) + fibonacci(n-1)

def htmlize(obj):
	content = html.escape(repr(obj))
	return '<pre>{}<pre>'.format(content)

# ===============================================================
def main():
	print('*' * 40, 'Calling snooze(.321)')
	snooze(.321)
	print('*' * 40, 'Calling factorial(6)')
	factorial(4)
	print('*' * 40, 'Calling fibonacci(6)')
	fibonacci(6)
	print(htmlize('hello'))

if __name__ == '__main__':
	main()

