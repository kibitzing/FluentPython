#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 등차수열 제너레이터 알아보는 예제

"""
class ArithmeticCalculation:
    
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end
        
    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index
            

ac = ArithmeticCalculation(0, 1, 3)
list(ac)  # [0, 1, 2]

ac = ArithmeticCalculation(1, .5, 3)
list(ac)  # [1.0, 1.5, 2.0, 2.5]


from fractions import Fraction
ac = ArithmeticCalculation(0, Fraction(1, 3), 1)
list(ac)  # [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]


from decimal import Decimal
ac = ArithmeticCalculation(0, Decimal('.1'), .3)
list(ac)  # [Decimal('0'), Decimal('0.1'), Decimal('0.2')]