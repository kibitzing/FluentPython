#%% 09-14
from array import array
import numpy as np
from random import random
from time import time
floats = array('d', (random() for i in range(10**7)))
print (floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print (floats2[-1])
print (floats2 == floats)

floats3 = array(floats2.typecode, sorted(floats2))

t = time()
floats3 = array(floats2.typecode, sorted(floats2))
floats3 *= 10
print ('array time :',time()-t)
t = time()
floats4 = np.sort(floats2)
floats4 *= 10
print ('numpy time :',time()-t)

print ('original  array : ',floats2[:5])
print ('sorted by array : ',floats3[:5])
print ('sorted by numpy : ',floats4[:5])

### numpy가 array보다 훨신 빠르다!
### 책에서 서술한 numpy장점인 C and Fortran codebase coding이 array에는 적용되지 않은듯...

#%% 09-15
from collections import deque
import numpy as np
from time import time
from random import shuffle

maxlen = 100
minlen =  20
batchsize = 100

imageset = np.random.randn(50000,32,32,3)

start = time()
imageset = deque([img for img in imageset])
imagequeue = deque([], maxlen = maxlen*batchsize)

while(len(imageset)>0):
    if len(imagequeue) < minlen:
        while (len(imagequeue) < maxlen):
            imagequeue.append(imageset.popleft())
            
        shuffle(imagequeue)
    
    batch_image = np.array([imagequeue.popleft() for _ in range(batchsize)])
    
print ('dequeue provider : ', time() - start)


imageset = np.random.randn(50000,32,32,3)


maxlen = 100
minlen =  20
batchsize = 100

start = time()
imageset = [img for img in imageset]
imagequeue = []

while(len(imageset)>0):
    if len(imagequeue) < minlen:
        while (len(imagequeue) < maxlen):
            imagequeue.append(imageset.pop())
            
        shuffle(imagequeue)
    
    batch_image = np.array([imagequeue.pop() for _ in range(batchsize)])
    
print ('list-right provider : ', time() - start)

imageset = np.random.randn(50000,32,32,3)


maxlen = 100
minlen =  20
batchsize = 100

start = time()
imageset = [img for img in imageset]
imagequeue = []

while(len(imageset)>0):
    if len(imagequeue) < minlen:
        while (len(imagequeue) < maxlen):
            imagequeue.insert(0,imageset[0])
            del imageset[0]
            
        shuffle(imagequeue)
    
    batch_image = np.array(imagequeue[:batchsize])
    imagequeue[:batchsize] = []
    
print ('list-left provider : ', time() - start)

### dataset provider를 naive하게 제작
### 억지로 list의 left에서 pop을 하려고하면 느려지기는 한데 큰 의미는 없는 듯 함


