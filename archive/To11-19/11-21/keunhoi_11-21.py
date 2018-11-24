#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p332-ch11end
# Example 11-14 ~ 17
'''


'''

import abc
import random

import doctest
from tombola import Tombola
import bingo, lotto, tombolist, drum

TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'

@Tombola.register
class TomboList(list):

	def pick(self):
		if self:
			position = random.randrange(len(self))
			return self.pop(position)
		else:
			raise LookupError('pop from empty TomboList')
		load = list.extend()

	def loaded(self):
		return bool(self)

	def inspect(self):
		return tuple(sorted(self))

class Struggle:
	def __len__(self): return 23

def main(argv):
	verbose = '-v' in argv
	real_subclasses = Tombola.__subclasses__()
	virtual_subclasses = list(Tombola._abc_registry)

	for cls in real_subclasses + virtual_subclasses:
		test(cls, verbose)


def test(cls, verbose=False):

	res = doctest.testfile(
            TEST_FILE,
            globs={'ConcreteTombola': cls},
            verbose=verbose,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
	tag = 'FAIL' if res.failed else 'OK'
	print(TEST_MSG.format(cls.__name__, res, tag))

def main2():

	print('='*50)
	print(issubclass(TomboList, Tombola))
	print(isinstance(TomboList(range(100)), Tombola))
	print(TomboList.__mro__) # 데코레이터와 상속의 차이
	print(Tombola.__subclasses__())
	print(Tombola._abc_registry)

def main3():

	from collections import abc
	print('='*50)
	print(isinstance(Struggle(), abc.Sized))
	print(issubclass(Struggle, abc.Sized))


if __name__ == '__main__':
	import sys
	main(sys.argv)
	main2()
	main3()
