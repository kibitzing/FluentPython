#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 18/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        learn to use contextmanager in generator form
        implemented upper_case, lower_case
"""
import sys
import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write

    yield 'abcdABCD'
    sys.stdout.write = original_write

@contextlib.contextmanager
def upper_case():
    import sys
    original_write = sys.stdout.write

    def write_upper(text):
        original_write(text.upper())

    sys.stdout.write = write_upper
    yield 'abcdABCD'
    sys.stdout.write = original_write

@contextlib.contextmanager
def lower_case():
    import sys
    original_write = sys.stdout.write

    def write_lower(text):
        original_write(text.lower())

    sys.stdout.write = write_lower
    yield 'abcdABCD'
    sys.stdout.write = original_write

with looking_glass() as what:
    with lower_case() as why:
        print('Alice, Kitty and Snowdrop')
        print('what?', what)
        print('why?', why)
with upper_case() as what:
    print('Alice, Kitty and Snowdrop')
    print('what?', what)

with lower_case() as what:
    print('Alice, Kitty and Snowdrop')
    print('what?', what)
