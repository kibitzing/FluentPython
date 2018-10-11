import time
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)
def double(n):
    return n*2
print (factorial(42))

fact = factorial

t = time.time()
a = list(map(double, filter(lambda n: n % 2, range(100000))))
print (time.time()-t)

t = time.time()
b = [double(n) for n in range(100000) if n % 2]
print (time.time()-t)

## 책에 나와 있듯이 comprehensive가 더 좋음

import tensorflow as tf
slim = tf.contrib.slim
