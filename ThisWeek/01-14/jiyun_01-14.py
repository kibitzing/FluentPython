# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:24:30 2019

@author: jiyun
"""
#원서 기준 560~564p

import asyncio
import collections
import aiohttp
from aiohttp import web
import tqdm

from flags2_common import main, HTTPStatus, Result, save_flag

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000

class FetchError(Exception): # 예외 클래스 정의
    def __init__(self, country_code):
        self.country_code = country_code

@asyncio.coroutine
def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    if resp.status == 200:
        image = yield from resp.read()
        return image
    elif resp.status == 404:
        raise web.HTTPNotFound()
    else:
        raise aiohttp.HttpProcessingError(
                code = resp.status, message = resp.reason,
                headers = resp.headers)

@asyncio.coroutine
def download_one(cc, base_url, semaphore, verbose): # 예제 18-9 버전
    try:
        with(yield from semaphore):
            image = yield from get_flag(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_flag, image, cc.lower() + '.gif')
#        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'
        
    if verbose and msg:
        print(cc,msg)
        
    return Result(status,cc)
################################################################## 이어서
@asyncio.coroutine
def downloader_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req) # 코루틴 동시 실행 가능한 개수 정해주는 Semaphore
    to_do = [download_one(cc, base_url, semaphore, verbose)
            for cc in sorted(cc_list)]
    to_do_iter = asyncio.as_completed(to_do)
    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total = len(cc_list))
    
    for future in to_do_iter:
        try:
            res = yield from future
        except FetchError as exc:
            country_code = exc.country_code
            try:
                error_msg = exc.__cause__.args[0]
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:
                msg = '*** Error for {} : {}'
                print(msg.format(country_code, error_msg))
            status = HTTPStatus.error
        else:
            status = res.status
        
        counter[status] += 1
    return counter

def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro) # 이벤트 루프에 전
    loop.close()
    
    return counts

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
    
# Python 3.5 부터 yield from이 await으로 대체 되었지만 대다수 비동기 라이브러리들은
# 하위 호환성을 위해 아직 yield from 사용    
