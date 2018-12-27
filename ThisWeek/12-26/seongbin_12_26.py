def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

coro_avg = averager()
print(next(coro_avg))
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))


from functools import wraps

def coroutine(func):
    """데커레이터: 'func'를 기동해서 첫 번째 'yield'까지 진행한다."""
    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
coro_avg2 = averager()
from inspect import getgeneratorstate
print(getgeneratorstate(coro_avg2))
print(coro_avg2.send(10))
print(coro_avg2.send(30))
print(coro_avg2.send(5))
