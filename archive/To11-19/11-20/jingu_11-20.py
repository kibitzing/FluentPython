#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 20/11/2018.
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

@Friend.register
class normalFriend(Friend):
    def __init__(self):
        self.isFriend = True

    def knowMyHabit(self):
        print('연구실에 오래 있음.')

    def contactMe(self):
        print('이메일을 보낸다.')

@Friend.register
class fakeFriend(Friend):
    def __init__(self):
        self.isFriend = False

    def knowMyHabit(self):
        print('사실 모름')

    def contactMe(self):
        print('안함')


fF = fakeFriend()
oF = oldFriend()
nF = normalFriend()
print(issubclass(oldFriend, Friend))
print(issubclass(normalFriend, Friend))
print(issubclass(fakeFriend, Friend))

print(isinstance(oF, Friend))
print(isinstance(nF, Friend))
print(isinstance(fF, Friend))
# but all True
