#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 26/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        Implemented summer in the same pattern in ex 16-17
"""

from collections import namedtuple

Result = namedtuple('Result', 'total')
def summer():
    total = 0

    while True:
        term = yield
        if term is None:
            break
        total += term
    return Result(total)

def grouper(results, key):
    while True:
        results[key] = yield from summer()

def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    report(results)

def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:7} total: {}'.format(group, result.total))

data = {
'class A;points': [80, 90, 20, 80 ,33, 74, 100, 48],
'class B;points': [87, 66,58,87,69,67,67,54],
'class C;points': [68, 70, 24, 80 , 73, 47, 90, 75],
'class D;points': [26, 60, 28, 46 ,89, 73, 10, 85]
}


if __name__ == '__main__':
    main(data)

# def main(data):
#     results = {}
#     for key, values in data.items():
#         group = grouper(results, key)
#         next(group)
#         for value in values:
#             group.send(value)
#         group.send(None)
#     # print(results)
#     report(results)

# def report(results):
#     for key, result in sorted(results.items()):
#         group, unit = key.split(';')
#         print('{:2} {:5} total {:.2f} {}'.format(result.count, group, result.total, unit))

#
# def averager():
#     total = 0.0
#     count = 0
#     average = None
#     while True:
#         term = yield
#         if term is None:
#             break
#         total += term
#         count += 1
#         average = total / count
#     return Result(count, average)
#
#
# def grouper(results, key):
#     while True:
#         results[key] = yield from averager()
