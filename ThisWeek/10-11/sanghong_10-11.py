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
2018_10_11_Fluent_Python
@Author Sanghong.Kim
고위 함수들은 대부분 제거 되었음 -> 더 나은 방법이 있기 때문이라 함
map filter -> 지능형 리스트 (이전에 배운 내용)
바뀌어진 sum이 reduce 와 sum을 사용한 것보다 Running Time이 더 적은 것을 확인 할 수 있었다.
물론 이전에 기본 함수로 있었을때는 어땠을지 모르나 현재로써는 그렇다.
객체라는 것을 이해하지 못하고 있다가 아 이런식으로 쓰면 객체구나 라는 생각을 하게 되었다.
bash 스크립트를 쓰다가 python을 쓰니 편하긴 한데 아직 사용할 수 있는 범위가 적은 것 같다.
매일 주석을 일기 처럼 쓰는 것 같음을 느낀다, 일과의 끝을 해당 스터디로 보내기 때문인 것 같다.
"""

# Import Modules
import time
import os
import sys
import argparse
from functools import reduce
from operator import add

fruits = [
    'strawberry',
    'fig',
    'apple',
    'cherry',
    'raspberry',
    'banana'
]


def factorial_example(n):
    '''n factorial, doc 기능을 처음 알았음'''
    return 1 if n < 2 else n * factorial_example(n-1)

def factorial_if_else(n):
    '''n factorial, doc 기능을 처음 알았음 example 보다 처리 속도가 빠름 '''
    if n < 2:
        return 1
    else:
        return n * factorial_if_else(n-1)

def time_cal(program):
    # Started Time
    st=time.time()
    # Running Program
    print(program)
    # Ended Time
    et=time.time()
    # Running Time
    return et-st

def main(args):
    print("Running Time : ", time_cal(factorial_example(5)))
    print("Running Time : ", time_cal(factorial_if_else(5)))

    #print(factorial_example.__doc__)
    print(factorial_if_else.__doc__)

    fact=factorial_if_else

    # 아래의 프로그램이 처리속도가 더 빠른데 이유를 모르겠음
    print("Running Time : ", time_cal(fact(5)))

    # map은 고위 함수로 함수를 인수로 받거나 함수를 결과로 반환 ex) sorted()
    print(list(map(fact, range(1,11))))

    # 길이를 기준으로 sort 해준다.
    print(sorted(fruits, key=len))

    print("Running Time : ", time_cal(reduce(add,range(100))))
    print("Running Time : ", time_cal(sum(range(100))))


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
