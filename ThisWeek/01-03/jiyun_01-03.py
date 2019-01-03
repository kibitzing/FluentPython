# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:04:37 2019

@author: jiyun
"""
# 원서 기준 517~521p

from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20 # 최대 스레드 수

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    with futures.ProcessPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))
        # map 메서드 : 제너레이터 반환

    return len(list(res))

if __name__ == '__main__':
    main(download_many)

#BD BR DE CN CD EG FR ET ID IN NG PK MX PH IR KR RU TR VN US
#20 flags downloaded in 1.380889s

#########################################################################
    
from time import sleep, strftime

def display(*args):
    print(strftime('[%H:%M:%S]'), end = ' ')
    print(*args)
    
def loiter(n):
    msg = '{}loiter({}) : doing nothing for {}s...'
    display(msg.format('\t'*n,n,n))
    sleep(n)
    msg = '{}loiter({}): done'
    display(msg.format('\t'*n,n))
    return n*10

def main():
    display('Srcript starting')
    executor = futures.ThreadPoolExecutor(max_workers = 3)
    results = executor.map(loiter,[0,1,2,4]) # map : 논블로킹 메서드, 호출한 순서 그대로 반환
    display('results:', results) # 반환값 바로 출력
    display('Waiting for individual results:')
    for i, result in enumerate(results): 
        # for 루프 안에서 enumerate -> 암묵적 next()호출
        # __next__() 메서드는 전 future 객체가 완료될 때 까지 대기
        display('results {}: {}'.format(i,result))
        
main()
#[17:13:50] Srcript starting
#[17:13:50] loiter(0) : doing nothing for 0s...
#[17:13:50] loiter(0): done
#[17:13:50]      loiter(1) : doing nothing for 1s...
#[17:13:50]              loiter(2) : doing nothing for 2s...   # 스레드 3개이므로 2까지 바로 실행
#[17:13:50] results: <generator object Executor.map.<locals>.result_iterator at 0x000001E03D96B780>
#[17:13:50] Waiting for individual results:
#[17:13:50] results 0: 0
#[17:13:50]                              loiter(4) : doing nothing for 4s...   # loiter(0)이 done 이므로 실행
#[17:13:51]      loiter(1): done
#[17:13:51] results 1: 10
#[17:13:52]              loiter(2): done
#[17:13:52] results 2: 20
#[17:13:54]                              loiter(4): done
#[17:13:54] results 3: 40