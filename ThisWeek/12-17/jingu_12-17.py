#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 17/12/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        simple variation of example source
        using with and stdout.write
"""
import sys

class LookingMinus:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.minus_write
        return '12345'

    def minus_write(self, numbers):
        for number in numbers:
            if number == '[' or number == ']' or number == ',' or  number == ' ' or  number == '\n':
                continue
            self.original_write('-'+ str(number))

        self.original_write('\n')

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True
with LookingMinus() as what:
    print([1,2,3,4,5])
    print('what?', what)
print('Back to normal.')
print('what?', what)

print('================')
class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'abcdef'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print('what?',what)

print('Back to normal.')
print('what?',what)
