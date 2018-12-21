#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 20/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        used exception to implement demo version summer.
"""
class DemoException(Exception):
    """An exception type for the demonstration"""

def demo_summer_finally():
    print('-> coroutine started.')
    total = 0
    try:
        while True:
            try:
                term = yield
                if term is None:
                    break
                total += term

            except DemoException:
                print('*** DemoException handled. Continueing....')

            except StopIteration:
                print('*** StopIteration handled. Continueing....')

            else:
                print('coroutine received : {!r}'.format(total))

    finally:
        return total
        print('-> coroutine ending')


exc_coro = demo_summer_finally()
next(exc_coro)
exc_coro.send(11)
exc_coro.send(22)
exc_coro.send('hi')
exc_coro.send(44)
exc_coro.send(None)
exc_coro.close()
