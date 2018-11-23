#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 다중 상속과 메서드 결정 순서를 정하는 예제
    
    pages 443~447; 한글 기준
"""


class A:
    def ping(self):
        print('ping:', self)
        
class B(A):
    def pong(self):
        print('B-pong:', self)
        
class C(A):
    def pong(self):
        print('C-pong:', self)
        
        
class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)
        
    def pingpong(self):
        self.ping()     # D.ping() 출력                         - (1)
        super().ping()  # D.ping() 대신 A.ping() 출력            - (2)
        self.pong()     # __mro__에 따라 B.pong() 출력            - (3)
        super().pong()  # 마찬가지로 __mro__에 따라 B.pong() 출력   - (4)
        C.pong(self)    # __mro__를 무시하고 C.pong() 출력         - (5) 
        
d = D()
d.pong()  # B-pong: <__main__.D object at 0x117a84898>
C.pong(d)  # C-pong: <__main__.D object at 0x117a84898>

### 메서드 결정 순서; Method Resolution Order (MRO)
# 클래스에 있는 __mro__ 속성은 현재 클래스로부터 object 클래스까지 슈퍼클래스들의
# MRO를 tuple 형태로 저장한다.

D.__mro__  # (__main__.D, __main__.B, __main__.C, __main__.A, object)


d.ping()  # ping: <__main__.D object at 0x117a84898>
          # A.ping이 출력한 것
          # post-ping: <__main__.D object at 0x117a84898>
          # 그 다음 print문이 출력한 것
          
d.pingpong()  # (self.ping())                                   - (1)
              # ping: <__main__.D object at 0x117a84898>
              # post-ping: <__main__.D object at 0x117a84898>
              
              # (super().ping())                                - (2)
              # ping: <__main__.D object at 0x117a84898>
              
              # (self.pong())                                   - (3)
              # B-pong: <__main__.D object at 0x117a84898>
              
              # (super().pong())                                - (4)
              # B-pong: <__main__.D object at 0x117a84898>
              
              # (C.pong(self))                                  - (5)
              # C-pong: <__main__.D object at 0x117a84898>