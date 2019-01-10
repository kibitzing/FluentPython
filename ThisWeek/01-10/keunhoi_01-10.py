#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p547-551
# Example 18-5

'''
	예제 위주로 작성
'''

import asyncio

import aiohttp

from flags import BASE_URL, save_flag, show, main

# Example 18-5
@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    image = yield from resp.read()
    return image

@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc) # 유일한 차이점
	# 기존 코드
	# image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)

if __name__ == '__main__':
    print('{0:=<50}'.format("Example 18-5"))
    main(download_many)
