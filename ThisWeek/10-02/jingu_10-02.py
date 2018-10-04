"""
created by Jingu Kang on 10-02
"""

## 
chineseChar = '你好吗'
print('你好吗 encode with gb2312: ', chineseChar.encode('gb2312')) 
# 你好吗 encode with gb2312:  b'\xc4\xe3\xba\xc3\xc2\xf0'
print('你好吗 encode with utf-8: ', chineseChar.encode('utf-8'))
# 你好吗 encode with utf-8:  b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x90\x97'
print('你好吗 encode with cp(error="replace"): ', chineseChar.encode('cp437', errors='replace'))
# 你好吗 encode with cp(error="replace"):  b'???'
gbEncodedCnCh = chineseChar.encode('gb2312')
utfEncodedCnCh = chineseChar.encode('utf-8')

print('你好吗 gb decoded -> utf decode: ', gbEncodedCnCh.decode('utf-8', errors='replace'))
ㅋ# 你好吗 gb decoded -> utf decode:  �����
print('你好吗 gb decoded -> gb decode: ', gbEncodedCnCh.decode('gb2312', errors='replace'))
# 你好吗 gb decoded -> gb decode:  你好吗
print('你好吗 utf encoded -> gb decode: ', utfEncodedCnCh.decode('gb2312', errors='replace'))
# 你好吗 utf encoded -> gb decode:  浣�濂藉��

## example 4-6
city = 'São Paulo'
print(city.encode('utf-8'))
print(city.encode('utf_16'))
print(city.encode('iso8859_1'))

print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='xmlcharrefreplace'))

## example 4-7
octets = b'Montr\xe9al'
print('cp1252:', octets.decode('cp1252'))
print('iso8859_7:', octets.decode('iso8859_7'))
print('koi8_r:', octets.decode('koi8_r', errors='replace'))
print('utf-8:', octets.decode('utf-8', errors='replace'))
print('utf version: ', octets.decode('cp1252').encode('utf-8'))