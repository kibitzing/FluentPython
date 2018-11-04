#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 01/11/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        리터럴만 되는 게 신기하다..?! 튜플을 스트링으로 만들어서 해도 인터닝이 일어날까?
        일어나지 않는다. 왜?!! 이미 다른 곳에 있으면 당연히 다르다고 생각하고 다르게 만드는 것 같다.
        see #6 and #7
"""

t1 = (1,2,3)
t2 = tuple(t1)

print('#1')
print(t2 is t1)

t3 = t1[:]
print('#2')
print(t3 is t1)

t4 = (1,2,3)
t5 = (1,2,3)
print('#3')
print(t4 is t5)

t4_2 = str(t4)
t5_2 = str(t5)
print('#4')
print(id(t4_2), id(t5_2)) # 4430830960 4430857328
print(t4_2 + " is " + t5_2 + "?")
print(t4_2 is t5_2)


t4_3 = str((1,2,3))
t5_3 = str((1,2,3))
print(id(t4_3), id(t5_3)) # 4430858224 4430858288
print('#5')
print(t4_3 + " is " + t5_3 + "?")
print(t4_3 is t5_3)
print(type(t4_3))

str_x = str((1,2,3))
t4_4 = str_x
t5_4 = str_x
print('#6')
print(id(t4_4), id(t5_4)) # 4554318960 4554318960
print(t4_4 + " is " + t5_4 + "?")
print(t4_4 is t5_4)
print(type(t4_4))

t6 = '(1,2,3)'
t7 = '(1,2,3)'
print('#7')
print(id(t7), id(t6)) # 4429375472 4429375472
print(t6 + " is " + t7 + "?")
print(t6 is t7)
print(type(t6))