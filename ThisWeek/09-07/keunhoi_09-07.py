#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Example 2-2
# 변형 : 깨진 한글과 깨지지 않은 한글 추출
symbols = '아#*버$*지#*$*!'
codes = [ord(symbol) for symbol in symbols]
unnormal_chars = [ord(symbol) for symbol in symbols if ord(symbol) < 1000]
normal_chars = [ord(symbol) for symbol in symbols if ord(symbol) >= 1000]

print(codes)
print(unnormal_chars)
print(normal_chars)

# Example 2-3
import time

symbols = '#*$*!!&'

start_time = time.time()
beyond_ascii = [ord(s) for s in symbols if ord(s) > 40]
end_time = time.time()
elapsed = end_time - start_time

start_time2 = time.time()
beyond_ascii2 = list(filter(lambda  c: c > 127, map(ord, symbols)))
end_time2 = time.time()
elapsed2 = end_time2 - start_time2

result = (elapsed == elapsed2)
print("Is Time(1) = Time(2) ? :", result)
