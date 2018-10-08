"""
created by Jingu Kang on 2018-10-08
code: utf-8
"""

from unicodedata import normalize, name


def nfc_equal(str1, str2):   
    return normalize('NFC',str1) == normalize('NFC', str2)

def fold_equal(str1, str2):   
    return (normalize('NFC',str1).casefold() == normalize('NFC', str2).casefold())

s1 = 'café'
s2 = 'cafe\u0301'

NFC_s1 = normalize('NFC', s1)
NFD_s1 = normalize('NFD', s1)

NFC_s2 = normalize('NFC', s2)
NFD_s2 = normalize('NFD', s2)

print('NFC_s1, NFD_s1 = {0}, {1}'.format(NFC_s1, NFD_s1))
print('NFC_s2, NFD_s2 = {}, {}'.format(NFC_s2, NFD_s2))
print('length: NFC_s1, NFC_s2 = {}, {}'.format(len(NFC_s1), len(NFC_s2)))
print('length: NFD_s1, NFD_s2 = {}, {}'.format(len(NFD_s1), len(NFD_s2)))

print('\ns1 == s2: ',s1 == s2) # False
print('NFC_s1 == NFC_s2: ', NFC_s1 == NFC_s2) # True
print('NFC_s1 == NFD_s1: ' ,NFC_s1 == NFD_s1) # False
print('NFD_s1 == NFD_s2: ' ,NFD_s1 == NFD_s2) # True

for i in NFC_s1:
    print(i)   
# c
# a
# f
# é

for i in NFD_s1:
    print(i)
# c
# a
# f
# e
#  ́
    
    
ohm = '\u2126'
print('ohm:',ohm)
ohm_cf = ohm.casefold()
print('case folded ohm:',ohm_cf)
print('{}=={}'.format(ohm,ohm_cf) + ' -> ', ohm == ohm_cf)
print('fold_equal(ohm,ohm_cf):',fold_equal(ohm,ohm_cf))

# ohm: Ω
# case folded ohm: ω
# Ω==ω ->  False
# fold_equal(ohm,ohm_cf): True