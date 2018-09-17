"""
created by jingu Kang on 2018-09-17

deque examples
"""

from collections import deque

# play with deque
dq = deque(range(10), maxlen=100)
dq1 = deque(range(10), maxlen=10)
print(dq)
#deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=100)

dq.extend([11,22,33])
print(dq)
#deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=100)

dq1.extend([11,22,33])
print(dq1)
#deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10) 익스텐드라서 늘어나는 줄 알았더만 그냥 앞에거 밀어냄.

dq.rotate(3)
print(dq)
#deque([11, 22, 33, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=100)

dq.rotate(-4)
print(dq)
#deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 0], maxlen=100)

dq.extend([i+1 for i in range(90)])
print(dq)
print(len(dq))
#deque([4, 5, 6, 7, 8, 9, 11, 22, 33, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], maxlen=100)

# where should I use deque? some where num of container is fixed...
thingsToDoToday = deque(['Python Study','ML study','Experiments'], maxlen=8)

# priority high but not urgent
thingsToDoToday.append('new assignments')
thingsToDoToday.append('new command of my professor')

# important but not urgent
for things in ['learn linear Algebra','learn speech enhancement','learn physics','go to library']:
    if len(thingsToDoToday) != thingsToDoToday.maxlen:
        thingsToDoToday.appendleft(things)

print("You should do %s now" % thingsToDoToday[-1])
#You should do new command of my professor now
print(thingsToDoToday)
#deque(['learn physics', 'learn speech enhancement', 'learn linear Algebra', 'Python Study', 'ML study', 'Experiments', 'new assignments', 'new command of my professor'], maxlen=8)