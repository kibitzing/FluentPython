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
2018_10_16_Fluent_Python
@Author Sanghong.Kim
오늘은 opertator 라는 것 까지 알아보았다. 가장 관심이 가는 부분은 methodcaller 에서 replace 였다.
Data를 처리할 일이 많은 나에게 있어서 지금까지 sed 's/바꿔질패턴/바뀐패턴/g' temp > output 이런식으로 했었는데
너무 쉽게 처리 할 수 있었다.
"""

# Import Modules
import time
import os
import sys
import argparse
import inspect
from functools import reduce
import operator

metro_data=[
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691997)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def clip_annot(text, max_len=80) -> str:
    """max_len 앞이나 뒤의 마지막 공백에서 잘라낸 텍스트를 반환한다.
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

def fact(n):
    return reduce(operator.mul, range(1,n+1))

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
    print(clip_annot.__annotations__)
    sig = inspect.signature(clip_annot)
    print(sig.return_annotation)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)

    print(fact(5))

    # Operator 의  Itemgetter를 이용하여 Tuple에서 원하는 정보들을 가져옴
    cc_name = operator.itemgetter(1,2)
    for city in metro_data:
        print(cc_name(city))

    from collections import namedtuple
    LatLong = namedtuple('LatLong', 'lat long')
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')
    metro_areas = [Metropolis(name, cc, pop, LatLong(lat,long))
                   for name, cc, pop, (lat,long) in metro_data]
    print(metro_areas[0])
    print(metro_areas[0].coord.lat)



    name_lat = operator.attrgetter('name', 'coord.lat')

    for city in sorted(metro_areas, key=operator.attrgetter('coord.lat')):
        print(name_lat(city))

    ''' 튜플을 가지고 노는 느낌이 든다... '''

    s = "16일 2018 10월 모의고사가 전국 고등학교 3학년 재학생을 대상으로 치러졌다. 이른바 '자살방지 모의고사'라고 불리는 2018 10월 모의고사 성적에 응시자들의 관심이 집중되고 있다."

    upcase = operator.methodcaller('upper')
    hiphenate = operator.methodcaller('replace', ' ', '_')
    print(upcase(s))
    print(hiphenate(s))



# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
