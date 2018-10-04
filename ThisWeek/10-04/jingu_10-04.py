"""
created by Jingu Kang on 10-04
"""

open('cafe.txt', 'w', encoding='utf-8').write('café')
print(open('cafe.txt').read())

open('cafe2.txt', 'w', encoding='cp1252').write('café')
print(open('cafe.txt').read())
