#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

""" 파이썬 추상 클래스를 사용하는 예제
    파이썬은 추상 클래스라는 기능을 제공한다.
    추상 클래스는 클래스의 다형성을 위해 사용할 수 있다.
    또한 추상 클래스는 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용할 수 있다.
"""

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
 
    @abstractmethod
    def go_to_school(self):
        pass
    
    
class Student(StudentBase):
    def study(self):
        print('열공하기!')
        
dd = Student()
dd.study()  

# TypeError: Can't instantiate abstract class Student with abstract methods go_to_school
# StudentBase를 상속받은 Student에서는 study 메서드만 구현하고, 
# go_to_school 메서드는 구현하지 않았으므로 에러가 발생한다!!!

class Student(StudentBase):
    def study(self):
        print('열공하기!')
 
    def go_to_school(self):
        print('늦잠잔 뒤에 학교 천천히 가기')
        
dd = Student()
dd.study()
dd.go_to_school()

# 예제와 같이 추상 클래스는 파생 클래스가 반드시 구현해야 하는 메서드를 정해줄 수 있다.


