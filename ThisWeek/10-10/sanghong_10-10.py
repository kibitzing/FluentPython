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
2018_10_10Fluent_Python
@Author Sanghong.Kim
드디어 지루하였던 4장이 끝났다.
다양한 방법을 시도해서 접근해 보고 싶었으나 10-08일 unicodecsv를 알아 낸 것 이외에 아직까지는 특별한 도움은 없었다.
앞으로 얼마나 많이 사용될지 모르겠으나 (스페인어, 그리스어를 쓸 일이 없을 것 같아서) 확실히 많이 사용되지는 않을 것 같다.
읽을 거리를 보다보니 2012년도의 내용이 언급된 것으로 보아 해당 책의 신뢰도가 올라간 것 같다.
드디어 함수 부분을 들어 간다. 사실 python을 하면서 객체라는 것을 이해하는 것이 어려웠는데 이를 이해하는데 도움이
되었으면 한다.
오늘 역시 예제로 코드를 끝낸다.
"""

# Import Modules
import time
import argparse
import unicodedata
import string
import pyuca

spanish=[
    'café',
    'São Paulo'
]

fruits = [
    'caju',
    'atemoia',
    'cajá',
    'açaí',
    'acerola'
]

greek = [
    'Κόρινθος',
    'Άγιο Όρος'
]

def pre_shave_marks(txt):
    "발음 구별 기호를 모두 제거"
    norm_txt = unicodedata.normalize('NFD', txt)

    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

def shave_marks(txt):
    """발음 구별 기호를 제거하는 함수"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for  c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
            # 라틴 기반 문자의 발음 구별 기호는 무시
        keepers.append(c)
        # 결합 문자가 아니면, 이 문자를 새로운 기반 문자로 간주
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)

def main(args):
    # Started Time
    st=time.time()

    for i in range(0,2):
        print(pre_shave_marks(greek[i]))
        print(shave_marks(greek[i]))

    coll = pyuca.Collator()

    sorted_fruits = sorted(fruits, key=coll.sort_key)
    print(sorted_fruits)

    # Ended Time
    et=time.time()

    # Running Time (End Time - Start Time)
    print ("Running Time : ",et-st,"s")


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
