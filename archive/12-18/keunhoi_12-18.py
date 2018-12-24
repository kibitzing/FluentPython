#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p452-ch15end
# Example 15-5-7

'''
   예제 위주 작성
'''

import contextlib

# Example 15-5

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'GNIDOCYPPAH'
    sys.stdout.write = original_write

# Example 15-7

@contextlib.contextmanager
def looking_glass_157():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
        msg = ''
        try:
            yield 'GNIDOCYPPAH'
        except ZeroDivisionError:
            msg = 'Please DO NOT divide by zero !'
        finally:
            sys.stdout.write = original_write
            if msg:
                print(msg)

    sys.stdout.write = reverse_write
    yield 'GNIDOCYPPAH'
    sys.stdout.write = original_write


@contextlib.contextmanager
def looking_glass2():
    import sys
    import random
    original_write = sys.stdout.write

    def shuffle_write(text):
        original_write(''.join(random.sample(text,len(text))))

    sys.stdout.write = shuffle_write
    yield 'GNIDOCYPPAH'
    sys.stdout.write = original_write

@contextlib.contextmanager
def looking_glass3():
    import sys
    import random
    original_write = sys.stdout.write

    def shuffle_write(text):
        original_write(''.join(random.sample(text,len(text))))

    sys.stdout.write = shuffle_write
    yield 'GNIDOCYPPAH'
    # sys.stdout.write = original_write


if __name__ == '__main__':
    print('{0:=<50}'.format("Example 15-6"))

    with looking_glass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

    print('{0:=<50}'.format("Custom Example1"))

    with looking_glass2() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

    print('{0:=<50}'.format("Custom Example2"))

    mystring = 'HAPPYHAPPYHAPPY'
    with looking_glass3() as what:
        print(mystring)
    print(mystring)
    print('RANDOM_SAMPLING_CHAOS')