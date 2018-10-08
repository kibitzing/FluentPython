#!/usr/bin/env python3
# -*- coding: utf-8 -*-

codec = ['ascii','latin_1','cp1252','cp437','gb2312','utf_8','utf_16']
for cod in codec:
    try:
        print(cod, '你好吗？'.encode(cod))
    except UnicodeEncodeError as e:
        print(cod,'is not able to encode “你好吗？”')

print('='*50)

s = '레포트 문자 박살내자'
print(s.encode('cp437', errors='ignore'))
print(s.encode('cp437',errors='replace'))
print(s.encode('cp437', errors='xmlcharrefreplace'))
try:
    print(s.encode('cp437'))
except UnicodeEncodeError as e:
    print('UnicodeDecodeError')
