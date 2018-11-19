print(2*3*4*5)
import functools
print(functools.reduce(lambda a,b:a*b,range(1,6)))
n= 0
for i in range(6):
    n^=i
print(n)
print(functools.reduce(lambda a, b: a^b, range(6)))
import operator
print(functools.reduce(operator.xor,range(6)))

## this code is 11_07's code
from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in(self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r}'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    ###newlines
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self,other):
            if a != b:
                return False
        return True

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)
    ### to here
    def __abs__(self):
        return math.hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec = ''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self),self.angle())
            outer_format = '<{}, {}>'
        else:
            coords = self
            outer_format = '({}, {})'
            components = (format(c, format_spec) for c in coords)
            return outer_format.format(*components)

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(*memv)
### to here
