#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 11/01/2019.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
      add error handling to asyncio,
      error handled, but 'unclosed client session' happens        
"""

import asyncio
import collections
import aiohttp
import requests
from aiohttp import web
import tqdm
from flags2_common import main, HTTPStatus, Result, save_flag

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'
base_url = 'http://flupy.org/data/flags'
DEST_DIR = './downloads/'

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 10

class FetchError(Exception):
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
        raise web.HTTPNotFound

    else:
        raise aiohttp.ClientHttpProxyError(
            code = resp.status, message=resp.reason,
            headers=resp.headers)

# @asyncio.coroutine
# def get_flag(cc):
#     url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
#     resp = requests.get(url)
#     return resp.content

@asyncio.coroutine
def download_one(cc, base_url, semaphore, verbose):
    try:
        with (yield from semaphore):
            image = yield from get_flag(base_url, cc.lower())
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc.lower()) from exc
    else:
        save_flag(image, cc.lower() + 'gif')
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)
    return Result(status, cc)

@asyncio.coroutine
def downloader_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    to_do = [download_one(cc, base_url, semaphore, verbose) for
             cc in sorted(cc_list)]
    to_do_iter = asyncio.as_completed(to_do)
    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))
    for future in to_do_iter:
        try:
            res = yield from future
        except FetchError as exc:
            country_code = exc.country_code
            try:
                error_msg = exc.__cause__.args[0]
            except IndexError:
                error_msg = exc.__cause__.args[0]
            if verbose and error_msg:
                msg = '*** Error for {}:{}'
                print(msg.format(country_code , error_msg))
            status = HTTPStatus.error

        else:
            status = res.status
        counter[status] += 1
    return counter

def download_many(cc_list, base, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()
    return counts

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)

