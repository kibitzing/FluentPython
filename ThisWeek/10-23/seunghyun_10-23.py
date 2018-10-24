import tensorflow as tf
slim = tf.contrib.slim

regularizer = []
def regularization(reg_func):
    regularizer.append(reg_func)
    return reg_func

@regularization
def l2_regularization(X):
    """l2_regularization"""
    return tf.norm(X, ord = 'euclidean')

@regularization
def l1_regularization(X):
    """l1_regularization"""
    return tf.norm(X, ord = 'fro')

@regularization
def kld_regularization(X, Y = None ,reverse = False):
    """kld_regularization"""
    if Y == None:
        """if Y is None generate unit Gaussian""" 
        Y = tf.random_normal(X.get_shape().as_list())
    
    if reverse : 
        X, Y = (Y, X) 
    
    X = tf.nn.softmax(X)
    Y = tf.nn.softmax(Y)
    kld = tf.reduce_sum(Y*tf.log(Y/X))
        
    return kld

### network 생성
img = tf.placeholder(tf.float32, [None, 32, 32,3])
conv = slim.conv2d(img,   8, kernel_size=[3,3], stride = 2, scope = 'conv_0')
conv = slim.conv2d(conv, 16, kernel_size=[3,3], stride = 2, scope = 'conv_1')
conv = slim.conv2d(conv, 32, kernel_size=[3,3], stride = 2, scope = 'conv_2')

feat = tf.reduce_mean(conv,[1,2])
feat = slim.fully_connected(feat, 100, scope = 'fc', activation_fn = None)
variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
reg_loss = []
for v in variables:
    reg_loss.append(regularizer[0](v))

reg_loss = tf.add_n(reg_loss)

