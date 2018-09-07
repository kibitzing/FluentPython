
#separate eng/jpn(hir)/jpn(kat)/kor
words = "ガaンネsウ너コ니kに드な프dでぺ쯊i가e"
decimal_unicode_eng = [ord(s) for s in words if ord(s) >= 97 and ord(s) <= 122]
decimal_unicode_hiragana = [ord(s) for s in words if ord(s) >= 12352 and ord(s) <= 12447]
decimal_unicode_katakana = [ord(s) for s in words if ord(s) >= 12448 and ord(s) <= 12543]
decimal_unicode_kor = [ord(s) for s in words if ord(s) >= 12593]
eng = [chr(s) for s in decimal_unicode_eng]
kor = [chr(s) for s in decimal_unicode_kor]
hiragana = [chr(s) for s in decimal_unicode_hiragana]
katakana = [chr(s) for s in decimal_unicode_katakana]
print(eng)
print(hiragana)
print(katakana)
print(kor)