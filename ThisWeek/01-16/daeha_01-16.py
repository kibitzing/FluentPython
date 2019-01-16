#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 동적 속성을 이용한 데이터 랭글링

"""
from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'osconfeed.json'

def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())
            
    with open(JSON) as fp:
        return json.load(fp)
    
feed = load()
sorted(feed['Schedule'].keys())

for key, value in sorted(feed['Schedule'].items()):
    print('{:3} {}'.format(len(value), key))