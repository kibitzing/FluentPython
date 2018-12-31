# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:39:54 2018

@author: jiyun
"""

# 원서기준 480~484p

from collections import namedtuple

Result = namedtuple('Result','count average')

# 하위 제너레이터
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None: # 종료 조건
            break
        total += term
        count += 1
        average = total/count
    return Result(count,average)

# 대표 제너레이터
def grouper(results, key):
    while True:
        results[key] = yield from averager() # 받는 값 averager() 객체로 전달
        
# 호출자 : 함수 전체 실행       
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None) # 현재 객체 종료시킴, grouper가 실행 재개하게 만들 때 새로운 averager() 객체 생성
        
#    print(results)
    report(results)
    
# 실행 결과 보고서   
def report(results):
    for key, result in sorted(results.items()):
        classname, group, unit = key.split(';')
        print('{:3} {:2}명 과목 : {:8} 평균 : {:.2f}{}'.format(classname, result.count,group, result.average, unit))
        

data = {
        '1반;math;점':
            [40,25,68,22,99,58,68,48,57,54,92,86,67,48,100,10],
        '1반;english;점':
            [44,45,85,86,75,28,84,95,94,83,37,58,64,49,58,81],
        '2반;math;점':
            [100,82,97,91,90,85,81,83,74,70,68,64,60,58,28],
        '2반;english;점':
            [55,27,84,61,37,84,59,72,61,52,68,70,51,28,99],
        }
    
    
if __name__ == '__main__':
    main(data)
    
"""
1반  16명 과목 : english  평균 : 66.62점
1반  16명 과목 : math     평균 : 58.88점
2반  15명 과목 : english  평균 : 60.53점
2반  15명 과목 : math     평균 : 75.40점
"""    
    