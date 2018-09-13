# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:51:28 2018

@author: jiyun
"""

import dis
dis.dis('s[a] += b')

colors = ['white', 'black','red','blue','yellow']
print(sorted(colors))
#['black', 'blue', 'red', 'white', 'yellow']

print(colors)
#['white', 'black', 'red', 'blue', 'yellow']

print(sorted(colors, reverse=True)) 
#['yellow', 'white', 'red', 'blue', 'black']

print(sorted(colors, key=len, reverse=True)) 
#['yellow', 'white', 'black', 'blue', 'red']

print(sorted(colors, key=len)) 
#['red', 'blue', 'white', 'black', 'yellow']

print(colors) 
#['white', 'black', 'red', 'blue', 'yellow']

print(colors.sort()) 
#None

print(colors) 
#['black', 'blue', 'red', 'white', 'yellow']