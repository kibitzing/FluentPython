fp = open('cafe.txt','w', encoding='utf_8')
fp.write('café')
fp.close()

import os
os.stat('cafe.txt').st_size
fp2 = open('cafe.txt')
print(fp2)
fp2.encoding
print(fp2.read())
fp3 = open('cafe.txt',encoding='utf_8')
print(fp3)
print(fp3.read())
fp4 = open('cafe.txt','rb')
print(fp4)
print(fp4.read())

import sys,locale

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """
my_file = open('dummy','w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30),'->',repr(value))