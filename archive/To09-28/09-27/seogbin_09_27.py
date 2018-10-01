test_text = 'information of incoding'
encoded_text = test_text.encode('utf_16')
le_encode = test_text.encode('utf_16le')
if encoded_text == le_encode:
    print('default encoding type is Little Endian')
else:
    print('default encoding type is Big Endian')

