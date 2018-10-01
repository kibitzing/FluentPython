#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    특수문자를 encoding하여 byte value로 확인하는 예제
"""

strange_str = bytes('ˆ¨†∆µ', encoding='utf_8')
print(strange_str)  # b'\xcb\x86\xc2\xa8\xe2\x80\xa0\xe2\x88\x86\xc2\xb5'

strange_str_1 = bytes('∆˜ø', encoding='utf_8')
print(strange_str_1)  # b'\xe2\x88\x86\xcb\x9c\xc3\xb8'