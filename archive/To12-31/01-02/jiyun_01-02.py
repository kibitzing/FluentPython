# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 18:17:34 2019

@author: jiyun
"""

#원서 기준 512~516p

from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20 # 최대 스레드 수

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image,cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS,len(cc_list)) # 불필요한 스레드 생성하지 않도록
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
        # map 메서드 : 제너레이터 반환
        
    return len(list(res))

def download_many_2(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers = 5) as executor: # 대기중인 객체 확인하려면 5보다 적은 수
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one,cc)
            to_do.append(future) # future 객체 저장
            msg = 'Scheduled for {}:{}'
            print(msg.format(cc,future))
            
        results = []
        for future in futures.as_completed(to_do):
            # as_completed() : future 완료 시 해당 future 객체 생성
            res = future.result()
            msg = '{} result : {!r}'
            print(msg.format(future,res))
            results.append(res)
            
    return len(results)
            
if __name__ == '__main__':
    main(download_many)    
#############################################################     
#   BDCNTRIDBRDEVNRUNG FR ET  KR   US PK PHMXEG        IR CD IN 
#   20 flags downloaded in 1.385020s
#############################################################    
    main(download_many_2)
#############################################################
#    Scheduled for BR:<Future at 0x1f54a3111d0 state=running>
#    Scheduled for CN:<Future at 0x1f54a311748 state=running>
#    Scheduled for ID:<Future at 0x1f54a348860 state=running>
#    Scheduled for IN:<Future at 0x1f549993160 state=running>
#    Scheduled for US:<Future at 0x1f549993dd8 state=running>
#    BR <Future at 0x1f54a3111d0 state=finished returned str> result : 'BR'
#    CNIN  <Future at 0x1f549993160 state=finished returned str> result : 'IN'
#    <Future at 0x1f54a311748 state=finished returned str> result : 'CN'
#    ID <Future at 0x1f54a348860 state=finished returned str> result : 'ID'
#    US <Future at 0x1f549993dd8 state=finished returned str> result : 'US'
#
#    5 flags downloaded in 0.374900s
#############################################################    