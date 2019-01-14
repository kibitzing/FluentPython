#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" multi-threading을 활용한 동시성 사용 예제 

"""
import threading
import itertools
import time, sys

class Signal:
    go = True
    

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))
    
    
def slow_function():
    time.sleep(5)
    return 29


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


def main():
    result = supervisor()
    print('Answer:', result)
    
    
if __name__ == '__main__':
    main()