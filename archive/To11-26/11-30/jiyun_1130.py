# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 18:47:56 2018

@author: jiyun
"""
from Vector import Vector
from Vector2d import Vector2d
va = Vector([1,2,3])
vz = Vector([5,6,7])

#def __matmul__(self, other):
#    try:
#        return sum(a*b for a,b in zip(self, other))
#    except TypeError:
#        return NotImplemented
#    
#def __rmatmul__(self, other):
#    return self@other

print(va @ vz) #38.0
print(vz @ vz) #110.0
 
#def __eq__(self, other):
#    if isinstance(other, Vector):
#        return (len(self) == len(other) and all (a==b for a,b in zip(self,other)) )
#    else:
#        return NotImplemented

vb = Vector(range(1,4))
print(va == vb) #True
t3 = (1,2,3)
print(va == t3) #False 두 객체의 ID 비교 결과

#def __ne__(self, other):
#    eq_result = self == other
#    if eq_result  is NotImplemented:
#        return NotImplemented
#    else:
#        return not eq_result

print(va != vb) #False
print(va != (1,2,3)) #True
 
"""
복합 할당 연산자
"""

va_alias = va #별명 할당 id(va) :  2616361733032
va += vb
print(va) #(2.0, 4.0, 6.0) id(va) : 2616361730736 (객체 새로 생성됨)
print(va_alias) #(1.0, 2.0, 3.0) 원래 객체 변화X


