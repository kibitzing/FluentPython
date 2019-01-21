# Created by Jingu Kang on 01-16
# reference: Fluent Python by Luciano Ramalho
# if you are coding on a Window, you should add "encodint='utf-8'" when opening json file.
#
from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'

def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb', encoding='utf-8') as local:
            local.write(remote.read())

    with open(JSON, encoding='utf-8') as fp:
        return json.load(fp)


if __name__ == '__main__':
    feed = load()
    print(feed['Schedule'])
    feededSch = feed['Schedule']
    sortedList = sorted(feed['Schedule'])
    print(feededSch.keys())
    for key, value in feededSch.items():
        print('{:3} {}'.format(len(value), key))
    print(feededSch['speakers'][-1]['name'])
    print(feededSch['speakers'][-1]['serial'])
    print(feededSch['events'][40]['name'])
    print(feededSch['events'][40]['speakers'])
