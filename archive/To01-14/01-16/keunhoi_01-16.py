#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p585-589
# Example 19-1~(4)

"""
	예제 위주로 작성
"""

# Example 19-2
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
        with urlopen(URL) as remote, open(JSON, 'wb', encoding='UTF8') as local: # 윈도우에서 cp949 에러를 방지하기 위해서 encoding을 'UTF8'으로 설정한다.
            local.write(remote.read())

    with open(JSON, encoding='UTF8') as fp: # 윈도우에서 cp949 에러를 방지하기 위해서 encoding을 'UTF8'으로 설정한다.
        return json.load(fp)


if __name__ == "__main__":
    print('{0:=<50}'.format("Example 19-3"))

    feed = load()
    print(sorted(feed['Schedule'].keys()))
    for k, v in sorted(feed['Schedule'].items()):
        print('{:3} {}'.format(len(v),k))

    print('{0:=<50}'.format("Example 19-4"))

