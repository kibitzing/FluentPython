#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = "PYTHON"
dummy = [ord(x) for x in x]

print(dummy)

symbols = ")(*&^%$#@!"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 40]

print(beyond_ascii)