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
2018_09_21_Fluent_Python
@Author Sanghong.Kim
set

"""

# Import Modules
import time
import os
import sys
import argparse

from dis import dis
from unicodedata import name

def main(args):
    # Started Time
    st=time.time()

    s = {1}
    print(s)

#    print(dis('set([1])'))
    a = {chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')}
    print(a)
    
    # Set 에 int형 add는 가능
    s.add(2)
    print(s)

    # s.add(a) 가 불가능 하다. set은 Non Hashable 함을 알 수 있음
    try:
        s.add(a)
    except TypeError as e:
        print("Type Error occured")
        sys.exit(0)

    # Ended Time
    et=time.time()

    # Running Time (End Time - Start Time)
#    print ("Running Time : ",et-st,"s")


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
