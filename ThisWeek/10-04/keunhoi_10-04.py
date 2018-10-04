#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
class Decoder:
    def __init__(self):
        self.s = b'montr\xe9al'

    def decoding(self,s=b'montr\xe9al',mode='cp1252'):
        if s == None:
            self.s = self.s
        else:
            self.s = s
            try:
                return s.decode(mode)
            except UnicodeDecodeError as e:
                print('%s codex is not proper for string s' % mode)
                return s.decode(mode,errors='replace')

d = Decoder()
print(d.decoding())
print(d.decoding(mode='iso8859'))
print(d.decoding(mode='koi8_r'))
print(d.decoding(mode='utf_8'))

