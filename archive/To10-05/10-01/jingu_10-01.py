"""
created by Jingu Kang on 10-01
"""
chineseChar = '你好吗'

print('original character:', chineseChar)
print('length of three Chinese Character is %s ' % len(chineseChar))

encoded = chineseChar.encode('utf-8')
print("after encoding: ",encoded)
print('length of three Chinese character in bytes is {}'.format(len(encoded)))
print('it means that one chinese character holds {0} bytes'.format(int(len(encoded)/len(chineseChar))))

print("after decoded:", encoded.decode('utf-8'))
###output:
#
# original character: 你好吗
# length of three Chinese Character is 3 
# after encoding:  b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x90\x97'
# length of three Chinese character in bytes is 9
# it means that one chinese character holds 3 bytes
# after decoded:  你好吗
#