#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 09/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        __getitem__, __len__  추가.
"""
import reprlib
import numbers


class Duty: # 당번
    members = ['진구', '대하','근회','승현','성빈','지윤','상홍']
    counter = 0

    def __init__(self, dutyname):
        self.dutyname = dutyname
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        Duty.counter = Duty.counter + 1

    def __repr__(self):
        duty = reprlib.repr(self.dutyname + ' 당번 ')
        return duty

    def __str__(self):
        return str(self.dutyname+' 당번')

    def __len__(self):
        return(Duty.counter)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, str):
            days_counter = [(v, c) for c,v in enumerate(self.days)]
            day_mem_dict = dict(days_counter)
            return '오늘의 ' + str(self) + ": " + str(self.members[day_mem_dict[index]])

        elif isinstance(index, numbers.Integral):
            return self.members[index]

        elif isinstance(index, slice):
            return self.members[index]

        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

duty_fine = Duty('벌금 기록')

print(len(duty_fine)) # 몇개의 벌금이 있는지로도 구현해 보았다.

duty_git_manage = Duty('깃허브 관리')
duty_git_manage.days.reverse()

print(duty_fine['Monday']) # 오늘의 벌금 기록 당번: 진구
print(duty_git_manage['Monday']) # 오늘의 깃허브 관리 당번: 상홍
print(len(duty_git_manage))

print(duty_fine[1]) # 대하
print(duty_fine[-1]) # 상홍
print(duty_fine[:]) # ['진구', '대하', '근회', '승현', '성빈', '지윤', '상홍']
print(duty_fine[2:4]) # ['근회', '승현']
print(duty_fine[1,2]) # TypeError: Duty indices must be integers

