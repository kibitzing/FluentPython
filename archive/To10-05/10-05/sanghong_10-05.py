#!/usr/bin/envs python3
# -*- coding: utf-8 -*-

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_10_05_Fluent_Python
@Author Sanghong.Kim
"""

# Import Modules
import time
import os
import sys
import argparse
import locale

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

def main(args):
    # Started Time
    st=time.time()

    my_file = open('dummy', 'w')

    for expression in expressions.split():
        value = eval(expression)
        print(expression.rjust(30), '->', repr(value))

    print("--------------------------------------------------------")

    for expression in expressions.split():
        value = eval(expression)
        print(expression.ljust(30), '->', repr(value))

    print("--------------------------------------------------------")

    for expression in expressions.split():
        value = eval(expression)
        print(expression.center(30), '->', repr(value))

    my_file.close()

    # Ended Time
    et=time.time()

    # Running Time (End Time - Start Time)
    print("Running Time : ",et-st,"s")


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
