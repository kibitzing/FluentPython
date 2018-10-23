#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#p188~192

# 핵심 특징: 정의된 직후 실행, 즉 임포트 타임에 실행.
from dis import dis
from time import gmtime, strftime

b = 'global b: SO Interesting'

def f1(a):
	print(a)
	print(b)

def f2(a):
	print(a)
	print(b)
	b = 'local b in f2 : Sooooo Interesting'

def f3(a):
	global b
	print(a)
	print(b)
	b = 'global b in f3 : Sooooo Interesting'

# ===============================================================

class Averager():

	def __init__(self):
		self.series = []

	def __call__(self, new_value):
		self.series.append(new_value)
		total = sum(self.series)
		return total/len(self.series)

def make_averager():
	series = []

	def averager(new_value):
		series.append(new_value)
		total = sum(series)
		return total/len(series)

	return averager

# ===============================================================
# 다른 서적을 보다가 궁금해졌단 다수의 데코레이터 사용의 이해를 위한 연습 코드.
def auther(func):
    def auther_wrapper(*args, **kwargs):
        print('khahn0213')
        return func(*args, **kwargs)
    return auther_wrapper


def datetime(func):
    def datetime_wrapper(*args, **kwargs):
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        return func(*args, **kwargs)
    return datetime_wrapper


@auther
@datetime
def introduce():
    print("Today's code is finished.")


def main():
	b = 'local b in main : Sooooo Interesting'
	f1('So Interesting')
	try:
		f2('So Interesting')
	except UnboundLocalError as e:
		print("f2 def has UnboundLocalError: local variable 'b' referenced before assignment")

	f3('So Interesting')
	print('See the Bytecode')
	print('@@ f1'), dis(f1)
	print('@@ f2'), dis(f2)
	print('@@ f3'), dis(f3)

	print('=' * 100)
	avg = Averager()
	print(avg(10))
	print(avg(11))
	print("Class Averager's bytecode"), dis(avg)
	# Class는 dis(class)가 안 되는 듯 하다
	# 공식문서는
	# For a module, it disassembles all functions. For a class, it disassembles all methods (including class and static methods)
	# 이라는데...?

	print('=' * 100)
	avg = make_averager()
	print(avg(10))
	print(avg(11))
	print("@@ def make_averager's bytecode"), dis(avg)
	# 클로저는 함수를 정의하는 범위가 사라진 후에 함수를 호출해도 자유 변수에 접근할 수 있다.
	# 이 사실을 미리 알았더라면.... print 디버깅을 그따구로 하진 않았었겠다...

	introduce()

if __name__ == '__main__':
	main()