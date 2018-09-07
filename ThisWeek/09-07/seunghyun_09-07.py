# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 21:30:33 2018

@author: lsh91
"""

#Example 2-1. Build a list of Unicode codepoints from a string.
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
    
print (codes)

#Example 2-2. Build a list of Unicode codepoints from a string, take two.
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]

print (codes)

#Example 2-3. The same list built by a listcomp and a map/filter composition.
# listcomp를 통해 iterative process + condition까지 할 수 있다.
# Out = [Process(i) for i in Input if Condition ]

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print (beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print (beyond_ascii)

### index를 통한 image 분류....
idx = [0,1,1,0,1,0]
imgs = ['L', 'R', 'R', 'L', 'R', 'L',]
left_img  = [img for i, img in enumerate(imgs) if idx[i] ==0]
right_img = [img for i, img in enumerate(imgs) if idx[i] ==1]

print (left_img)
print (right_img)




