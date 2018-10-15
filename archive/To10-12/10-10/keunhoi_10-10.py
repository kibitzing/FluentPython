#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import _locale
_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

from unicodedata import normalize, name

s1 = 'caffè'
s2 = 'caffe\u0301'
print(len(s1),len(s2))
print(len(normalize('NFC', s1)),len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)),len(normalize('NFD', s2)))
print('='*50)

ohm = '\u2126'
print(name(ohm))
ohm_c = normalize('NFC', ohm)
print(name(ohm_c))
print(ohm==ohm_c)
print('='*50)

half = '½'
print(half)
half = normalize('NFKC', half)
print(half)
print('Is 1/2 == half?? ', 1/2 == half)
print('Is "1⁄2" == half?? ','1/2' == half)

four_squared = '4²'
print(four_squared)
four_squared = normalize('NFKC', four_squared)
print(four_squared)
print('Is 42 == four_squared ??', 42 == four_squared)
print('Is "42" == four_squared ??','42' == four_squared)
print('='*50)

micro = 'μ'
print(name(micro))
micro_cf = micro.casefold()
print(micro_cf) # 예제와는 반대로 출력되는 것으로 판단된다.

# ================================

import locale
fruits = ['caju','atemoia','acerola','cajá', 'açaí']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print('sorted by locale.strxfrm', sorted_fruits)
print('not sorted by locale.strxfrm', sorted(fruits))
print('='*50)

import unicodedata
import string

class remover:

    def shave_marks(self, txt):
        """Remove all diacritic marks"""
        norm_txt = unicodedata.normalize('NFD', txt)
        shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
        return unicodedata.normalize('NFC', shaved)

    def shave_marks_latin(self, txt):
        """Remove all diacritic marks from Latin base characters"""
        norm_txt = unicodedata.normalize('NFD', txt)
        latin_base = False
        keepers = []
        for c in norm_txt:
            if unicodedata.combining(c) and latin_base:
                continue # ignore diacritic on Latin base char
                keepers.append(c)
                # if it isn't combining char, it's a new base char
            if not unicodedata.combining(c):
                latin_base = c in string.ascii_letters
                shaved = ''.join(keepers)
        return unicodedata.normalize('NFC', shaved)
