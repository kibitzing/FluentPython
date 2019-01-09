#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p542-546
# Example 18-2~4

'''
	concurrent 문서 참고.
'''

import asyncio
import itertools
import sys

# Example 18-2
@asyncio.coroutine
def spin(msg):
	write, flush = sys.stdout.write, sys.stdout.flush
	for char in itertools.cycle('|/-\\'):
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
	# pretend waiting a long time for I/O
	yield from asyncio.sleep(3)
	return 42

@asyncio.coroutine
def supervisor():
	spinner = asyncio.async(spin('thinking!'))
	print('spinner object:', spinner)
	result = yield from slow_function()
	spinner.cancel()
	return result

def main182():
	loop = asyncio.get_event_loop()
	result = loop.run_until_complete(supervisor())
	loop.close()
	print('Answer:', result)

# Example 18-3
def supervisor():
	signal = Signal()
	spinner = threading.Thread(target=spin,
	args=('thinking!', signal))
	print('spinner object:', spinner)
	spinner.start()
	result = slow_function()
	signal.go = False
	spinner.join()
	return result

# Example 18-4
@asyncio.coroutine
def supervisor():
	spinner = asyncio.async(spin('thinking!'))
	print('spinner object:', spinner)
	result = yield from slow_function()
	spinner.cancel()
	return result

if __name__ == '__main__':
	print('{0:=<50}'.format("Example 18-2"))
	main182()
