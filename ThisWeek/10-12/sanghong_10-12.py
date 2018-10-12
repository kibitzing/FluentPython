#!/usr/bin/envs python3
# -*- coding: utf-8 -*-

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_10_12_Fluent_Python
@Author Sanghong.Kim
오늘은 약속이 생긴 이유로 예제 코드만 보고 실행 시켜 보았다.
tag 에서 볼 수 있는 모습은 <p> 또는 <br>이었으며 이를 보니 html을 보는 것과 같은 생각을 하게되었다.
이를 통해서 html을 작성하는 코드를 짤 수 도 있겠다는 생각이 든다.
물론 스타일은 없는 html이겠으나 input으로 해당 단어를 넣었을 때 특정 부분에 입력을 자동으로 해주면 편할 것 같다.
역시 4장에서 넘어와서 함수를 다루다 보니 재미있는 부분이 많은 것 같다.
4장 내용에서 ㄱ ㅣ ㅁ -> 김으로 만들어주는 코드를 작성하려 했으나 실패한 부분에 대해서 간단한 프로젝트를 진행하려 한다.
현재 사용하고 있는 서버의 ip를 wget을 하기위해서 (학교 네트워크 생각 보다 보안이 철저한거 같다.) 라즈베리파이를 준 상황
이다. 따라서 오늘의 코드는 google chrome에서 인터넷으로 올릴 예정이다. 처음 시도하는 것이지만 잘 되지 않을까 생각된다.
새로운 소식 : Raspberry pi 에서 Audio Card로 사용하였던 Cirrus Logic Audio 카드가 Raspbian 4.14.y 부터인지 그 이전인지
기본적으로 Raspbian에 탑재 되었다. 혹시라도 사용하는 사람이 있다면 참고하면 좋을 것 같다.
"""

# Import Modules
import time
import os
import sys
import argparse
import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

def time_cal(program):
    # Started Time
    st=time.time()
    # Running Program
    print(program)
    # Ended Time
    et=time.time()
    # Running Time
    return et-st

def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attrs_str = ''.join('%s="%s"' %(attr, value)
                            for attr, value in sorted(attrs.items()))
    else:
        attrs_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attrs_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attrs_str)


def main(args):
    # 사용자 정의 콜러블형 BingoCage 만들기
    # bingo는 카드게임인 그 Bingo 말하는 듯
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))

    print(dir(BingoCage))

    # 함수 인트로스펙션
    # 함수인 func 에서 class인 obj의 속성들을 제거 하여 함수와 클래스 사이의 차이점을 알아봄
    class C: pass
    obj = C()
    def func(): pass
    print(sorted(set(dir(func)) - set(dir(obj))))


    tag('br')
    tag('p', 'hello')
    print(tag('p','hello','world'))
    print(tag('p', 'hello', id='33'))
    print(tag('p', 'hello', 'world', cls='sidebar'))

    tag(content='tesing', name="img")
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'senset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
