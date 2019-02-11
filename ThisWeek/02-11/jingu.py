# created by Jingu Kang on 2019-02-11
# reference: Fluent Python by Luciano Ramalho
# the sequence differs depending on if class or def.

import collections
print(collections.Iterable.__class__)

import abc
print(abc.ABCMeta.__class__)

print(abc.ABCMeta.__mro__)

def deco_alpha(cls):
    print('<[200]> deco_alpha')

    def inner_1(self):
        print('<[300]> deco_alpha:inner_1')

    cls.method_y = inner_1
    return cls


class MetaAleph(type):
    print('<[400]> MetaAleph body')

    def __init__(cls, name, bases, dic):
        print('<[500]> MetaAleph.__init__')

        def inner_2(self):
            print('<[600]> MetaAleph.__init__:inner_2')

        cls.method_z = inner_2

class Hi():
    print('<[500]> hi')


print('<[1]> evaltime_meta module start')

@deco_alpha
class ClassThree():
    print('<[2]> Class Three body')

    def method_y(self):
        print('<[3]> ClassThree.method_y')


class ClassFour(ClassThree):
    print('<[4]> Class Four body')

    def method_y(self):
        print('<[5]> ClassFour.method_y')

class ClassFive(metaclass=MetaAleph):
    print('<[6]> ClassFive.__init__')
    def __init__(self):
        print('<[7]> ClassFive.__init__')
    def method_z(self):
        print('<[8]> ClassFive.method_z')

class ClassSix(ClassFive):
    print('<[9]> ClassSix body')
    def method_z(self):
        print('<[10]> ClassSix.method_z')
if __name__ == '__main__':
    print('<[11]> ClassThree tests', 30 * '.')
    three = ClassThree()
    three.method_y()

    print('<[12]> ClassFour tests', 30 * '.')
    three = ClassFour()
    three.method_y()

    print('<[13]> ClassFive tests', 30 * '.')
    three = ClassFive()
    three.method_z()

    print('<[14]> ClassSix tests', 30 * '.')
    three = ClassSix()
    three.method_z()
