#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p605-609
# Example 19-17~21

"""
	예제 위주로 작성
	객체 속성과 클래스 속성
	property의 고전적인 구문
"""

# Example 19-17
class LineItem1:
    """ property를 사용한 예제
    """

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('weight value must be > 0')


# Example 19-18
class LineItem2:
    """ 고전적인 구문
    """

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('weight value must be > 0')

    weight = property(get_weight, set_weight)


# Example 19-19~21
# 객체 속성과 클래스 속성 차이


# if __name__ == "__main__":