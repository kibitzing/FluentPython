#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 산술 콘텍스트의 정밀도를 변경해보는 예제
    
    pages 465~469; 한글 기준
"""


import decimal

ctx = decimal.getcontext()
ctx.prec = 40
num = decimal.Decimal('1') / decimal.Decimal('3')
print(num)  # 0.3333333333333333333333333333333333333333

print(num == +num)  # True

ctx.prec = 29
print(num == + num)  # False

print(+num)  # 0.33333333333333333333333333333