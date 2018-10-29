#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#p193~197
import time
from dis import dis
from time import gmtime, strftime

# ===============================================================
def auther(func):
    def auther_wrapper(*args, **kwargs):
        print('khahn0213')
        return func(*args, **kwargs)
    return auther_wrapper


# def datetime(func):
#     def datetime_wrapper(*args, **kwargs):
#         print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
#         return func(*args, **kwargs)
#     return datetime_wrapper

@auther
# @datetime
def introduce():
    print("Today's code is finished.")
# ===============================================================
def make_averager():
	series = []

	def averager(new_value):
		series.append(new_value)
		total = sum(series)
		return total/len(series)

	return averager

def make_averager2():
	count, total = 0, 0

	def averager2(new_value):
		nonlocal  count, total
		count += 1
		total += new_value
		return total/count

	return averager2
# ===============================================================
def clock(func):
	def clocked(*args):
		t0 = time.perf_counter()
		result = func(*args)
		elapsed = time.perf_counter() - t0
		name = func.__name__
		arg_str = ', '.join(repr(arg) for arg in args)
		print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
		return result
	return clocked

@clock
def snooze(seconds):
	time.sleep(seconds)

@clock
def factorial(n):
	return 1 if n<2 else n*factorial(n-1)




# ===============================================================
def main():
	introduce()

	avg = make_averager()
	print(avg.__code__.co_varnames)
	print(avg.__code__.co_freevars)
	print(avg.__closure__)
	print(avg.__closure__[0].cell_contents)
	print(avg(10)) # print로 불러와도 call은 한거라서 추가된다.
	print(avg.__closure__[0].cell_contents)
	avg(11)
	print(avg.__closure__[0].cell_contents)

	print('=' * 100)

	avg2 = make_averager2()
	print(avg2.__code__.co_varnames)
	print(avg2.__code__.co_freevars)
	print(avg2.__closure__)
	print(avg2.__closure__[0].cell_contents)
	print(avg2.__closure__[1].cell_contents)
	print(avg2(10))
	print(avg2.__closure__[0].cell_contents)
	print(avg2.__closure__[1].cell_contents)
	avg2(11)
	print(avg2.__closure__[0].cell_contents)
	print(avg2.__closure__[1].cell_contents)

	print('=' * 100)

	print('*' * 40, 'Calling snooze(.123)')
	snooze(.123)
	print('*' * 40, 'Calling factorial(6)')
	print('6! =', factorial(6))
	print('*' * 20, '__name__ return value of snooze :', snooze.__name__)
	print('*' * 20, 'dis result of snooze :'), dis(snooze)
	print('*' * 20, '__name__ return value of factorial :', factorial.__name__)
	print('*' * 20, 'dis result of factorial :'), dis(factorial)
if __name__ == '__main__':
	main()