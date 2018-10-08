#!/usr/bin/envs python3
# -*- coding: utf-8 -*- --> 파이썬 3부터는 utf-8이 기본 인코딩임

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_10_01_Fluent_Python
@Author Sanghong.Kim
텍스트와 바이트
"""

# Import Modules
import time
import sys
import argparse
import struct
import cv2


def main(args):
    # 한글의 bytearray 표현
    consonant=bytearray('ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ', encoding='utf-8')
    vowel=bytearray('ㅏ ㅑ ㅓ ㅕ ㅗ ㅛ ㅜ ㅠ ㅡ ㅣ', encoding='utf-8')
    gana=bytearray('가 갸 거 겨 나 냐 너 녀', encoding='utf-8')

    # byte로 나타낸 한글 표현
    print(consonant)
    print(vowel)
    print(gana)

    """
    UTF-8 Encoding 이 된 문자는 0~255까지의 숫자 3개의 집합?으로 표현됨 'ㄱ + ㅏ' 와 '가'는 애초에 다른 문자임을 알 수 있었음
    별의 별 이상한 연산을 해보았으나 패턴을 찾을 수 없었기에 UTF-8 Table 을 찾아보았고 해당 Table 을 보니 해당 이유를 알 수 있었음 
    """
    print(consonant[0:3].decode('utf8') + vowel[0:3].decode('utf8'))
    print(gana[0:3].decode('utf8')+gana[3:4].decode('utf8')+gana[4:7].decode('utf8'))

    """
    Opencv 등에서 Image 의 크기를 가져오는 방식중 아래의 방법이 들어가 있을 것 같음
    Header 가 어디까지인지 정보만 알면 쉬운 처리가 가능할 것 같으나 사실상 해당 코드를 돌려 보았을 때 드는 생각은
    해당 방법을 실제로 사용하지는 않을 것 같음 확실히 실행 시간은 매우 빠름을 확인 할 수 있었음
    gif 파일과 jpg 파일이라는 맹점이 있으나 그럼에도 불구하고 저정도의 속도 차이는 크다고 생각되어짐
    """

    # Started Time
    st=time.time()

    giffmt = '<3s3sHH'
    with open('capture.gif', 'rb') as fp:
        img = memoryview(fp.read())

    header = img[0:10]
    print(struct.unpack(giffmt,header))
    del header
    del img

    # Ended Time
    et = time.time()

    # Running Time (End Time - Start Time)
    print("Running Time : ", et - st, "s")

    # Started Time
    st=time.time()

    img = cv2.imread('capture.jpg')
    height, width, channels = img.shape
    print (width, height)

    # Ended Time
    et=time.time()

    # Running Time (End Time - Start Time)
    print ("Running Time : ",et-st,"s")


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    # This program cannot completely avoid Arguments error
    if len(sys.argv) > 3:
        print ("Too many Arguments!")
        parser.print_help()
        sys.exit(0)
    main(args)