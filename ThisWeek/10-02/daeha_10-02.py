#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    memoryview와 struct library를 사용하여 .png file header 조사하기
    또한 기존 파일을 읽어 처리하는 작업에서 memoryview를 사용했을 때 속도 향상을 확인하기
"""

import struct
fmt = '<3s3sHH'
with open('python.png', 'rb') as fp:
    img = memoryview(fp.read())
    
header = img[:10]
bytes(header)  # b'\x89PNG\r\n\x1a\n\x00\x00'

struct.unpack(fmt, header)  # (b'\x89PN', b'G\r\n', 2586, 0)

del header
del img


import time
for n in (100000, 200000, 300000, 400000):
    data = 'x'*n
    start = time.time()
    b = data
    while b:
        b = b[1:]  # slicing and slicing and slicing ...
    print('bytes', n, time.time()-start)
    # bytes 100000 0.16228103637695312
    # bytes 200000 0.728708028793335
    # bytes 300000 2.6988298892974854
    # bytes 400000 3.4712140560150146

for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = memoryview(data)  #TODO():
    while b:
        b = b[1:]
    print('memoryview', n, time.time()-start)
    # memoryview 100000 0.011627197265625
    # memoryview 200000 0.022507190704345703
    # memoryview 300000 0.03441882133483887
    # memoryview 400000 0.04538774490356445
    
    # very FAST!!!
