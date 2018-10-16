# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:12:21 2018

@author: jiyun
"""
from inspect import signature

def clip(text:str, max_len:'int > 0' = 80) -> str:
    end = None
    if len(text) > max_len:
        space_before= text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


print(clip.__defaults__)
print(clip.__code__.co_argcount)

sig = signature(clip)
print(sig)

for name,param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
    
print(clip.__annotations__)
print(sig.return_annotation)

for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)

##################################################################
    
from functools import reduce
from operator import mul

def fact(n):
    return reduce(lambda a, b:a*b, range(1,n+1))
def fact_mul(n):
    return reduce(mul, range(1,n+1))

print(fact(4))
print(fact_mul(4))

##################################################################

from operator import itemgetter, attrgetter
        
student =[('Kim', '12181265', '20', 'B'),
          ('Park', '12171415', '21', 'A'),
          ('Kang', '12131514', '25', 'D'),
          ('Choi', '12161417', '22', 'C')]

for age in sorted(student, key = itemgetter(2)):
    print(age)
    
class Student:
    def __init__(self,name,studentID, age, grade):
        self.name = name
        self.studentID = studentID
        self.age = age
        self.grade = grade
    def __repr__(self):
        return repr((self.name, self.studentID, self.age, self.grade))
        
class3 = [Student('Kim', '12181265', '20', 'B'),
          Student('Park', '12171415', '21', 'A'),
          Student('Kang', '12131514', '25', 'D'),
          Student('Choi', '12161417', '22', 'C')]
    
for student in sorted(class3, key = attrgetter('grade')):
    print(student)
