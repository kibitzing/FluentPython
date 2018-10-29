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
2018_10-24_Fluent_Python
@Author Sanghong.Kim
간단하게 클래스를 다루는 프로그램을 짜봤다.
클래스에서 self 를 이용해서 테스트를 해볼게 많을 것 같다.
__repr__, __call__ 등 다양한 하위 method 가 존재했는데 이를 알맞게 쓰는 방법을 익히는 것이 우선일 것 같다.
"""

# Import Modules
import time
import os
import sys
import argparse
import average_hong as average


def time_cal(program):
    # Started Time
    st=time.time()
    # Running Program
    print(program)
    # Ended Time
    et=time.time()
    # Running Time
    print('Running Time :', et-st)

class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


class Sentence():

    def __init__(self):
        self.series = []
        self.called = 0

    def __call__(self, new_value):
        self.series.append(new_value)
        self.called += 1
        return self.series, self.called

def main(args):
    print("Add Your Code Below")
    avg = Averager()
    word = Sentence()
    print(avg(10))
    print(avg(16))

    avg = average.make_averager()
    print(avg(10))
    print(avg(16))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__[0].cell_contents)

    avg = average.nonlocal_averager()
    print(avg(10))
    print(avg(16))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__[0].cell_contents)

    print(word('안녕'))
    print(word("하세요"))


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
