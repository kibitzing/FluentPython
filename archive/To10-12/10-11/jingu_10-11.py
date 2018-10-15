"""
created by jingu kang on 2018-10-11
coding: utf-8
"""

from functools import reduce
from operator import add

def factorial(n):
    """returns n!"""
    return 1 if n<2 else n*factorial(n-1)

mapped = list(map(factorial, range(5)))
mapped2 = [factorial(i) for i in range(5)]

print(mapped == mapped2)
print(mapped)
print(mapped2)

filteredMapped = list(map(factorial, filter(lambda n: n%2, range(6))))
filteredMapped2 = [factorial(i) for i in range(6) if i%2]
print(filteredMapped)
print(filteredMapped2)
print(filteredMapped == filteredMapped2)


summed = reduce(add, range(6))
summed2 = sum(range(6))
print(summed)
print(summed2)
print(summed==summed2)

fruits = ['strawberry', 'blueberry' , 'apple', 'cherry', 'turky', 'dizzy']

def reverse(word):
    return word[::-1]

print(sorted(fruits, key=reverse))
print(sorted(fruits, key=lambda word:word[::-1]))

abs, str, 13
print([callable(i) for i in (abs,str,13)])

## 결론: 파이썬3는 계속해서 발전 했고, 그래서 전에 많이 쓰던 map, filter, reduce은 대체되었다. 람다도 가독성이 떨어져 잘 안쓴다.