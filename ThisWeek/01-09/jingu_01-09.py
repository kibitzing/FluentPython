#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 09/01/2019.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        수영하는 사람 애니메이션.
        simple modification from example 18-2
"""
import asyncio
import itertools
import sys

@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('ㄱㅡㅇㄷㅡ'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))

@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(5)
    return '1등'

@asyncio.coroutine
def supervisor():
    spinner = asyncio.async(spin('Swimming!'))
    print('spinner object:', spinner)
    result = yield from slow_function()
    spinner.cancel()
    return result

def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('등수:', result)

if __name__ == '__main__':
    main()
