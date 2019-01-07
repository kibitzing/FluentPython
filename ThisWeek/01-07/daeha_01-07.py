#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Decorator 복습해보는 예제

"""
### 1)
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function('Hello kdh!!')
bye_func = outer_function('Hello again kdh!!')

hi_func()
bye_func()


### 2)
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print("Display function operate!!")
    

decorated_display = decorator_function(display)
decorated_display()


### 3)

def decorator_function(original_function):
    def wrapper_function():
        print('Before {} function operate.'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display_1():
    print("Operate display_1 function")
    
@decorator_function
def display_2():
    print("Operate display_2 function")
    
    
display_1()
print("\n")
display_2()
