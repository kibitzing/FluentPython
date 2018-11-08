#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 08/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        practice using protocol(sequence)
"""
import reprlib

class Duty: # 당번
    members = ['진구', '대하','근회','승현','성빈','지윤','상홍']

    def __init__(self, dutyname):
        self.dutyname = dutyname
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def __repr__(self):
        duty = reprlib.repr(self.dutyname + ' 당번 ')
        return duty

    def __str__(self):
        return str(self.dutyname+' 당번')

    def __len__(self):
        return(len(self.members))

    def __getitem__(self, date):
        days_counter = [(v, c) for c,v in enumerate(self.days)]
        day_mem_dict = dict(days_counter)
        return '오늘의 ' + str(self) + ": " + str(self.members[day_mem_dict[date]])

duty_fine = Duty('벌금 기록')
duty_git_manage = Duty('깃허브 관리')
duty_git_manage.days.reverse()

print(duty_fine['Monday']) # 오늘의 벌금 기록 당번: 진구
print(duty_git_manage['Monday']) # 오늘의 깃허브 관리 당번: 상홍

