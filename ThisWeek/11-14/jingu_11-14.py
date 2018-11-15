#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 14/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION:
        ~와 같은 객체
        ~ 프로토콜
        ~ 인터페이스

            다 같은 말이다. 그래서 더 이해가 아직은 잘 가지 않는다.
            인터페이스: 클래스가 상속하거나/구현하거나 한 공개속성들의 집합.
             즉, 부를 수 있는것 전부!
"""
from textwrap import wrap

class Friends:

    def __init__(self, f_list):
        self.friend_list = f_list

    def __getitem__(self, item):
        return self.friend_list[item]
# __getitem__만 구현해도

pythonStudy = Friends(wrap('근회진구대하승현상홍성빈지윤',2))

print(pythonStudy[1])
print('진구' in pythonStudy)

k = 0
for member in pythonStudy:
    k = k + 1
    print('{} : {}'.format(k, member))

## __contain__ 과 __iter__ 이 따라온다..!
## 시퀀스 인터페이스, 시퀀스같은 객체가 되기 때문..!