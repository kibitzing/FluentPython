"""
created by Jingu Kang on 10-04
"""

open('cafe.txt', 'w', encoding='utf-8').write('café')
print(open('cafe.txt').read())

open('cafe2.txt', 'w', encoding='cp1252').write('café')
print(open('cafe.txt').read())

## window 에서 실행 시 
# caf챕
# cafÃ©
## 윈도우 디폴트 설정인 cp949 와 cp1252 에서 é를 인코딩 하지 못함.

## 맥에서 실행 시 
# café
# café

## 한글 처리 방식도 다른데 맥/리눅스에서는 한글을 자음 모음 하나하나 처리하기 때문에 글자 수 맞추기도 어렵..
## 이거 처리방법도 한번 봐야겠다.
#