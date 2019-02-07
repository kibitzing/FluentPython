# p647~p651
# created by Jingu Kang on 01-31
# reference: Fluent Python by Luciano Ramalho

# more abstract python

def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]

def display(obj):
    cls = type(obj)

    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))

## essential classes for this example

class Overriding:
    """a.k.a  data descriptor or enforced descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class overridingNoGet:
    """an overriding descriptor without __get__"""
    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class NonOverriding:
    """a.k.a. non-data or shadowable descriptor"""
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

class Managed:
    over = Overriding()
    over_no_get = overridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> managed.spam({})'.format(display(self)))
#
# obj = Managed()
# Managed.over = 1
# Managed.over_no_get = 2
# Managed.non_over = 3
# print(obj.over, obj.over_no_get, obj.non_over)

### Methods are descriptors
obj = Managed()
print(obj.spam)
print(Managed.spam)

obj.spam = 7
print(obj.spam)
print(Managed.spam)

import collections

class Text(collections.UserString):
    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]


word = Text('forward')
print(word)

print(word.reverse())

print(Text.reverse(Text('backward')))

print(type(Text.reverse), type(word.reverse))
# <class 'function'> <class 'method'>

print(list(map(Text.reverse, ['repaid', (10,20,30), Text('stressed')])))

print(Text.reverse.__get__(word)) #bound method
print(Text.reverse.__get__(None, Text)) #function
print(word.reverse) #bound method


