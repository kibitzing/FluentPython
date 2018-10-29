#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
"""
    Created by Jingu Kang on 30/09/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.
    
    DESCRIPTION:
    practice using decorator
    say which functions are included in the main function
    Difference between first and second decorator is interesting
"""
from os import system as sys

def tellingFunctionName(func):
    functionName = str(func)[10:-16]
    sys('say '+ functionName)
    def inner():
        print(functionName)
    return inner

def tellingFunctionName2(func):
    functionName = str(func)[10:-16]
    sys('say '+ functionName)
    return func

@tellingFunctionName
def hello():
    print('hello2') # not going to be printed

@tellingFunctionName
def everyOne():
    print('everyone2') # not going to be printed


@tellingFunctionName2
def keras():
    print('import keras')

@tellingFunctionName2
def tensorflow():
    print('import tensorflow as tf')

def main():
    sys('say are in this main function')
    hello() # hello
    everyOne() # everyOne
    keras() # import keras
    tensorflow() # import tensorflow as tf

if __name__ == '__main__':
    main()
