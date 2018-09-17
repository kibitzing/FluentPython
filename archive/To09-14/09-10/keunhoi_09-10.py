#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # Example 2-4

# colors = ['black', 'white']
# sizes = ['S','M','L']
# tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)

nums1 = range(2,10)
nums2 = range(1,10)
mul_table = [(num1, num2, num1 * num2) for num1 in nums1 for num2 in nums2]
print(mul_table)

# # Example 2-5
# symbols = '#*&%^$'
# ord_symbols = tuple(ord(symbol) for symbol in symbols)
#
# import array
# array_symbols = array.array('I', (ord(symbol) for symbol in symbols))
# print(array_symbols)

import os, glob

pwd = os.getcwd()
pyfiles = glob.glob('*.py')
pyfiles2 = tuple(f for f in glob.glob('*.py'))
print(pyfiles, pyfiles2, sep='\n')
annotation_files = tuple(f for f in glob.glob('*.xml'))
image_files = tuple(f for f in glob.glob('*.jpg'))

