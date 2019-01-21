#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p590-594
# Example 19-5~7

"""
	예제 위주로 작성
"""

# Example 19-5
from collections import abc


class FrozenJSON:

    # def __init__(self, mapping):
    #     self.__data = dict(mapping)

    # Example 19-6
    # def __init__(self, mapping):
    #     self.__data = {}
    #     for key, value in mapping.items():
    #         if keyword.iskeyword(key):
    #             key += '_'
    #         self.__data[key] = value
	#
    # def __getattr__(self, name):
    #     if hasattr(self.__data, name):
    #         return getattr(self.__data, name)
    #     else:
    #         return FrozenJSON.build(self.__data[name])

    # Example 19-7
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


# if __name__ == "__main__":