#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    ASCII character인지 확인하는 예제
"""

from unicodedata import normalize

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def fold_to_ascii(text):

    if is_ascii(text):
        return text
    return normalize('NFKD', text).encode('ascii', 'ignore') 
        
        
text = "Hello earth!!"

if is_ascii(text):
    print(text)
    
_ascii = fold_to_ascii(text)
print(_ascii)
