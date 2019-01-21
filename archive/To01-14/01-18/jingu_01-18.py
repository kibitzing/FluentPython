# Created by Jingu Kang on 01-18
# reference: Fluent Python by Luciano Ramalho
# printed one more speaker from db

import warnings
import osconfeed

DB_NAME= 'data/schedule1_db'
CONFERENCE = 'conference.115'

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading {}'.format(DB_NAME))
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)

import shelve
db = shelve.open(DB_NAME)
if CONFERENCE not in db:
    load_db(db)

speaker = db['speaker.3471']
speaker2 = db['speaker.141169']
print(type(speaker))
print(speaker.name, speaker.twitter)
print(speaker2.name, speaker2.twitter)
