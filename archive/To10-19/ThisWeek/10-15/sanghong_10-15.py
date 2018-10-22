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
2018_10_15_Fluent_Python
@Author Sanghong.Kim
requests 를 이용하여 합성된 음성을 가져오는 프로그램

"""

# Import Modules
import time
import os
import sys
import argparse
import requests
import inspect

def clip(text, max_len=80):
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].rstrip()


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


def time_cal(program):
    # Started Time
    st=time.time()
    # Running Program
    print(program)
    # Ended Time
    et=time.time()
    # Running Time
    return et-st

def main(args):
    sig = inspect.signature(clip)
    sig # doctest: _ELLIPSIS
    str(sig)
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

    sig = inspect.signature(tag)
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    bound_args = sig.bind(**my_tag)
    print(bound_args)


    # 아래는 원본
    text = args.text
    output = args.output
    print("합성될 Text : %s" %text)
    fp = requests.get('http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=64&client=tw-ob&q=%s&tl=ko-kr' %text)

    if fp.status_code == 200:
        with open(output, 'wb') as f:
            for chunk in fp:
                f.write(chunk)
    else:
        print("Request Error!")
    fp.close()
    print("Result : ", output)


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", "-t", dest='text', type=str, help="Input your Text")
    parser.add_argument("--output", "-o", dest='output', type=str, help="Output File", default='./output.mp3')
    args = parser.parse_args()
    if args.text is None:
        print('Useage : python speech_synthesis.py -t "input text"')
        sys.exit(1)
    else:
        main(args)