# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:58:49 2018

@author: jiyun
"""

s = 'aÿé'
print(len(s)) #2
#b = s.encode()
b = bytes(s,encoding = 'utf_8')
print(b)
# b'\xc3\xbf\xc3\xa9'
print(len(b)) #4
print(b.decode()) #ÿé



#bb = b'café'
# SyntaxError: bytes can only contain ASCII literal characters.
bb = b'string to byte'
# b'string to byte'



c = '\xff'
print(c) #ÿ
d = '\xc3\xbf'
print(d) #Ã¿



print(b[0]) #97
print(b[:1]) #b'a'
print(b[1:2]) #b'\xc3'

bb = bytearray(b)
print(b[:1]) #b'a'
print(b[1:2]) #b'\xc3'

##################################################

cafe = bytes('café', encoding = 'utf_8')
print(cafe) #b'caf\xc3\xa9'
print(cafe[0]) #99
print(cafe[:1]) #b'c'
print(cafe[:4]) #b'caf\xc3'
print(cafe[:5]) #b'caf\xc3\xa9'
print(cafe[-1:])
cafe_arr = bytearray(cafe)
print(cafe_arr) #bytearray(b'caf\xc3\xa9')
print(cafe_arr[:4]) #bytearray(b'caf\xc3')
print(cafe_arr[:5]) #bytearray(b'caf\xc3\xa9')
print(cafe_arr[-1:])
