#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 26/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        try Mixin Class
"""


# Mixin class에는 메서드만 있다.
# 코드 재활용을 위해 사용한다.

import collections

class greetingMixin():
    def printHi0(self):
        print('hi0')

    def printHi1(self):
        print('hi1')

    def printHi2(self):
        print('hi2')

    def printHi3(self):
        print('hi3')

    def printHi4(self):
        print('hi4')

    def printHi5(self):
        print('hi5')

    def printHi6(self):
        print('hi6')

    def printHi7(self):
        print('hi7')

    # 보통 믹스인 클래스에는 이렇게 많은 코드가 들어온다.

class hiMan(greetingMixin, collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

class helloMan(greetingMixin): # , collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)
# 믹스인 클래스만 상속해도 되긴 된다.


man = hiMan()
man2 = helloMan()

man.printHi0() # hi0
man2.printHi7() #hi7
