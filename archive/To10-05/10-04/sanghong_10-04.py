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
2018_10_04_Fluent_Python
@Author Sanghong.Kim
오늘 Pytorch가 1.0 버전이 나왔다.
Tensorflow 1.0이 나왔을 때와 마찬자기로 1.0 이라는 숫자가 붙은 점에서 의미 있는 업데이트라 생각되어진다.
Documentation을 보고 변경된 부분이 어느정도인지 봐야겠다.
10월 2일과 마찬가지로 4장의 내용은 큰 의미가 있을지 모르겠는 바이다.
이번주 코드를 작성하고 나니 해당 내용에 대해서 내가 흥미를 느끼고 있는지 모르겠다는 생각이 든다.
다음 장으로 넘어가면 좋겠다는 생각이 든다.
예제 코드만 작성하여서 슬프다.
"""

# Import Modules
import time
import os
import sys
import argparse


def main(args):
    # Started Time
    st=time.time()

    '''
    example code
    '''

    u16 = 'El Niño'.encode('utf_16')
    print(u16)
    print(list(u16))

    # Little-endian
    u16le = 'El Niño'.encode('utf_16le')
    print(u16le)
    print(list(u16le))

    # Big-endian
    u16be = 'El Niño'.encode('utf_16be')
    print(u16be)
    print(list(u16be))

    # 해당 Endian들 간에는 저장하는 방법에 대한 차이가 잇는 것 뿐이라고 생각되어진다. (Format 차이)

    open('cafe.txt', 'w', encoding='utf_8' ).write('Café')
    print(open('cafe.txt').read())

    # Ended Time
    et=time.time()

    # Running Time (End Time - Start Time)
    print ("Running Time : ",et-st,"s")


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
