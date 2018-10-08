#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    string의 encoding & decoding을 수행하는 예제
    파이썬 built-in `open`을 사용해도 되지만, 개념을 이해하는 차원에서 
    다음과 같은 예제를 작성할 수 있다
"""

import codecs  # 파일을 조금씩 읽을 수 있고, 메모리에도 약간의 리소스만 소요됨

# open input stream and output stream
input = codecs.open("input.txt", "rb", encoding="utf-8")
output = codecs.open("output.txt", "wb", encoding="utf-8")

# streaming Unicode chunk data
with input, output:
    while True:
        chunk = input.read(4096)
        print(chunk)
        if not chunk:
            break
        chunk = chunk.replace(u"\u000B", u"")
        output.write(chunk)
