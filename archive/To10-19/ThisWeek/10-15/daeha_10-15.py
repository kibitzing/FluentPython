#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "daehakim"
__email__ = "kdhht5022@gmail.com"

"""
    string을 clipping하는 에제
"""

def clip(text, max_len=100):
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)

    return text[:end].rstrip()

clip.__defaults__

clip.__code__

clip.__code__.co_varnames

clip.__code__.co_argcount


