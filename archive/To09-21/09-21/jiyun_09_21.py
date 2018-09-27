# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 14:13:33 2018

@author: jiyun
"""
from datetime import datetime
from types import MappingProxyType

subject = {3:'DSP', 2:'Capstone'}

#강입
year = datetime.today().year        
month =datetime.today().month      
day = datetime.today().day        
if((year == 2018) and (month >= 10) and (day > 1)):
    subject = MappingProxyType(subject)
    
try:
    subject[1] = '실험'
    print('"실험"과목이 신청되었습니다')
except:
    print('강입 기간이 끝났습니다')

##################################################################

l = ['spam','spam','spam','spam','spam','spam','spam','spam']
print(set(l)) #{'spam'}
print(type(l))
print(l.pop())
print(l) #['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam']
s = {1}
print(type(s))
print(s) #{1}
print(s.pop())
print(s) #set()

##################################################################

from dis import dis
print(dis('set({1})'))

##################################################################

from unicodedata import name
print({chr(i) for i in range(200,256) if 'SIGN' in name(chr(i),'')}) #{'÷', '×'}

##################################################################

a = {2,3,4}
b = {3,5,7}
print(a.__and__(b)) #{3}
print(a.__or__(b)) #{2, 3, 4, 5, 7}
print(a.__iand__(b)) #{3}
print(a) #{3}