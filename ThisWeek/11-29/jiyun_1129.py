# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:54:48 2018

@author: jiyun
"""
from Vector import Vector
from Vector2d import Vector2d


v1 = Vector([3,4,5])

print(v1 + (1,2,3))
v2d = Vector2d(1,2)
print(v1 + v2d)
  
#    def __radd__(self,other):
#        return self+other

print(v2d + v1) # 역순 메서드 구현

#    def __add__(self, other):
#        try:
#            pairs = itertools.zip_longest(self, other, fillvalue = 0.0)
#            return Vector(a + b for a,b in pairs)
#        except TypeError:
#            return NotImplemented
#        
#    def __radd__(self,other):
#        return self+other

#print(v1 + 1) 
# NotImplemented 반환 ->  TypeError: unsupported operand type(s) for +: 'Vector' and 'int'

"""
* 오버로딩
"""

#    def __mul__(self, scalar):
#        return Vector(n*scalar for n in self)
#    
#    def __rmul__(self, scalar):
#        return self*scalar

print(v1*25)
print(100*v1)


 