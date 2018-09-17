# 가상으로 구현한 loocv(leave one out cross validation)기법

from collections import deque
import numpy as np
import random
import time
import math
def cross_validation(dataset, address ,acc):
    print("%d th test_set : %s" % (int(address+1),dataset[address]))
    print("cross_validation %d times... " % int(address+1))
    print("accuracy : %.5f %%" % float(acc*100))
    time.sleep(0.3)
#make fake 10000 datasets that have 7 features and 1 label
dataset = np.zeros((10000,8))
acc = 0
for i in range(10000):
    for j in range(0,6):
        dataset[i,j] = random.randrange(1,10)
    dataset[i,7] = random.choice([True, False])
dataset_address = deque(range(10000),maxlen = 10000)
for i in range(dataset_address.__len__()):
    cross_validation(dataset,i,acc)
    acc = math.tanh((i/100000000)*i*i)
    dataset_address.rotate(-1)





