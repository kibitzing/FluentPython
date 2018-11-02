from array import array
import math

class Vector2d:
    """this is 2d vector class """
    typecode = 'd'

    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        self.x = self.x+other.x
        self.y = self.y+other.y

    def __sub__(self, other):
        self.x = self.x-other.x
        self.y = self.y-other.y

    def dot(self, other):
        return self.x * other.x + self.y * other.y



def computeCost(x, y, theta,j):
    m = len(x)
    h = [0]*m
    print(x)
    print(y)
    print(theta)
    print(j)
    for i in range(m):
        h[i] = x[i].dot(theta)
        j = j+(h[i]-y[i])**2

    return j/(2*m)
'''
origin y = 1*x_1+2*x_2
x_1,x_2,y = 0 0 0
            0 1 2
            1 1 3
            2 1 4
            2 2 6
'''
x = (Vector2d(0,0),Vector2d(0,1),Vector2d(1,1),Vector2d(2,1),Vector2d(2,2))
y = [0,2,3,4,6]
theta = Vector2d(1,2)
j = 0
'''나중에할래
def gradientDescent(x,y,theta,alpha,num_iters,datalen):
    h = [0]*
    for i in range(num_iters):
        h = x.dot(theta)
        theta.x = theta.x - (alpha*(h-y)*x.x)/datalen
        theta.y = theta.y - (alpha*(h-y)*x.y)/datalen
'''
print(computeCost(x,y,theta,j))
