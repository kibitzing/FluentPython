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