#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 코루틴 예제

    python 2.5
    
    refer below link:
    https://github.com/CreatCodeBuild/TensorFlow-and-DeepLearning-Tutorial/blob/master/PythonTips/coroutine.py

"""
import socket
import time
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()


class Future:
    
    def __init__(self):
        self.callbacks = []
        
    def resolve(self):
        for func in self.callbacks:
            func()


class Task:
    
    def __init__(self, gen, eventLoop):
        self.gen = gen
        self.step()
        
    def step(self):
        try:
            f = next(self.gen)
            f.callbacks.append(self.step)
        except StopIteration as e:
            eventLoop.n_task -= 1
            
            
class EventLoop:
    
    def __init__(self):
        self.n_task = 0
        
    def add_task(self, generator):
        self.n_task += 1
        Task(generator, self)
        
    def start(self):
        while self.n_task > 0:
            events = selector.select()
            for event, mask in events:
                f = event.data
                f.resolve()
                

def pause(s, event):
	f = Future()
	selector.register(s.fileno(), event, data=f)
	yield f		# pause this function


def resume(s):
	selector.unregister(s.fileno())


def async_await(s, event):
	yield from pause(s, event)
	resume(s)


def async_get(path):
	s = socket.socket()
	s.setblocking(False)
	try:
		s.connect(('localhost', 3000))
	except BlockingIOError as e:
		print(e)

	yield from async_await(s, EVENT_WRITE)

	request = 'GET %s HTTP/1.0\r\n\r\n' % path
	s.send(request.encode())

	totalReceived = []
	while True:
		yield from async_await(s, EVENT_READ)

		received = s.recv(1000)
		if received:
			totalReceived.append(received)
		else:
			body = (b''.join(totalReceived)).decode()
			print('--------------------------------------')
			print(body)
			print('--------------------------------------', 'Byte Received:', len(body), '\n\n')


if __name__ == '__main__':
    start = time.time()
    eventLoop = EventLoop()
    
    for i in range(10):
        eventLoop.add_task(async_get('/super-slow'))
        
    eventLoop.start()
    
    print('{}'.format(time.time() - start))