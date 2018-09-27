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
2018_09_18_Fluent_Python
@Author Sanghong.Kim
UserDict
Mapping
set
라즈베리파이 핀번호를 변경하고 싶은 사용자에 대한 시뮬레이션
"""

# Import Modules
import sys
import argparse
import collections
from types import MappingProxyType

DIAL_CODES = [
    (2, '강민호'),
    (3, '이민선'),
#    (_12, '언더바십이'),   # _등의 특수문자형 비 문자열은 안된다.
    (1, '숫자일'),
    (0.123, '박진희')
]

mydict = {
    2: '강민호',
    3: '이민선',
    1: '숫자일',
    0.123: '박진희'
}

newdict={}
# Apple Pie ABC song
index=[ 'A', 'B', 'C', 'D', 'E']
value=['Apple Pie', 'Bit it', 'Cut it', 'Dealt it', 'Eat it']

raspberrypipin={
    'pin31' : 'GPIO_6',
    'pin32' : 'GPIO_5',
}

GPIO=MappingProxyType(raspberrypipin)


# Ascii Art 및 Vim Editer 사용으로 쉽게 그릴 수 있음
def draw_gpio():
    print(        "                                                              '''''``````````````````````````````````````````````````````````````````'''''                                                              ")
    print(        "                                                              '''''``````````````.''+'';.```````````````````````;'''''.``````````````'''''                                                              ")
    print(        "                                                              '''''````````````;'++++++++',``````````````````,'++++++++';````````````'''''                                                              ")
    print(        "  ````````````````````````````````````````````````````````````'''''``````````.'++++++++++++'````````````````'++++++++++++'```````````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''`````````,'++++++++++++++'``````````````'+++++++++++++++,`````````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''````````,+++++++''''++++++'````````````+'++++++''++++++++.````````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''```````.'+++++'`` ``,'+++++'` ````````'+++++',`  `.'++++++````````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''```````'+'++'`        ,+++++;````````'+++++,        `'++++'```````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''``````'++++'           `'++++.``````.++++'`           '++++;``````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''``````++++'             `'+++'``````'+++'`             '++++``````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''`````;+++'               .++++.````.++++.               ++++;`````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''`````++++`                '+++'````'+++;                ,+++'`````'''''````````````````````````````````````````````````````````````  ")
    print(        "  `````````````````````````@@@@``@@@@#``@#``@@@#```@@@````````'''''````,+++'                 `'++'````'+++`                 '+++.````'''''````````@@@@``@@@@+``@#``@@@#````@@```@@@```````````````````  ")
    print(        "  ````````````````````````@@@@@+`@@@@@``@#`@@@@@+`+@@@#```````'''''````'+++.                  '+++.``,+++'                  ,+++'````'''''```````@@@@@;`@@@@@``@#`@@@@@'``@@@``@@@@@``````````````````  ")
    print(        "  ```````````````````````.@@``@``@@`'@,`@#`@@``@@`@@``````````'''''````+++'    `@@'     +`    .+++'``'+++`    @@+   ,@@#     '++'````'''''``````,@#``@``@@`#@.`@#`@@``@@`@@@@``@#`#@``````````````````  ")
    print(        "  ```````````````````````;@:`````@@`@@.`@#.@+``@@`@#@@.```````'''''````+++'    @; @.   .@`     '++'``'+++    @' @,  @, @;    '+++````'''''``````'@:`````@@`@@.`@#,@+``@@`@`@@`````@@``````````````````  ")
    print(        "  ```````````````````````;@,`@@@`@@@@@``@#.@'``@@`@@@@@```````'''''```,+++,   .#  :+  .@@`     '++'``+++'   `@  ,# ;+  .@    ,+++.```'''''``````'@,`@@@`@@@@@``@#,@'``@@```@@````@@```````````````````  ")
    print(        "  ```````````````````````,@#`@@@`@@@@```@#`@@``@@`@#`+@```````'''''```:+++`       :+  @ @`     ;+++``+++;       ,+ +:   @    .+++:```'''''``````:@'`@@@`@@@@```@#`@@``@@```@@```@@````````````````````  ")
    print(        "  ````````````````````````@@@@@@`@@`````@#`@@@@@#`@@`@@```````'''''```;+++       `@     @`     ,+++`.+++,       @      :#    `+++;```'''''```````@@@@@@`@@`````@#`@@@@@#```@@``@@@@@``````````````````  ")
    print(        "  ````````````````````````:@@@@.`@@`````@#`.@@@@``.@@@'```````'''''```;+++      .@@     @`     ,+++`.+++.     `@@      @     `+++'```'''''```````;@@@@``@@`````@#`.@@@@````@@``@@@@@``````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''```;+++        .@    @`     ,+++`.+++.       .@    @'     `+++'```'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''```;+++         @    @`     ,+++`.+++.        @   #@      `+++;```'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''```:+++`   ;#   @    @`     :+++``+++:   :@   @  '@       `+++:```'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''```,+++.   .@  `@    @`     '+++``+++'   `@   @ `@        .+++,```'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''```.+++;    @@@@.    @`     '+++``+++'    @@@@, #@@@@@    '+++````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''````+++'     #@      @`    `+++'``'+++`    +@   @@@@@@    '++'````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''````++++`                  :+++:``;+++:                  `+++'````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''````:+++;                  '+++```.'+++                  '+++:````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''`````+++'                 ,+++'````'+++.                `++++`````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''`````'+++'                '+++:````:++++                '+++'`````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''`````.'++',              '++++``````++++'              ,++++.`````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''``````'++'+.            ;++++;``````;++++;            .'+++'``````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''``````.+++++:          '++++'````````'++++'          :+++++```````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''```````'+++++'`      ,++++++.````````.+++++',      `'+++++;```````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''````````'++++++'';'''++++++:``````````:++++++''''''++++++'````````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''`````````'++++++++++++++++:````````````;++++++++++++++++'`````````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''``````````''+++++++++++++,``````````````,+++++++++++++';``````````'''''````````````````````````````````````````````````````````````  ")
    print(        "  ````````````````````````````````````````````````````````````'''''```````````,'++++++++++'``````````````````'++++++++++'.```````````'''''````````````````````````````````````````````````````````````  ")
    print(        " `````````````````````````````````````````````````````````````'''''`````````````,'++++++'.````````````````````.'++++++',`````````````'''''````````````````````````````````````````````````````````````  ")
    print(        "                                                              '''''``````````````````````````````````````````````````````````````````'''''                                                              ")
    print(        "                                                              '''''``````````````````````````````````````````````````````````````````'''''                                                              ")
    print(        "                                                                                                                                                                                                        ")
    print(        "                                                                                                                                                             ")
    print(        "                                                                                                                                                                                                        ")
    print(        "                                                                                                                                                                                                    ")
    print(        "                                                                                                                                                                                                        ")
    print(        "                                                                                                                                                                                                        ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                    ")
    print(        "                                                                   '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                    ")
    print(        "                                                                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                     ")
    print(        "                                                                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                      ")
    print(        "                                                                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                       ")
    print(        "                                                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'                                                                                        ")
    print(        "                                                                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;                                                                                         ")
    print(        "                                                                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                                                                                          ")
    print(        "                                                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                                                                                           ")
    print(        "                                                                            ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                             ")
    print(        "                                                                             `@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                              ")
    print(        "                                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                               ")
    print(        "                                                                                @@@@@@@@@@@@@@@@@@@@@@@@                                                                                                ")
    print(        "                                                                                 @@@@@@@@@@@@@@@@@@@@@@                                                                                                 ")
    print(        "                                                                                  @@@@@@@@@@@@@@@@@@@#                                                                                                  ")
    print(        "                                                                                   #@@@@@@@@@@@@@@@@+                                                                                                   ")
    print(        "                                                                                    +@@@@@@@@@@@@@@                                                                                                     ")
    print(        "                                                                                     '@@@@@@@@@@@@                                                                                                      ")
    print(        "                                                                                      ;@@@@@@@@@@                                                                                                       ")
    print(        "                                                                                        @@@@@@@@                                                                                                        ")
    print(        "                                                                                         @@@@@@                                                                                                         ")
    print(        "                                                                                          @@@@                                                                                                          ")
    print(        "                                                                                           @;                                                                                                           ")
    print(        "                                                                                                                                                                                                        ")
    print(        "                                                                                                                                                                                                        ")
    print(        "                                                                                                                                                                                                        ")
    print(        "                                                                                                                                                                                                        ")
    print(        "                                                                                                                                                                                                                                                                                                                             ")
    print("")
    print("")
    print("")
    print("")
    print(        "                                                              '''''```````````````.:;;:.````````````````````````.:;;:.``````````````.'''''                                                              ")
    print(        "                                                              '''''`````````````''''+++'',````````````````````''++++++''````````````.'''''                                                              ")
    print(        "                                                              '''''```````````'+++++++++++'.````````````````:+++++++++'+';``````````.'''''                                                              ")
    print(        " `````````````````````````````````````````````````````````````'''''`````````.'++++++++++++++:``````````````'++++++++++++++'`````````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''````````.'++++++++++++++++'````````````'++++++'+++++++++'````````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''````````'+++++''...:'++++++;``````````'+++++'':..:''+++++'```````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''```````'+++++,`      `'+++++.````````;+++++'`      `;+++++;``````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''``````;++++'`          ;++++'```````.++++'.          .'++++.`````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''``````'+++'`            :'+++:``````'+++'`            `'+++'`````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''`````;+++'`              '++++`````.++++,              .'+++,````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''`````'++',               `'+++,````'+++;                '+++'````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''````,'++'                 ,+++'````'+'+`                `'+++````.'''''````````:@@```@@@@``.@+```@@`````@@```+@+```````````````````` ")
    print(        " ```````````````````````````@@'``+@@@;``@@```@@.```@@@@```````'''''````'+++.                  '+'+```:++';                  ;+++:```.'''''```````@@@@@``@@@@@`,@+`+@@@@.``,@@``@@@@#``````````````````` ")
    print(        " `````````````````````````,@@@@@`+@@@@,`@@`.@@@@#``@@@@```````'''''````'+''     @@      #     ;+++,``'+++.    @@     @@     `+++'```.'''''``````.@@`'@+`@@`@@`.@+`@@.'@@`@@@@``@@`@@``````````````````` ")
    print(        " `````````````````````````@@;`@@`+@.;@+`@@`@@+`@@`.@.`````````'''''```.+++'    @@@@    `@     `'++'``'++'    @@@@   @@@@`    ''+'```.'''''``````'@,`````@@`@@`.@+.@+``@@`@'@@`````@@``````````````````` ")
    print(        " `````````````````````````@@`````+@..@+`@@`@@``'@,,@@@'```````'''''```,+++.   :@  #:   @@      '++'``+++'   ,@  #; '#  +#    ;++'```.'''''``````+@.`@@@`@@@@@`.@+,@;``@@```@@````@@,``````````````````` ")
    print(        " ````````````````````````.@#`#@@`+@@@@;`@@`@@``:@;'@@@@```````'''''```'++'`    :  ':  @,@      '+++`.+++:    '  ;' #`   @    ,+++.``.'''''``````'@,`@@@`@@@@,`.@+.@+``@@```@@```@@:```````````````````` ")
    print(        " ````````````````````````.@@`#@@`+@@@@``@@`@@``'@,```.@,``````'''''```'++'`       @     @      ;+++`,+++.       @`     ,#    .+++,``.'''''``````.@@``@@`@@````.@+`@@.'@@```@@``'@,````````````````````` ")
    print(        " `````````````````````````@@;`@@`+@.````@@`@@+`@@.@@`:@.``````'''''```'++'      :@`     @      ;+++`,+++`     ,@`      @.    `+++:``.'''''```````@@@@@;`@@````.@+`+@@@@.```@@``@@@@@``````````````````` ")
    print(        " `````````````````````````,@@@@@`+@.````@@``@@@@#`.@@@@```````'''''```'++'        @;    @      ;++'`:+++`       @+    +@     `+++:``.'''''````````:@@```@@````.@+```@@`````@@``@@@@@``````````````````` ")
    print(        " ```````````````````````````@@.``+@.````@@```@@.````@@````````'''''```'++'         @    @      ;+++`,+++`        @   :@      `+++:``.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''```'++'`    ,   @    @      ;+++`,+++.    :   @  .@       .+++,``.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''```'++'`   '+  `@    @      '++'`.+++:   :#  `@  @`       ,+++.``.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''```:+++.    @. @:    @      '++'``'++'    @, @; #'        ;+++```.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''```.+++;    ,@@'     @     `+++'``'+''    .@@#  @@@@@@    '++'```.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''````'++'                   :'++,``'++'`                  `+++'```.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''````'+++.                  '+++```:''+;                  ;'++:```.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''````:'++'                 .+++'````'++'`                `'+''````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''`````'+++.               `'+++:````'+++;                ;+++'````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''`````'+++'`              ;+++'`````.++++.              .'+'+,````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''``````'+++'             :++++;``````'+++'`            `'+++'`````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''``````'+++''`          :''++'```````.++++'`          `'+++'.`````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''```````''+++'.       `'+++++.````````;+'++';`      `;'++++'``````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''````````''+++'':```,''+++++;``````````'++++'+'.``.''+++++'```````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''````````.'++'++++++++++++''````````````''++++++++++'++++'````````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''`````````.'+'++++++++++'';``````````````'''++++++++++++'`````````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''```````````'+++++++++++'.````````````````;+++++++++++';``````````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''````````````,''++++'+';```````````````````.'''++++'''````````````.'''''````````````````````````````````````````````````````````````` ")
    print(        " `````````````````````````````````````````````````````````````'''''```````````````,;'';.````````````````````````.;'';.``````````````.'''''````````````````````````````````````````````````````````````  ")
    print(        "                                                              '''''`````````````````````````````````````````````````````````````````.'''''                                                              ")

# UserDict는 MutableMapping을 상속받음
class StrKeyDit(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

def main(args):
    '''
    책 예제 내용
        #Tuple List로부터 dict 생성
        dial_code=dict(DIAL_CODES)

        # Float 및 Int가 포함된 Dictionary
        print("Float 및 Int가 포함된 Dictionary")
        print(dial_code)
        # Str로 변경되는 것을 알 수 있음
        print("StrKeyDit를 사용하여 String형으로 변경 됨을 확인 가능")
        print(StrKeyDit(dial_code))

        # 불변 Mapping으로 newdict_proxy를 생성
        newdict_proxy = MappingProxyType(newdict)
        # 책의 설명과 마찬가지로 newdict_proxy는 불변형으로 변경이 불가능
        # newdict_proxy[1] = 'a'

        # 기존의 dictionary가 변경 되었을 때 newdict_proxy가 변경되는 것을 확인
        k = 0
        for i in index:
            newdict[i] = value[k]
            print(newdict_proxy)
            k += 1
    '''

    # 책의 내용을 보면 Mapping을 하는 이유는 하드웨어 적인 부분을 변경 하지 못하게 하기 위함임
    # Pin 31번의 GPIO_6을 GPIO_5로 변경하고 싶은 사용자
    print(draw_gpio())

    print("pin_31 is :",GPIO['pin31'])
    try:
        if args.change:
            print("Change pin_31 as GPIO_5")
            GPIO['pin31'] = 'GPIO_5'
        else:
            return
        # Error의 종류를 Debugging 한 뒤 예외 처리 적용, 모르고 있었음, 예외 처리에 시간을 생각보다 많이 소비
    except TypeError as e:
        print("You Can't Change GPIO Mapping Number!")
        sys.exit()



# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--changepin", dest='change', action='store_true', help="To Change GPIO_6 to GPIO_5")
    args = parser.parse_args()
    print("해당 스크립트를 실행시 Ascii Art의 영향으로 전체 화면으로 보시는 것을 권장드립니다.")
    reply = str(input("동의 하십니까? [y/n] ")).lower().strip()
    if reply[:1] == 'y':
        main(args)
    elif reply[:1] == 'n':
        print("눈에 무리가 갈 수도 있습니다, 프로그램을 종료합니다.")
    else:
        sys.exit()
    print("--changepin 옵션도 이용해 보세요! ex) python3 sanghong_09-20.py --changepin")