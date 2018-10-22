import numpy as np
def computeCost(X, y, theta):
    J = 0;
    m = len(y)
    for i in range(m):
        h = np.subtract(np.dot(X,theta), y)
        J = J + (h[i]-y[i])**2
    J = J/(2*m);
    return J
X = np.array([
    [1,1],
    [1,2],
    [1,3],
    [1,4]])
y = np.array([
    [1],
    [2],
    [3],
    [4]
])
theta = np.array([
    [0],
    [0]
])

print(computeCost(X,y,theta))
#print(computeCost.__default__)
print(computeCost.__code__)
print(computeCost.__code__.co_varnames)
print(computeCost.__code__.co_argcount)