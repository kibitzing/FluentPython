### network를 학습하고 variables를 mat file로 저장하고 다시 불러와 load하는 코드 작성
import tensorflow as tf
slim = tf.contrib.slim
import scipy.io as sio
import numpy as np
import re
### network 생성
img = tf.placeholder(tf.float32, [None, 32, 32,3])
conv = slim.conv2d(img,   8, kernel_size=[3,3], stride = 2, scope = 'conv0')
conv = slim.conv2d(conv, 16, kernel_size=[3,3], stride = 2, scope = 'conv1')
conv = slim.conv2d(conv, 32, kernel_size=[3,3], stride = 2, scope = 'conv2')
feat = tf.reduce_mean(conv,[1,2])
feat = slim.fully_connected(feat, 100, scope = 'fc', activation_fn = None)


### network의 trainable variables 중 convolution의 parameter 저장
variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
sess = tf.Session()
sess.run(tf.global_variables_initializer())

var = {v.name[:-2] : sess.run(v)+1 
       for v in variables 
       if len(re.findall('conv',v.name)) > 0}

print ([np.mean(sess.run(v)) for v in variables])
sio.savemat('params.mat', var)

### network의 trainable variables load 및 있는 것만 assign
params = sio.loadmat('params.mat')
for v in variables:
    p = params.get(v.name[:-2])
    if p is not(None):
        sess.run(tf.assign(v, p.reshape(*v.get_shape().as_list())))

variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
print ([np.mean(sess.run(v)) for v in variables])


