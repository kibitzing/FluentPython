#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Working example for my blog post at:
# https://danijar.github.io/structuring-your-tensorflow-models

""" 객체의 값과 정체성에 관한 예제
"""

charles = {'name': 'Charles L. Dodgson', 'born': 1832}
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex == charles)  # False

lewis = charles
id(charles)
id(lewis)

lewis['balance'] = 950

alex == charles  # True; 객체의 값을 비교

alex is not charles  # True; 객체의 정체성을 비교