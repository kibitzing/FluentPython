# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 13:54:16 2019

@author: jiyun
"""
# 원서 기준 544~548

import asyncio
import itertools
import sys

@asyncio.coroutine
def spin(msg): # 스레드 종료를 위한 변수 필요없음
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' '+ msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(0.1)
        except asyncio.CancelledError: # 예외 처리로 안전하게 취소 가능
            break
    write(' '*len(status) + '\x08' * len(status))

@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3) # 메인 루프의 제어 흐름 처리
    return 42

@asyncio.coroutine
def supervisor():
    spinner = asyncio.async(spin('thinking!')) # Task 객체 (spinner) 반환
    print('spinner object : ', spinner) 
    result = yield from slow_function()
    # 이벤트 루프는 계속 실행중
    # (slow_function에서 asyncio.sleep을 통해 제어권 메인 루프로 넘겨줌)
    spinner.cancel()
    return result

def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor()) # supervisor() 코루틴 구동 
    loop.close()
    print('Answer : ', result)
    
if __name__ == '__main__':
    main()
    
#spinner object :  <Task pending coro=<spin() running at 0109.py:13>>
#Answer :  42
################ 예제 18-1과 비교 ################
#spinner object: <Thread(Thread-1, initial)>
#Answer: 42     

