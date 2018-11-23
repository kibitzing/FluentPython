#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 23/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        상속 흐름 제어 연습
"""

class Friend():
    def greeting(self):
        print('hi')

class GoodFriend(Friend):
    def greeting(self):
        print('yo man')

class BestFriend(Friend):
    def greeting(self):
        print('yo yo yo')

class AFriend(GoodFriend, BestFriend):
    def bye(self):
        print('bye')

class BFriend(BestFriend, GoodFriend):
    def bye(self):
        print('bye')

jay_z = AFriend()
jay_z.greeting()

Beyonce = BFriend()
Beyonce.greeting()

