from array import array
import math
import csv

class Vector2d:
    """this is 2d vector class """
    typecode = 'd'

    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

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

    def __divmod__(self, other):
        self.x = self.x/other.x
        self.y = self.y/other.y

    #추가부분
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


#변경점 -> x는 단일 데이터가 아닌 데이터 셋

def computeCost(x, y, theta):
    j = 0
    m = len(x)
    #h = [0]*m
    h = [Vector2d(0,0) for i in range(m)]
    for i in range(m):
        h[i] = Vector2d(0,x[i].dot(theta))
        j = j+(h[i].y-y[i].y)**2

    return j/(2*m)

def gradientDescent(x,y,theta,alpha,num_iters):
    m = len(x)
    J_his = [0]*num_iters
    h = [Vector2d(0, 0) for i in range(m)]

    for i in range(num_iters):
        temp_x = 0
        temp_y = 0
        for j in range(m):
            h[j] = Vector2d(0, x[j].dot(theta))
            temp_x = temp_x + (0 + (alpha*(h[j].y-y[j].y)*x[j].x)/m)
            temp_y = temp_y + (0 + (alpha*(h[j].y-y[j].y)*x[j].y)/m)

        theta = Vector2d(theta.x-temp_x,theta.y-temp_y)
        J_his[i] = computeCost(x,y,theta)
        print(J_his[i])
    return (theta,J_his)


with open('normdata.csv') as f:
    reader = csv.reader(f,delimiter=',')
    data = [(col1, col2, col3,col4,col5,col6) for col1, col2, col3,col4,col5,col6 in reader]
y = [Vector2d(0,float(data[i][5])) for i in range (len(data))]
x_column = [Vector2d(data[i][3], data[i][4]) for i in range(len(data))]

theta = Vector2d(1,1)
j = 0

print(computeCost(x_column, y, theta))
print(gradientDescent(x_column,y,theta,0.01,10000000))


#그냥 넘파이를 쓰자 ;
