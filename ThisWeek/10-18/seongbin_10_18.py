from functools import reduce
from operator import mul

def fact(n):
    return reduce(mul, range(1,n+1))

print("fatorization 3 (3!) : "+str(fact(3)))

read_data = open('car.data','r')
data_tuple = [0]*1000
for i in range(0,1000):
    data_tuple[i] = read_data.readline()
    data_tuple[i] = data_tuple[i].split(',')
    data_tuple[i] = tuple(data_tuple[i])

from operator import itemgetter
#print(data_tuple)
for label in sorted(data_tuple, key= itemgetter(6)):
    print(label)
    
