# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:08:33 2019

@author: jiyun
"""
# futures.as_completed() 예제

from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from time import sleep
 
def return_after_5_secs(num):
    sleep(3)
    return "Result : {}".format(num)
 
pool = ThreadPoolExecutor(5)
futures = []
for x in range(5):
    futures.append(pool.submit(return_after_5_secs, x))
    
 
for x in as_completed(futures): # 완료되는 순서대로
    print(x.result())
    # timeout = 3 으로 설정 시  TimeoutError: 5 (of 5) futures unfinished

print(wait(futures, timeout = 3)) 
#DoneAndNotDoneFutures(done={<Future at 0x191b0813c18 state=finished returned str>,
#                            <Future at 0x191b07c94a8 state=finished returned str>,
#                            <Future at 0x191b0830cc0 state=finished returned str>,
#                            <Future at 0x191b07c95c0 state=finished returned str>},
#                  not_done={<Future at 0x191b07fbf28 state=running>})

