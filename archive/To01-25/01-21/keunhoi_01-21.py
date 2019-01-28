#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p600-604
# Example 19-12~(16)

"""
	예제 위주로 작성
"""

# Example 19-12
class MissingDatabaseError(RuntimeError):
    """필요한 데이터베이스가 설정되어 있지 않을 때 발생."""

class DbRecord(Record):

    __db =None

    @staticmethod
    def set_db(db):
        DbRecord.__db = db

    @staticmethod
    def get_db():
        return DbRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = "database not set; call '{}.set_db(my_db)'"
                raise MissingDatabaseError(msg.format(cls.__name__))
            else:
              raise

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return'<{} serial={!r}'.format(cls_name, self.serial)
        else:
            return super().__repr__()


# Example 19-13
class Event(DbRecord):

    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, '_speaker_objs'):
            spkr_serials = self.__dict__['speakers']
            fetch = self.__class__fetch
            self._speaker_objs = [fetch('speaker.{}'.format(key))
                                  for key in spkr_serials]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, 'name'):
            cls_name = self.__class__.__name__
            return '<{} {!r}>'.format(cls_name, self.name)
        else:
            return super().__repr__()


# Example 19-14

# osfonfeed.py -> class osconfeed
class osconfeed:

    from urllib.request import urlopen
    import warnings
    import os
    import json

    URL = 'http://www.oreilly.com/pub/sc/osconfeed'
    JSON = 'data/osconfeed.json'

    def load(self):
        if not os.path.exists(JSON):
            msg = 'downloading {} to {}'.format(URL, JSON)
            warnings.warn(msg)  # <1>
            with urlopen(URL) as remote, open(JSON, 'wb') as local:  # <2>
                local.write(remote.read())

        with open(JSON) as fp:
            return json.load(fp)  # <3>

def load_db(db):
    import inspect
    import warnings

    raw_data = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DbRecord)
        if inspect.isclass(cls) and issubclass(cls, DbRecord):
            factory = cls
        else:
            factory = DbRecord
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)

# Example 19-15
class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

# if __name__ == "__main__":