#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p478-482
# Example 16-16~17

'''
   예제 위주 작성
'''

from collections import namedtuple

class DemoException(Exception):
    """An exception type for the demonstration."""

# Example 16-16
def chain(*iterables):
    for it in iterables:
        yield from it

# Example 16-17
Result = namedtuple('Result', 'count average')

# 하위 제너레이터
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)

# 대표 제너레이터
def grouper(results, key):
    while True:
        results[key] = yield from averager()

# 호출자
def main(data):
    results = {}
    for k,vals in data.items():
        group = grouper(results, k)
        next(group)
        for v in vals:
            group.send(v)
        group.send(None) # 이 부분이 중요하다고 한다.

    # print(results)    # 디버깅을 하기 위한 코드. 디버깅이 필요 없을 시에는 주석 처리.

# 실행 결과 보고서
def report(results):
    for k, result in sorted(results.items()):
        group, unit = k.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))

data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


if __name__ == '__main__':
    print('{0:=<50}'.format("Example 16-17"))
    main(data)