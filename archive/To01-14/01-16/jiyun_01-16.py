# json 파일 내려받기

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
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())
    with open(JSON) as fp:
        return json.load(fp)


# FrozenJSON으로 변환

from collections import abc

class FrozenJSON:
    """ 점 표기법을 이용해서 JSON과 유사한 객체를 순회하는
        읽기 전용 퍼사드 클래스
    """

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


# feed['Schedule']['events'][40]['speakers']
# feed.Schedule.events[40].speakers 동일
