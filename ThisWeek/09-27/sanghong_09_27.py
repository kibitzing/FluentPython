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
2018_09_27_Fluent_Python
@Author Sanghong.Kim
find needles in haystack
data를 비교하는데 있어서 여러가지 방법이 있으며
그 중 3개에 대해서 알아보았다.
list와 list의 비교, set과 set과의 비교 등
이전에 python을 사용할 때 xrange라는 함수를 사용하면 속도가 더 빨랐던 것으로
기억하는데 xrange를 사용하려 하면 에러가 발생하여 이에 대해 확인이
필요하다.
dict 형에 대해서 for loop가 굉장히 빠른 시간을 나타냈는데 신기하다.
list 형에 대해서는 가장 느렸던 방법이 dict형에서는 가장 빠르니말이다.
"""


# Import Modules
import time
import os
import sys
import torch
import torch.nn as nn
import numpy as np
import argparse
import random
from unicodedata import name

def create_list(sData,nData):
    data = []
    for i in range(sData,nData):
        data.append(i)
    return data

def create_dict(sData,nData):
    data = {}
    key = range(sData,nData)
    value = range(1,nData)
    data = dict(zip(key,value))
    return data

def comparison(needles, haystack):
    # Started Time
    st=time.time()

    found = 0
    for n in needles:
        if n in haystack:
            found += 1

    # Ended Time
    et=time.time()

    print("Corresponded :", found)

    # Running Time (End Time - Start Time)
    print ("Running Time with for loop : ",et-st,"s")

    # Started Time
    st=time.time()

    found = len(set(needles) & set(haystack))

    # Ended Time
    et=time.time()

    print("Corresponded :", found)

    # Running Time (End Time - Start Time)
    print ("Running Time with set method : ",et-st,"s")

    # Started Time
    st=time.time()

    found = len(set(needles).intersection(haystack))

    # Ended Time
    et=time.time()

    print("Corresponded :", found)

    # Running Time (End Time - Start Time)
    print ("Running Time with set intersection : ",et-st,"s")



def main(args):

    sData1=random.randrange(1,10**3)
    sData2=random.randrange(10**2,10**4)

    needles = create_list(sData1,10**4)
    haystack_l = create_list(sData2,10**5)
    haystack_d = create_dict(sData2,10**5)


    print("Actual corresponded value :",10**4-sData2)


    print("---------------------")
    print("      List data      ")
    comparison(needles,haystack_l)

    print("---------------------")

    print("      Dict data      ")
    comparison(needles,haystack_d)
    print("---------------------")



# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    # This program cannot completely avoid Arguments error
    if len(sys.argv) > 4:
        print ("Too many Arguments!")
        parser.print_help()
        sys.exit(0)
    main(args)
