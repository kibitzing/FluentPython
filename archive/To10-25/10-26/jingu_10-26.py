#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 26/10/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        데코레이터팩토리 연습
        데코레이터로 꾸며줄 때 파라미터로 정보를 받아서 다르게 꾸며줄 수 있다.
        오버로드 느낌.
"""


import math
import numpy as np

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def prediction(method):
    def decorate(func):
        def predict(*_args):
            if method=='regression':
                y = func(*_args)
            else: # classification
                y = [sigmoid(func(*_args)) > 0.5]
            return y
        return predict
    return decorate

@prediction(method='regression')
def linearRegression(x, theta):
    return np.dot(x, theta)

@prediction('classfication')
def linearClassification(x, theta):
    return np.dot(x,theta)

@prediction('regression')
def polynomialRegression(x, theta):
    x = [i**(p+1) for i, p in zip(x, (range(len(x))))]
    return np.dot(x, theta)

@prediction('classfication')
def polynomialClassficiation(x, theta):
    x = [i**(p+1) for i, p in zip(x, (range(len(x))))]
    return np.dot(x, theta)

x = [1,2,3]
theta1 = [1,3,5]
theta2 = [1,3,-5]
print("x: {0}, theta: {1}".format(x, theta1))
print('linearRegression:',linearRegression(x, theta1))
print('linearClassification:',linearClassification(x, theta1))

print('polynomialRegression:',polynomialRegression(x, theta1))
print('polynomialClassficiation:',polynomialClassficiation(x, theta1))

print("x: {0}, theta: {1}".format(x, theta2))
print('linearRegression:',linearRegression(x, theta2))
print('linearClassification:',linearClassification(x, theta2))

print('polynomialRegression:',polynomialRegression(x, theta2))
print('polynomialClassficiation:',polynomialClassficiation(x, theta2))
#
# x: [1, 2, 3], theta: [1, 3, 5]
# linearRegression: 22
# linearClassification: [True]
# polynomialRegression: 148
# polynomialClassficiation: [True]
# x: [1, 2, 3], theta: [1, 3, -5]
# linearRegression: -8
# linearClassification: [False]
# polynomialRegression: -122
# polynomialClassficiation: [False]
