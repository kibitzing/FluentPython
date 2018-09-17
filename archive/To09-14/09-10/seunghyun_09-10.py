import random
import time
import numpy as np

rand = [random.uniform(-1,1) for _ in range(10000)]
neg_noise  = [r for i, r in enumerate(rand) if r < 0]
pos_noise = [r for i, r in enumerate(rand) if r >= 0]


t = time.time()
Neg_noise = [neg+pos for i, neg in enumerate(neg_noise)
                   for j, pos in enumerate(pos_noise)
                   if neg+pos < 0]
print (time.time()-t)


## 이런 단순연산은 아무래도 numpy array가 좋을 수 밖에 없음...
t = time.time()
neg_array = np.expand_dims(np.array(neg_noise),0)
pos_array = np.expand_dims(np.array(pos_noise),1)
Neg_array = neg_array+pos_array
Neg_array = Neg_array[np.where(Neg_array<0)]
print (time.time()-t)

colors = ['black', 'white']*1000
sizes = ['S', 'M', 'L']*1000

t = time.time()
tshirts = []
for color in colors:
    for size in sizes:
        tshirts.append((color, size))
print (time.time()-t)

t = time.time()        
tshirts_listcomp = [(color, size) for size in sizes for color in colors]
print (time.time()-t)

t = time.time()
tshirts_array = np.hstack(cs.reshape(-1,1) for cs in np.meshgrid(colors, sizes))
print (time.time()-t)

## 연산 속도는 for < listcomp <<< numpy
## numpy를 쓸 수 없는 상황일 때 listcomp를 고려하는게 좋을 듯
### tuple 예제는 할만한게 없어서 내일 한번에 하겠습니

