#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p447-p451
# Example 15-1~3

'''
   예제 위주 작성
'''


# Example 15-3
class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'GNIDOCYPPAH'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


if __name__ == '__main__':
    print('{0:=<50}'.format("Example 15-1"))

    l1 = list(range(10))

    for li in l1:
        print(li)
    else: # 이런거면 그냥 들여쓰기 안하고 작성하는 방식이랑 뭐가 다른거지...?
        print('else statement')


    print("\n{0:=<50}".format("Example 15-2"))
    with open('keunhoi_12-14.py', encoding='UTF8') as fp:
        src = fp.read(50)

    print(len(src))
    print(src)

    print("\n{0:=<50}".format("Example 15-3"))
    test = LookingGlass()
    test_text = test.__enter__()
    print(test_text == 'GNIDOCYPPAH')
    print(test_text)
    print(test)


