#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 19/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        
"""

import abc
class Friend(abc.ABC):
    @abc.abstractmethod
    def knowMyHabit(self):
        """
        친구는 나의 습관을 안다.
        :return:
        """
    @abc.abstractmethod
    def contactMe(self):
        """
        친구는 연락을 한다.
        :return:
        """

    def isFriend(self):
        return bool(self.isFriend)

class oldFriend(Friend):
    def __init__(self):
        self.isFriend = True

    def knowMyHabit(self):
        print('주말마다 집에감')
        print('연구실에 오래 있음')

    def contactMe(self):
        print('전화를 건다.')

class normalFriend(Friend):
    def __init__(self):
        self.isFriend = True

    def knowMyHabit(self):
        print('연구실에 오래 있음.')

    def contactMe(self):
        print('이메일을 보낸다.')

class fakeFriend(Friend):
    def __init__(self):
        self.isFriend = False


a = oldFriend()
b = normalFriend()

a.contactMe()
a.knowMyHabit()

b.contactMe()
b.knowMyHabit()

# c = fakeFriend() TypeError: Can't instantiate abstract class fakeFriend with abstract methods contactMe, knowMyHabit
