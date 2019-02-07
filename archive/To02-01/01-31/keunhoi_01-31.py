#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p645-ch20end
# Example 20-14

"""
    예제 위주로 작성
    프로퍼티 문서화

"""

# Example 20-14
import collections

class Text(collections.UserString):

    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]
        
# if __name__ == "__main__":