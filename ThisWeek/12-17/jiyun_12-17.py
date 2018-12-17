# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 22:19:15 2018

@author: jiyun
"""

# 원서 기준 449~453p

with open('mirror.py') as fp:
    src = fp.read(60)
    
print(len(src)) #60
print(fp) # 변수로 살아있음
print(fp.closed, fp.encoding) # 속성 읽기 가능
#print(fp.read(60)) # 파일 닫아서 입출력은 불가능

from mirror import LookingGlass
with LookingGlass() as what:
    print('ABCDEFGHIGKLMNOPQRSTUVWXYZ') # ZYXWVUTSRQPONMLKGIHGFEDCBA
    print(what) # YKCOWREBBAJ
    
print(what) # enter가 반환한 JABBERWOCKY
print('ABCDEFGHIGKLMNOPQRSTUVWXYZ') # ABCDEFGHIGKLMNOPQRSTUVWXYZ


"""
class LookingGlass:
    
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'
    
    def reverse_write(self, text):
        self.original_write(text[::-1])
        
    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('DO NOT divide by 0')
            return True
"""