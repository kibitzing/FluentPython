# shelve를 이용해서 OSCON 피드 구조 변경하기

import warnings
import osconfeed

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        # 키워드 인수로부터 생성된 속성으로 객체를 생성할 때 사용


def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]  # 컬렉션 명에서 s 제거
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            # record_type 과 'serial' 필드로부터 key 생성
            record['serial'] = key  # 'serial' 필드를 새로 생성한 key 로 설정
            db[key] = Record(**record)  # Record 객체 생성 후 해당 key 로 저장

# >>> import shelve
# >>> db = shelve.open(DB_NAME)
# >>> if CONFERENCE not in db:
# ...     load_db(db)
# >>> speaker = db['speaker.3471']
# >>> type(speaker)
# <class '__main__.Record'>
# >>> speaker.name, speaker.twitter
# ('Anna Martelli Ravenscroft', 'annaraven')
# >>> db.close()

