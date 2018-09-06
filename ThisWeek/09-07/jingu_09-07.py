#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 20:36:49 2018

@author: jingu
"""

"""
of books
symbols = '$%^&*('
codes = [ord(symbol) for symbol in symbols]

print(codes)

symbs = '%^&*('
beyond_ascii = [ord(s) for s in symbs if ord(s) > 17]

colors = ['black', 'white']
sizes = ['S','M', 'L']
tshirts = [(color, size) for color in colors 
                           for size in sizes]
"""
# ending page
ourBookPages = 684
# starting page
startingPage = 19
# total amount to be read
totalPageToRead = 684 - 19
# using listComp
daysToRead = [(startingPage + i * 5, startingPage + (i+1) * 5 -1 ) for i in range(round(totalPageToRead/5))]
# our schedule
print(daysToRead)
# days We will study.
print(len(daysToRead))
# 마지막 날은 한장 더 합시다 ^^;