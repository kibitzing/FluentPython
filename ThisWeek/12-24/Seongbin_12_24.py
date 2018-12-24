def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:',x)

my_coro = simple_coroutine()
print(my_coro)
next(my_coro)
my_coro.send(42)
my_coro.send(1729)

def simple_coro2(a):
    print('-> Started: a = ',a)
    b = yield a
    print('-> Received: b = ',b)
    c = yield a+b
    print('-> Received: c = '.c)

my_coro2 = simple_coro2(14)
from inspect import getgeneratorstate

print(getgeneratorstate(my_coro2))
next(my_coro2)
print(getgeneratorstate(my_coro2))
my_coro2.send(28)
my_coro2.send(99)
print(getgeneratorstate(my_coro2))
    
