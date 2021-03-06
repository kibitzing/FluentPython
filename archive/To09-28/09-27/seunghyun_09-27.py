### network를 학습하고 variables를 mat file로 저장하고 다시 불러와 load하는 코드 작성
import tensorflow as tf
slim = tf.contrib.slim
import scipy.io as sio
import numpy as np
import re
### network 생성
img = tf.placeholder(tf.float32, [None, 32, 32,3])
conv = slim.conv2d(img,   8, kernel_size=[3,3], stride = 2, scope = 'conv_0')
conv = slim.conv2d(conv, 16, kernel_size=[3,3], stride = 2, scope = 'conv_1')
conv = slim.conv2d(conv, 32, kernel_size=[3,3], stride = 2, scope = 'conv_2')
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
### 어떤 parameter를 load할지 지정하는 것을 set과 dictionary로 구현

variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
var = {v.name[:-2] : v 
       for v in variables 
       }

layer_params = {'conv' : ('weights', 'biases'),
                'fc'   : ('weights', 'biases'),
                'bn' : ('moving_average', 'moving_variance',
                        'beta','gamma')}

layer_name = {re.split('/',v)[-2] for v in set(var)}
load_layers = {'conv_0', 'conv_1', 'fc'}

not_in_net = load_layers - layer_name
    
print ('below layers are not in net\n',layer_name) if len(not_in_net) > 0 else print ()

load_params = {(layer + '/'+param )
               for layer in load_layers
               for param in layer_params[re.split('_',layer)[0]]}

params = sio.loadmat('params.mat')
p_name = set(params)

load_params = load_params.__and__(p_name)

not_in_ptnet = load_params - p_name
print ('below layers are not in pre_trained params\n',not_in_ptnet) if len(not_in_ptnet) > 0 else print ()

for v in load_params:
    sess.run(tf.assign(var[v], params[v].reshape(*v.get_shape().as_list())))

variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
print ([np.mean(sess.run(v)) for v in variables])
