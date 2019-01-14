#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 07/01/2019.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        download flags with error handling
"""
import os
import time
import sys
import tqdm
import string
import argparse
import requests
import collections
from collections import namedtuple
from enum import Enum


Result = namedtuple('Result', 'status data')

HTTPStatus = Enum('Status', 'ok not_found error')

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

DEFAULT_CONCUR_REQ = 1
MAX_CONCUR_REQ = 1


BASE_URL = 'http://flupy.org/data/flags'

DEFAULT_SERVER = 'LOCAL'

DEST_DIR = 'downloads/'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content



def download_one(cc, base_url, verbose=False):
    try:
        image = get_flag(cc)

    except requests.exceptions.HTTPError as exc:
        res =exc.response
        if res.status_code == 404:
            status = HTTPStatus.not_found
            msg = 'not Found'
        else:
            raise
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'
    if verbose:
        print(cc, msg)
    return Result(status, cc)

def download_many(cc_list, base_url, verbose, max_req):
    counter = collections.Counter()
    cc_iter = sorted(cc_list)

    if not verbose:
        cc_iter = tqdm.tqdm(cc_iter)

    for cc in cc_iter:
        try:
            res = download_one(cc, base_url, verbose)
        except requests.exceptions.HTTPError as exc:
            error_msg = 'HTTP error {res.status_Code} = {res.reason}'
            error_msg = error_msg.format(res=exc.response)
        except requests.exceptions.ConnectionError as exc:
            error_msg = "Connection error"
        else:
            error_msg = ''
            status = res.status
        if error_msg:
            status = HTTPStatus.error
        counter[status] += 1
        if verbose and error_msg:
            print('*** Error for {}:{}'.format(cc, error_msg))
        return counter

def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC, DEFAULT_CONCUR_REQ,True, MAX_CONCUR_REQ)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2}s '
    print(msg.format(count, elapsed))

if __name__ == '__main__':
    main(download_many)
