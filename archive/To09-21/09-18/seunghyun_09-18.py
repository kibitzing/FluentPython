import tensorflow as tf
slim = tf.contrib.slim
import scipy.io as sio
img = tf.placeholder(tf.float32, [None, 32, 32,3])

conv = slim.conv2d(img,   8, kernel_size=[3,3], stride = 2, scope = 'conv0')
conv = slim.conv2d(conv, 16, kernel_size=[3,3], stride = 2, scope = 'conv1')
conv = slim.conv2d(conv, 32, kernel_size=[3,3], stride = 2, scope = 'conv2')
feat = tf.reduce_mean(conv,[1,2])
feat = slim.fully_connected(feat, 100, scope = 'fc', activation_fn = None)

variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
var = {v.name[:-2] : sess.run(v) for v in variables}
sio.savemat('params.mat', var)

### network에서 trainable variables를 추출해서 dictionalry로 저장하는 코드