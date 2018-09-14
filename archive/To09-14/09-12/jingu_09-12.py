#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:30:57 2018

@author: jingu
"""
"""
리스트로 파라미터 할당하고 슬라이스로 넣는 예제 
"""

params = [['3'] * 2 + ['relu'] for i in range(3)]
params[2][2] = 'leaked_relu'
print(params) # output: [['3', '3', 'relu'], ['3', '3', 'relu'], ['3', '3', 'leaked_relu']]
layers = ['first', 'second', 'last']

for i in range(len(layers)):
    print('the {0} layer: {1} x {2} convolution filter using {3}'\
          .format(layers[i], params[i][:2][0],params[i][:2][1], params[i][-1]))
    
# output:
    # the first layer: 3 x 3 convolution filter using relu
    # the second layer: 3 x 3 convolution filter using relu
    # the last layer: 3 x 3 convolution filter using leaked_relu
    


"""
examples from book
l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])
print(l[:3])
print(l[3:])


invoice = "" " 
0.....6.................................40........52...55........
1909 Pimoroni PiBrella $17.50 3 $52.50
1489 6mm Tactile Switch x20 $4.95 2 $9.90
1510 Panavise Jr. - PV-201 $28.00 1 $28.00
1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95
"" " 붙여야함 ㅎㅎ  
print(invoice)
sku = slice(0,5)
description= slice(5,43)
unit_price = slice(43,52)
quantity = slice(52,55)
item_total = slice(55, None)

line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[unit_price], item[description])
""" 

