#!/usr/bin/envs python3
# -*- coding: utf-8 -*-

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_11-20_Fluent_Python
@Author Sanghong.Kim
"""

# Import Modules
import time
import os
import sys
import argparse
import functools
import doctest
import abc
import random
from sanghong_11_19 import Tombola
from sanghong_11_19 import BingoCage as bingo
from sanghong_11_19 import LotteryBlower as lotto
from sanghong_11_19 import TomboList as tombolist

TEST_FILE = 'tombola_sanghong.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
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


def test(cls, verbose=False):
    res = doctest.testfile(
        TEST_FILE,
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
    )
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))


@clock
def main(argv):
    print("Add Your Code Below")
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()
    virtual_subclasses = list(Tombola._abc_registry)

    for cls in real_subclasses + virtual_subclasses:
        test(cls, verbose)




# Arguments Setting
if __name__ == '__main__':
    main(sys.argv)
