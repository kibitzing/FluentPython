#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 28/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        코루틴으로 순환버스 구현하기.
        Implement Cycle route bus with coroutine
"""

def bus9200():
    time = 0
    passedTime = 0
    index = 0
    stations = ['1. 인하대', '2. 장미아파트', '3. 신동아아파트', '4. 선바위', '5. 강남']

    while True:
        try:
            passedTime = yield '현재역: ' + str(stations[index]) +', 누적주시간: '+str(time)
            time = time + passedTime
            index += 1
        except  IndexError:
            stations.reverse()
            index = 1

co =bus9200()

print(next(co))
print(co.send(3))
print(co.send(5))
print(co.send(30))
print(co.send(15))
print(co.send(30))
print(co.send(15))
print(co.send(5))
print(co.send(3))
print(co.send(5))
print(co.send(5))


# 현재역: 1. 인하대, 누적주행시간: 0
# 현재역: 2. 장미아파트, 누적주행시간: 3
# 현재역: 3. 신동아아파트, 누적주행시간: 8
# 현재역: 4. 선바위, 누적주행시간: 38
# 현재역: 5. 강남, 누적주행시간: 53
# 현재역: 4. 선바위, 누적주행시간: 83
# 현재역: 3. 신동아아파트, 누적주행시간: 98
# 현재역: 2. 장미아파트, 누적주행시간: 103
# 현재역: 1. 인하대, 누적주행시간: 106
# 현재역: 2. 장미아파트, 누적주행시간: 111
# 현재역: 3. 신동아아파트, 누적주행시간: 116
