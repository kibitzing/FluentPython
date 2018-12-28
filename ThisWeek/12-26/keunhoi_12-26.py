#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p483-487
# Example 16-18~19

'''
   예제 위주 작성
'''

# Example 16-18
def example1618():
    _i = iter(EXPR)
    try:
        _y = next(_i)
    except StopIteration as _e:
        _r = _e.value
    else:
        while 1:
            _s = yield _y
            try:
                _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break

    Result = _r

# Example 16-19
def example1619():
    import sys
    _i = iter(EXPR)
    try:
        _y = next(_i)
    except StopIteration as _e:
        _r = _e.value
    else:
        while 1:
            try:
                _s = yield _y
            except GeneratorExit as _e:
                try:
                    _m = _i.close
                except AttributeError:
                    pass
                else:
                    _m()
                raise _e
            except BaseException as _e:
                _x = sys.exc_info()
                try:
                    _m = _i.throw
                except AttributeError:
                    raise _e
                else:
                    try:
                        _y = _m(*_x)
                    except StopIteration as _e:
                        _r = _e.value
                        break
            else:
                try:
                    if _s is None:
                        _y = next(_i)
                    else:
                        _y = _i.send(_s)
                except StopIteration as _e:
                    _r = _e.value
                    break
    RESULT = _r


if __name__ == '__main__':
    EXPR = [1,2,3,4]
    print('{0:=<50}'.format("Example 16-18"))
    example1618()
    print('{0:=<50}'.format("Example 16-19"))
    example1619()
