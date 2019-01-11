# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 20:33:26 2019

@author: jiyun
"""
# 원서 기준 554~559p

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

@asyncio.corountine
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
def download_one(cc, base_url, semaphore, verbose): # semaphore는 동시 요청 수를 제한하기 위함
    try:
        with(yield from semaphore):
            image = yield from get_flag(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'
        
    if verbose and msg:
        print(cc,msg)
        
    return Result(status,cc)
        

