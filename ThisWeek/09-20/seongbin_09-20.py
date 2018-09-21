from random import randint
import math
import time
target = [['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ '],
          ['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ '],
          ['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ '],
          ['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ '],
          ['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ '],
          ['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ '],
          ['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ '],
          ['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ '],
          ['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ '],
          ['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ '],
          ['□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']]
#'▣'


dart = {1,1.5,2}

def make_target(target):
    for i in range(11):
        str = ''
        for j in range(11):
            str = str+target[i][j]
        print(str)
def shot(dart, target):
    i = randint(0,10)
    j = randint(0,10)
    target[i][j] = '▣ '
    make_target(target)
    k = dart.pop()
    point =(100 - math.sqrt((i-5)**2+(j-5)**2))*k
    print((100 - math.sqrt((i-5)**2+(j-5)**2))*k)
    print('point : ' +str(point))
    
make_target(target)
print('ready~!')
time.sleep(2)
print('shot')
time.sleep(1)
print('')
print('')
print('')
print('')
print('')
print('')
shot(dart,target)
time.sleep(5)
print('')
print('')
print('')
print('')
print('')
print('')
shot(dart,target)
time.sleep(5)
print('')
print('')
print('')
print('')
print('')
print('')
shot(dart,target)