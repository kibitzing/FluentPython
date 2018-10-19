metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]   

from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(0)):
    print(city)
    
from functools import reduce
from operator import mul
import numpy as np

def size(n):
    return reduce(mul, n.shape)

def single_size(n):
    return reduce(mul, n.shape[1:])

def flatten(n):
    return n.reshape(-1, single_size(n))
a = np.zeros([8, 10,10,3])
print (size(a))
print (single_size(a))

a_flatten = flatten(a)
print (a_flatten.shape)