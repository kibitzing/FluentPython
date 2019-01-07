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

### 4)
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Before {} function operate.'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print('Operate display function.')
    
    
@decorator_function
def display_information(name, age):
    print('Operate display_information({}, {}) function'.format(name, age))
    
display()
print("\n")
display_information('kdh', 29)


### 5)
class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function
        
    def __call__(self, *args, **kwargs):
        print('Before {} function operate.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
    
    
@DecoratorClass
def display():
    print('Operate display function.')
    
    
@DecoratorClass
def display_information(name, age):
    print('Operate display_information({}, {}) function.'.format(name, age))
    
display()
print("\n")
display_information("kdh", 29)