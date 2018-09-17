#!/usr/bin/envs python3
# -*- coding: utf-8 -*-

#################################
#				#
#       Inha University		#
#     DSP Lab Sanghong Kim	#
#     				#
#				#
#################################

"""
2018_09_17_Fluent_Python
@Author Sanghong.Kim
List를 대체 할 수 있는 것들
array
numpy
scipy
deque

결론 : list와 numpy로 자료를 만들 때 걸리는 시간이 비슷하였음
       데이터를 다루는데는 현재로는 numpy가 가장 쉬웠으며
       array가 list보다 자료 저장 및 불러오는 것은 쉬었음
       같은 data를 표현할때도 다양한 방법이 있다는 것을 알게됨
       따라서 해당 상황에 맞는 자료형 선택이 가장 중요하다 생각됨
"""

# Import Modules
import random
import time
import matplotlib.pyplot as plt
import os
import sys
import torch
import torch.nn as nn
import numpy as np
import argparse

from collections import deque
from array import array
from time import perf_counter

def array_data(nData):
    data=array('d', (random.uniform(0,1) for i in range(nData)))
#    data=array('d', (random.uniform(0.1,0.3) for i in range(nData)))
#    data2=array('d', (random.uniform(0.7,0.9) for i in range(num_data)))
     # Save Data -> Next Time
#    cdata=data1.__add__(data2)
#    fp = open('./data.bin', 'wb')
#    data.tofile(fp)
#    fp.close()
    return data

def list_data(nData):
    data=list(random.uniform(0,1) for i in range(nData))
#    foo 사용 해야됨
#    fp = open('./data.bin', 'wb')
#    data.tofile(fp)
#    fp.close()
    return data

def numpy_data(nData):
    data=np.random.random(nData)
#    fp = open('./data.bin', 'wb')
#    data.tofile(fp)
#    fp.close()
    return data

def deque_data(nData):
    data=deque((random.uniform(0,1) for i in range(nData)), maxlen=nData)
    return data

"""
# next time
# Loading Data
def load_data(nData):
    fp = open('./data.bin', 'rb')
    ldata=array('d')
    ldata.fromfile(fp, nData)
    fp.close()
    return ldata


# SVM
# Make Data One(0.2 to 0.3) Two(0.8,0.9) -> Linear SVM Classification
class LinearSVM(nn.Module):
    def __init__(self):
        super(LinearSVM, self).__init__()
        self.fc = nn.Linear(2,1)

    def forward(self, x):
        h = self.fc(x)
        return h
"""


def main(args):
    # Started Time
    st=time.time()

    # Select Data Type
    if args.list:
        data=list_data(10**args.nData)
    elif args.array:
        data=array_data(10**args.nData)
    elif args.numpy:
        data=numpy_data(10**args.nData)
    elif args.deque:
        data=deque_data(10**args.nData)
    else:
        sys.exit(0)
 
    # For Debugging
    print ("Data Type : ",type(data))

    # Ended Time
    et=time.time()

    # Running Time (End Time - Start Time)
    print ("Running Time : ",et-st,"s")


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--nData", type=int, default=7, help="Num of Data, 10^nData")
    parser.add_argument("--list", dest='list', action='store_true', help="Data Type : List")
    parser.set_defaults(list=False)
    parser.add_argument("--array", dest='array', action='store_true', help="Data Type : Array")
    parser.set_defaults(array=False)
    parser.add_argument("--numpy", dest='numpy', action='store_true', help="Data Type : Numpy")
    parser.set_defaults(numpy=False)
    parser.add_argument("--deque", dest='deque', action='store_true', help="Data Type : Deque")
    parser.set_defaults(dequey=False)
    args = parser.parse_args()
    # This program cannot completely avoid Arguments error
    if len(sys.argv) > 4:
        print ("Too many Arguments!")
        parser.print_help()
        sys.exit(0)
    main(args)
