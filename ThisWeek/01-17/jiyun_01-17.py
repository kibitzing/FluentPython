from collections import abc
from keyword import iskeyword

class FrozenJSON:
    """ 점 표기법을 이용해서 JSON과 유사한 객체를 둘러보기 위한
        읽기 전용 퍼사드 클래스
    """
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

# >>> grad = grad = FrozenJSON({'True':1,'False':0})
# >>> grad.True_
# 1
# >>> grad.False_
# 0

