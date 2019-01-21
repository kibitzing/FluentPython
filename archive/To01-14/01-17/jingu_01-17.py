# Created by Jingu Kang on 01-17
# reference: Fluent Python by Luciano Ramalho
# __new__ is very interesting!

from collections import abc
from osconfeed import load
from keyword import iskeyword
class FrozenJSON:
    """
    A read-only facade for navigating a JSON-like object
    using attribute notation
    """

    def __new__(cls, arg):
        print('Hi~! I am attribute New!') # appears so many time
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data =  {}
        for key , value in mapping.items():
            if iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name): # called only when there is no attribute
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

if __name__ == '__main__':
    raw_feed = load()
    # print(type(raw_feed))
    feed = FrozenJSON(raw_feed)
    # print(len(feed.Schedule.speakers)) #357
    # print(sorted(feed.Schedule.keys())) # ['conferences', 'events', 'speakers', 'venues']
    # for key, value in sorted(feed.Schedule.items()):
    #     print("{:3} {}".format(len(value), key))

    print(feed.Schedule.speakers[-1].name)
    talk = feed.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk.speakers)
