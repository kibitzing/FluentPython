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
2018_09_28_Fluent_Python
@Author Sanghong.Kim
hash가능 한 것에 대하여 다시 한번 생각 하게 됨
금일의 내용은 코드로서 짤 내용은 별로 없는 듯 싶으며 4장을 보았을 때 재밌어 보이는 부분이 있음
4학년 막학기 프로젝트로 bash shell 에서 문자를 비교할 때 사용하였던 문자의 byte형 표현이 보임
다시 한번 느끼는 것이지만 파이썬을 사용하니 bash shell 을 사용하였을 때 보다 훨씬 빠른 코딩 속도를 내고 있음
또한 shell 스크립트에서 사용하였던 구문들 중 비슷한 내용이 많아 조금 더 익숙해지면 간단한 게임을 만들어 볼 계획임
torch는 언젠간 사용하겠지 라는 생각으로 지속적으로 import 하는 중이며 이번 Digital Speech Processing 과목의 출석 \
대체 영상인 Andrew Ng 의 강의에 있는 간단한 Machine Learning 알고리즘을 실행 하는 방향으로 다음주는 코드를 짤 것 같음
"""

# Import Modules
import time
import os
import sys
import torch
import torch.nn as nn
import numpy as np
import argparse

DIAL_CODES_Korea = [
    ('010', 'CellPhone'),
    ('02', 'Seoul'),
    ('031', 'Gyeonggido'),
    ('032', 'Incheon'),
    ('033', 'Gangwondo'),
    ('041', 'Chungcheongnamdo'),
    ('042', 'Daejeon'),
    ('043', 'Chungcheongbukdo'),
    ('044', 'Sejong'),
    ('051', 'Busan'),
    ('052', 'Ulsan'),
    ('053', 'Daegu'),
    ('054', 'Gyeongsangbukdo'),
    ('055', 'Gyeongsangnamdo'),
    ('061', 'Jeollanamdo'),
    ('062', 'Gwangju'),
    ('063', 'Jeollabukdo'),
    ('064', 'Jeju')
]

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

def main(args):

    '''
    예제 코드
    '''

    d1=dict(DIAL_CODES)
    d2=dict(sorted(DIAL_CODES))
    d3=dict(sorted(DIAL_CODES,key=lambda x:x[1]))

    print('d1 : ', d1.keys())
    print('d2 : ', d2.keys())
    print('d3 : ', d3.keys())


    """
    hash 불가능한 dict 및 list에 대하여 set에 add 및 비교가 안되는 것을 확인
    set의 경우도 hash 불가능함을 알았음
    
    k=set(d1)
    l=set(d2)

    k.add(DIAL_CODES)
    
    """

    # frozenset은 언제나 hash가능 하므로 아래와 같이 해보았음

    DCK=frozenset(DIAL_CODES_Korea)
    DC=frozenset(DIAL_CODES)

    s1=set(DC)
    s2=s1.copy()
    s1.add(DCK)

    print("한국의 Dial Code와 한국 + 세계의 Dial Code 의 차이나는 부분 : ",s1.difference(s2))

    print("차이를 비교할 때는 비교 대상이 unhashable 해도 됨, 비교 대상이 type도 포함됨", s2.difference(d1))

    # assert 를 처음 써보았는데 if not 과 비교하여 보았을 때 if not이 더 빠르게 실행 되는 모습을 볼 수 있었음
    # 하지만 코드를 보기에는 assert가 더 깔끔 해 보임 (한줄)

    # Started Time
    st=time.time()

    assert d1 == d2 and d2 == d3

    # Ended Time
    et=time.time()

    # Running Time (End Time - Start Time)
    print ("Running Time : ",et-st,"s")

    # Started Time
    st=time.time()

    if not d1 == d2 and d2 == d3:
        raise AssertionError()

    # Ended Time
    et=time.time()

    # Running Time (End Time - Start Time)
    print ("Running Time : ",et-st,"s")

    try:
        assert d1 == d2 and d2 == d3
    except AssertionError:
        print("AssertionError")


    # 자동 push bash script 공유중
    # test용 주석


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
