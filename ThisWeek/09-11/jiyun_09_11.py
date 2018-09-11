# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:47:16 2018

@author: jiyun
"""

a,b,c,*d = range(10)
print(a,b,c,d) #0 1 2 [3, 4, 5, 6, 7, 8, 9]

###############################################################

metro_areas = [
    ('Mexico City','MX',20.142,(19.433333,-99.133333)),
    ('New York_Newark','US',20.104,(40.808611,-74.020386)),
    ('Sao Paulo','BR',19.649,(-23.547778,-46.635833)),
    ]
print('{:^15} | {:^9} | {:^9}'.format('City','lat.','long.'))
fmt = '{:^15} | {:^9.4f} | {:^9.4f}'
for name,cc,pop,(latitude, longitude) in metro_areas:
    if longitude >= -90:
        print(fmt.format(name,latitude, longitude))
        
#################################################################
        
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
saopaulo = City('Sao Paulo','BR',19.649,(-23.547778,-46.635833))
print(saopaulo) 
#City(name='Sao Paulo', country='BR', population=19.649, coordinates=(-23.547778, -46.635833))

#################################################################

print(City._fields)
#('name', 'country', 'population', 'coordinates')
LatLong = namedtuple('Latlong', 'lat long')
mexico_data = ('Mexico City','MX',20.142,(19.433333,-99.133333))
mexico = City._make(mexico_data)
mexico._asdict()
for key, value in mexico._asdict().items():
    print(key + ':', value)    
    
#################################################################
    
print(saopaulo.__len__()) #4
print(saopaulo.__mul__(2)) 
#('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833), 'Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
print(saopaulo.__getitem__(2)) #19.649

#################################################################    
    
a = [1,2,3,4,5]
print(a[:]) #[1, 2, 3, 4, 5]
print(a[:-1]) #[1, 2, 3, 4]
print(a[:-2]) #[1, 2, 3]
print(a[2:]) #[3, 4, 5]
