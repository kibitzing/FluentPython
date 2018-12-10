#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p388~392
# Example 13- 15 ~ 18
'''
11-30 코드 부분에 페이지 작성이 틀렸었네요.

예제 13-17 까지의 내용만 보고 바로 간단하게 AddalbeBingoCage 클래스 짜보는 연습 진행
'''

from array import array
import reprlib
import math
import functools
import operator
import itertools
import numbers

from random import randrange

# 추억의 Example 10-16
class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return 'Vector({})'.format(str(list(self))) # replace 'tuple' in 11-08 sanghong's code
        # return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    # Example 13-1 추가
    def __neg__(self):
        return Vector(-x for x in self)

    # Example 13-1 추가
    def __pos__(self):
        return Vector(self)

    # Example 13-10 추가
    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    # Example 13-7 추가
    def __radd__(self, other):
        return self + other

    # Example 13-11 추가
    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    # Example 13-11 추가
    def __rmul__(self, scalar):
        return self * scalar

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    # # Example 13-12
    # def __eq__(self, other):
    #     return (len(self)) == len(other) and all(a == b for a,b in zip(self, other))

    # Example 13-13
    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self)) == len(other) and all(a == b for a,b in zip(self, other))
        else:
            return NotImplemented

    def __getitem__(self, index):
        import numbers
        cls = type(self)
        print(cls)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name): # 속성이 있는지, 그리고 __class__과 상속 클래스에 있는지 보고 나서 검색하는 거면, 속도 저하가 있지 않을까?
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]

        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_name:
                error = 'readonly attribute {atttr_name!r}'
            elif name.islower(): # 단일 소문자로 되어 있는 속성의 설정을 막음.
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)


    def angle(self, n):
        r = math.sqrt(sum(x*x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1 ) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecode))
        return cls(memv)

class AddableBingoCage:

    def __init__(self, string=None):
        self.string = str(string)

    def inspect(self):
        return tuple(self.string)

    def pick(self):
        list_string = list(self.string)
        return list_string[randrange(len(list(list_string)))]

    def __iter__(self):
        return iter(self.string)

    def __getitem__(self, index):
        import numbers
        if isinstance(index, numbers.Integral):
            return list(self.string)[index]
        else:
            raise TypeError

    def __add__(self, other):
        return AddableBingoCage(self.string + other.string)

    def __iadd__(self, other):
        return AddableBingoCage(self.string + other.string)

if __name__ == '__main__':
    print("{0:=^20}".format("Example 13-15"))
    v1 = Vector([1.0, 2.0, 3.0])
    v1_alias = v1
    print(id(v1))
    v1 += Vector([3,4,5])
    print(v1)
    print(id(v1))
    print(v1_alias)
    v1 *= 11
    print(v1)
    print(id(v1))

    print("{0:=^20}".format("Example 13-16 : AddableBingoCage 객체 사용법"))
    vowels = 'AEIOU'
    globe = AddableBingoCage(vowels)
    print(globe.inspect())
    print(globe.pick() in vowels) # 뽑기만 하고 제거는 되지 않음.
    print(len(globe.inspect()))

    globe2 = AddableBingoCage('XYZ')
    globe3 = globe + globe2
    print(globe3.inspect())
    print(type(globe3))
    print(len(globe3.inspect()))

    globe += globe2
    print(len(globe.inspect())) # Example 13 - 17 만큼 완전하게 구현은 하지 않았다.
