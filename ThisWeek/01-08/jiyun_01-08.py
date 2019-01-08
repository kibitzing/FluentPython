# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:17:51 2019

@author: jiyun
"""
# 원서기준 539~543p

import threading
import itertools
import time
import sys

class Signal:
    go = True
    
def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' +msg
        write(status)
        flush()
        write('\x08' * len(status)) # backspace
        time.sleep(0.1)
        if not signal.go:
            break
    write(''*len(status) + '\x08' * len(status))
    
def slow_function():
    time.sleep(3)
    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target = spin, args = ('thinking!', signal))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function() # 메인 스레
    signal.go = False
    spinner.join() # spinner 스레드 종료 시 까지 대기
    return result

def main():
    result = supervisor()
    print('Answer:', result)
    
if __name__ == '__main__':
    main()
    
    
