#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 30/10/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 


"""
import copy

class StudyMember:
    moneyForMeeting = 0

    def __init__(self, name=''):
        self.name = name
        self.deposit = 10000

    def absence(self):
        self.deposit -= 1000
        StudyMember.moneyForMeeting += 1000
        if self.deposit is 0:
            print('alert, no more deposit')

    def charge(self):
        self.deposit = 10000

seongbin = StudyMember('seongbin')
jingu = copy.copy(seongbin)
jingu.name = 'jingu'

seunghyun = copy.copy(seongbin)
seunghyun.name = seunghyun.name[:2] + 'unghyun'
print(seongbin.name) #seongbin
print(jingu.name) #jingu
print(seunghyun.name) #seunghyun

seunghyun.name = list(seunghyun.name)[:1]
sanghong = copy.copy(seunghyun)

sanghong.name += ['a','n','g','h','o','n','g']
sanghong.name = ''.join(sanghong.name)
seunghyun.name = ''.join(seunghyun.name)
print(sanghong.name) #sanghong
print(seunghyun.name) #sanghong

