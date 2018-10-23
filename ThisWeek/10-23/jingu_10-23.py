#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 23/10/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        practice using decorator and global
        어떤 라이브러리 쓰는 함수를 사용할 때만 그 라이브러리를 호출하게 한다.
"""
os_funcList = []
tf_funcList = []

def importOS(funcUsingOS):
    if len(os_funcList) == 0:
        print("from os import system as sys")
        # global os, system
        global sys
        from os import system as sys
    os_funcList.append(funcUsingOS)
    return funcUsingOS

def importTF(funcUsingTF):
    if  len(tf_funcList) == 0:
        print("import tensorflow as tf")
        global tf
        import tensorflow as tf
    tf_funcList.append(funcUsingTF)
    return funcUsingTF

@importOS
def printCurrentDir():
    sys('pwd')

@importOS
def printDirList():
    sys('ls')


@importTF
def initialization():
    global sess
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)
    print('initialization Complete')

@importTF
def layerSetting():
    global X, W1, L1, W2, L2, W3

    X = tf.placeholder(tf.float32, [None, 784])

    W1 = tf.Variable(tf.random_normal([784, 256], stddev=0.01))
    # 입력값에 가중치를 곱하고 ReLU 함수를 이용하여 레이어를 만듭니다.
    L1 = tf.nn.relu(tf.matmul(X, W1))

    W2 = tf.Variable(tf.random_normal([256, 256], stddev=0.01))
    # L1 레이어의 출력값에 가중치를 곱하고 ReLU 함수를 이용하여 레이어를 만듭니다.
    L2 = tf.nn.relu(tf.matmul(L1, W2))

    W3 = tf.Variable(tf.random_normal([256, 10], stddev=0.01))
    # 최종 모델의 출력값은 W3 변수를 곱해 10개의 분류를 가지게 됩니다.
    model = tf.matmul(L2, W3)
    print('layer setting Complete')

printCurrentDir()
printDirList()
initialization()
layerSetting()

print(os_funcList)
print(tf_funcList)