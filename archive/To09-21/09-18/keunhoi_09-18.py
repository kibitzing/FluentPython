#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# example3-1
DIAL_CODES = [
    (86,'CHINA'),
    (91, 'INDIA'),
    (1,'USA'),
    (62, 'INDONESIA'),
    (55, 'BRAZIL'),
    (92, 'PAKISTAN'),
    (880,'BANGLADESH'),
    (234, 'NIGERIA'),
    (7, 'RUSSIA')
]
country_code = {country : code for code, country in DIAL_CODES}

print('country code : ', country_code)
country_code.clear()
print('country code : ', country_code)
country_code = {country : code for code, country in DIAL_CODES}
country_code2 = country_code.copy()
print('country code2 : ', country_code2)
print('country code == country code2 |', country_code == country_code2)

try:
    korea_number = country_code['KOREA']
except KeyError as e:
    print('KeyError is occured')
    korea_number = country_code.get('KOREA') # get은 에러없이 None을 return한다.
print('country code : ', country_code)

print(country_code.__len__())
country_code.setdefault('KOREA')
print(country_code) # setdefault는 get과는 다르게 none value를 가진 항목으로 추가해준다.
print(country_code.setdefault('KOREA'))
print(country_code.setdefault('USA'))
