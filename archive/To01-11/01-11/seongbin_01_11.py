from urllib.request import urlopen
import warnings,os,json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'
json_data=open('osconfeed.json').read()

def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL,JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote,open(JSON,'wb') as local:
            local.write(remote.read())

        with open(JSON) as fp:
            return json.load(fp)

feed =json.loads(json_data)
print(sorted(feed['Schedule'].keys()))
for key, value in sorted(feed['Schedule'].items()):
    print('{:3} {}'.format(len(value),key))

print(feed['Schedule']['speakers'][-1]['name'])
print(feed['Schedule']['speakers'][-1]['serial'])
print(feed['Schedule']['events'][40]['name'])
print(feed['Schedule']['events'][40]['speakers'])
#다운로드 안되서 파일 직접 받아서 실행
