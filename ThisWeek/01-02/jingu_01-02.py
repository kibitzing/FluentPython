#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 02/01/2019.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        added download_many() to previous code to see how futures works
"""


import os
import requests
import sys
import time
from concurrent import futures

image_addresses = [
    'http://cvip.inha.ac.kr/images/lsh.jpg',
    'http://biselab.inha.ac.kr/wp-content/uploads/2016/12/admin-ajax-3.jpg',
    'http://cvip.inha.ac.kr/images/kdh.jpg',
    'http://cvip.inha.ac.kr/images/pjy.jpg',
]

member_name = ['이승현', '강진구', '김대하', '박지윤']

DEST_DIR = './downloadMemberImage'

if not os.path.exists(DEST_DIR):
    os.mkdir(DEST_DIR)

def save_memberImage(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_memberImage(image_address):
    url = image_address
    resp = requests.get(url)
    return resp.content

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def main(download_many):
    t0 = time.time()
    count = download_many(image_addresses)
    elapsed = time.time() - t0
    msg = '\n{} images downloaded in {:.2}s '
    print(msg.format(count, elapsed))

MAX_WORKER = 4

def download_one(image_address):
    image = get_memberImage(image_address)
    show(image_address)
    save_memberImage(image, member_name[image_addresses.index((image_address))] + '.jpg')
    return image_address

def download_many(image_addresses):
    workers = min(MAX_WORKER, len(image_addresses))
    image_addresses = image_addresses[:5]
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        to_do= []
        for member in image_addresses:
            future = executor.submit(download_one, member)
            to_do.append(future)
            msg = "Scheduled for {}: {}"
            print(msg.format(member, future))
        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    return len(results)

if __name__ == '__main__':
    main(download_many)
