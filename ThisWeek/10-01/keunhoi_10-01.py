#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = 'cafe'
print(len(s))
b = s.encode('utf8')
print(b, len(b))
print(b.decode('utf8'))

print('='*50)

cafe = bytes('cafe', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe)
print(cafe_arr[-1:])

print('='*50)

print(bytes.fromhex('62 8B CF D9'))

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)