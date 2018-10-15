from unicodedata import normalize,name
s1 = 'café'
s2 = 'cafe\u0301'
print(len(s1), len(s2))
print(len(normalize('NFC' , s1)) , len(normalize('NFC' , s2)))
print(len(normalize('NFD' , s1)) , len(normalize('NFD' , s2)))
print(normalize('NFC',s1) == normalize('NFC',s2))
print(normalize('NFD',s1) == normalize('NFD',s2))

ohm = '\u2126'
print(name(ohm))
ohm_c = normalize('NFC',ohm)
print(name(ohm_c))
ohm_d = normalize('NFD',ohm)
print(name(ohm_d))
print(ohm_c == ohm)
print(normalize('NFC',ohm_c) == normalize('NFC',ohm))
half = '½'
print(normalize('NFKC',half))
four_squared = '4²'
print(normalize('NFKC',four_squared))
micro ='µ'
micro_kc = normalize('NFKC',micro)
print(micro, micro_kc)
print(ord(micro),ord(micro_kc))
print(name(micro),name(micro_kc))