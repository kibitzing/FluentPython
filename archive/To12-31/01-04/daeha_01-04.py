#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Multi-thread를 알아보는 예제

# original source:
# https://github.com/Hezi-Resheff/Oreilly-Learning-TensorFlow/blob/master/08__queues_threads/queue_basic.py

"""
from __future__ import print_function

import tensorflow as tf

import threading
import time

### 1) 기본 thread 예제
# run ses sion
sess = tf.InteractiveSession()

gen_random_normal = tf.random_normal(shape=())
queue = tf.FIFOQueue(capacity=100, dtypes=[tf.float32], shapes=())
enque = queue.enqueue(gen_random_normal)

def add():
    for i in range(10):
        sess.run(enque)
        

threads = [threading.Thread(target=add, args=()) for i in range(10)]
for t in threads:
    t.start()
    
print(sess.run(queue.size()))
time.sleep(0.001)
print(sess.run(queue.size()))
time.sleep(0.001)
print(sess.run(queue.size()))

sess.close()

# 21
# 56
# 100

### 2) Tensorflow의 thread control을 가능하게 해주는 tf.train.Coordinator를 사용하는 예제

# run session
sess = tf.InteractiveSession()

gen_random_normal = tf.random_normal(shape=())
queue = tf.FIFOQueue(capacity=100, dtypes=[tf.float32], shapes=())
enque = queue.enqueue(gen_random_normal)

def add_advanced(coord, i):
    while not coord.should_stop():
        sess.run(enque)
        if i == 11:
            coord.request_stop()
            
            
coord = tf.train.Coordinator()
threads = [threading.Thread(target=add_advanced, args=(coord, i)) for i in range(10)]
coord.join(threads)
for t in threads:
    t.start()
    
print(sess.run(queue.size()))
time.sleep(0.01)
print(sess.run(queue.size()))
time.sleep(0.01)
print(sess.run(queue.size()))

sess.close()  ###

# 에러 발생!
# 왜냐하면 앞의 add와 달리 add_advance는 request_stop()으로 tensorflow의 session을 종료시킴!
# CancelledError (see above for traceback): Enqueue operation was cancelled

### 3) tf.train.QueueRunner를 이용한 multi-threading 예제

sess = tf.InteractiveSession()

gen_random_normal = tf.random_normal(shape=())
queue = tf.RandomShuffleQueue(capacity=100, dtypes=[tf.float32],
                              min_after_dequeue=1)
enqueue_op = queue.enqueue(gen_random_normal)

qr = tf.train.QueueRunner(queue, [enqueue_op] * 10)
coord = tf.train.Coordinator()
enqueue_threads = qr.create_threads(sess, coord=coord, start=True)

print(sess.run(queue.size()))
time.sleep(0.01)
print(sess.run(queue.size()))
time.sleep(0.01)
print(sess.run(queue.size()))