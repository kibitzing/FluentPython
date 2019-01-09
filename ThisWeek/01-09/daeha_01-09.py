#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" asyncio의 코루틴을 사용한 동시성 예제

"""
import asyncio
import itertools
import sys

@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))
    
@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(5)
    return 29

@asyncio.coroutine
def supervisor():
    spinner = asyncio.async(spin('thinking!'))
    print('spinner object: ', spinner)
    results = yield from slow_function()
    spinner.cancel()
    return results


def main():
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer: ', results)
    
    
if __name__ == '__main__':
    main()