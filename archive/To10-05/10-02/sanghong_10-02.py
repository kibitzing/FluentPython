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
2018_10_02_Fluent_Python
@Author Sanghong.Kim
오늘의 책을 읽어 보았을 때 딱히 떠오르는 아이디어가 없었다. (더 좋은 방향이 있기 때문)
따라서 활용 방법을 모르겠어서 예제 코드만 돌려 보았다.
"""

# Import Modules
import time
import os
import sys
import argparse


def main(args):
    # Started Time
    st=time.time()

    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowel = ['a', 'e', 'i', 'o' 'u']



    '''
    example code
    '''
    print("example 4-5")
    print("------------------------------------------------------------------")
    for codec in ['latin_1', 'utf_8', 'utf_16']:
        print(codec, 'El Niño'.encode(codec), sep='\t')
    print("------------------------------------------------------------------")
    print()
    print("example 4-6")
    print("------------------------------------------------------------------")
    city = 'São Paulo'
    for codec in ['utf_8', 'utf_16', 'iso8859_1', 'cp437']:
        print(codec, city.encode(codec, errors='ignore'), sep='\t')
    print("------------------------------------------------------------------")
    print()
    print("example 4-7")
    print("------------------------------------------------------------------")
    # b -> bytes
    octets = b'Montr\xe9al'
    for codec in ['cp1252', 'iso8859_7', 'koi8_r', 'utf_8']:
        print(codec, octets.decode(codec, errors='replace'), sep='\t')
    print("------------------------------------------------------------------")


    # Ended Time
    et=time.time()

    # Running Time (End Time - Start Time)
    print ("Running Time : ",et-st,"s")


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
