#문자에 발음기호가 있는지 확인
s = 'café'
b = s.encode('utf8')
if len(s) != len(b):
    print(s+'에는 발음기호가 포함되어있음')
else:
    print(s + '에는 발음기호가 포함되어있지 않음')

