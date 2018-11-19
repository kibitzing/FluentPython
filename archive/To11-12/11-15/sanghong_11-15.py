import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

# 오늘 원근이형을 도와 간단한 bounding box 만드는 것을 해보았다. (영상에서) 아래 코드는 그 중 사용한 bounding box 코드 이다.
# 영상을 올리려 했으나 용량이 너무 커서 original.png 만올린다.


img = cv2.imread('original.png', cv2.IMREAD_COLOR)
img_red = cv2.imread('original.png', cv2.IMREAD_COLOR)
print(img.shape)

x1 = 230
y1 = 170
x2 = 620
y2 = 333
size_x = x2 - x1
size_y = y2 - y1
a = sys.argv[1]

if 1 == 1:
    # black
    for i in range(3):
        for k in range(size_x):
            img[y1 + i, x1 + k, :] = 0
            img[y2 + i, x1 + k, :] = 0
        for k in range(size_y):
            img[y1 + k, x1 + i, :] = 0
            img[y1 + k, x2 + i, :] = 0
if a == 'red':
    # read
    for i in range(3):
        for k in range(size_x):
            img[y1 + i, x1 + k, 0] = 255
            img[y2 + i, x1 + k, 0] = 255
        for k in range(size_y):
            img[y1 + k, x1 + i, 0] = 255
            img[y1 + k, x2 + i, 0] = 255


plt.imshow(img)
plt.show()
