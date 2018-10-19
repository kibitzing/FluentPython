from operator import mul
from functools import partial

triple = partial(mul, 3)
print (triple(7))
print (list(map(triple, range(1, 10))))

import numpy as np

def SUM(y, x):
    return np.sum(x, axis = y)
relu = partial(np.maximum, 0)
GAP = partial(SUM, (0,1))
n_relu = relu(np.random.randn(10,4,4,32))
n_gap = GAP(n_relu)

def where(a,b,c):
    return np.where(np.isfinite(c),b,a)

remove_nan = partial(where, 1, 0)
n_nan = np.random.randn(10,4,4,32)/n_relu
print ('number of NaNs in n_nan is :', np.sum(1-np.isfinite(n_nan)))
n_no_nan = remove_nan(n_nan)
print ('number of NaNs in n_no_nan is :', np.sum(1-np.isfinite(n_no_nan)))
