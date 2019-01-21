#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" matrix inversion vs. solving

    Refer below link:
    https://github.com/RuiShu/tensorflow-gp/blob/master/exp/solve_sym_pos_matrix.ipynb

"""
import numpy as np
from scipy.linalg import solve
from numpy.linalg import inv
import time
import matplotlib.pyplot as plt

import asyncio

n = 1000
K = np.random.randn(n, n)
K = K.dot(K.T)
Y = np.random.randn(n, n)

def generate(n):
    K = np.random.randn(n, n)
    K = K.dot(K.T)
    Y = np.random.randn(n, n)
    return K, Y


def solve_by_inv(K, Y):
    # Solve by matrix inversion
    t = time.time()
    X = inv(K).dot(Y)
    t = time.time() - t
    err = abs(K.dot(X) - Y).mean()
    return err, t


def solve_by_sol(K, Y):
    t = time.time()
    X = solve(K, Y, sym_pos=True)
    t = time.time() - t
    err = abs(K.dot(X) - Y).mean()
    return err, t



# Solve by matrix inversion
err, t = solve_by_inv(K, Y)
print("Solution check: ", err)
print("Computation time: ", t)



# 1) Naive method
ns = np.power(8, np.linspace(1, 3.5, num=10)).astype(int)
trials = 3
inv_err = np.zeros(trials*len(ns))
sol_err = np.zeros(trials*len(ns))
inv_t = np.zeros(trials*len(ns))
sol_t = np.zeros(trials*len(ns))
x = np.zeros(trials*len(ns))

i = 0
for n in ns:
    print("n: ", n)
    for _ in range(trials):
        K, Y = generate(n)
        err1, t1 = solve_by_inv(K, Y)
        err2, t2 = solve_by_sol(K, Y)
        inv_err[i] = err1
        sol_err[i] = err2
        inv_t[i] = t1
        sol_t[i] = t2
        x[i] = n
        
        i = i + 1
        print("*"*77)
        print("Error: ", err1, "\t", err2)
        print("Time: ", t1, "\t", t2)


# 2) Coroutine
ns = np.power(8, np.linspace(1, 3.5, num=10)).astype(int)
trials = 3
inv_err = np.zeros(trials*len(ns))
sol_err = np.zeros(trials*len(ns))
inv_t = np.zeros(trials*len(ns))
sol_t = np.zeros(trials*len(ns))
x = np.zeros(trials*len(ns))

def co_generate(n):
    K = np.random.randn(n, n)
    K = K.dot(K.T)
    Y = np.random.randn(n, n)
    yield [K, Y]

i = 0
for n in ns:
    print("n: ", n)
    args = co_generate(n)
    [K, Y] = next(args)
    #K, Y = await K, Y
    err1, t1 = solve_by_inv(K, Y)
    err2, t2 = solve_by_sol(K, Y)
    inv_err[i] = err1
    sol_err[i] = err2
    inv_t[i] = t1
    sol_t[i] = t2
    x[i] = n
    
    i = i + 1
    print("*"*77)
    print("Error: ", err1, "\t", err2)
    print("Time: ", t1, "\t", t2)