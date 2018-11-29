#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 연산자 오버로딩 예제

    본 예제는 tensorflow custom op library(.cc)를 바탕으로 실험을 진행한다.
    또한 아래 link를 참조하여 작성하였다.
    https://github.com/Coolnesss/tf-custom-log-loss
"""

import tensorflow as tf
import numpy as np
print('Version of tensorflow is {}'.format(tf.__version__))

class LogLossTest(tf.test.TestCase):
    def testLogLoss(self):
        log_loss_module = tf.load_op_library('./log_loss.so')
        with self.test_session():
            pred = np.array( [0.375, 0.371, 0.3939, 0.375] )
            y = np.array( [1, 0, 1, 0] )
            bias = 0.5

            result = log_loss_module.log_loss(y, pred).eval()
            correct = np.sum( -(y * np.log(pred + 1e-7) + (1 - y) * np.log(1 - pred + 1e-7)) )
            self.assertAlmostEqual(result, correct, places=5)

            #TODO(): 연산자 특수 메서드 사용
            print('correct with bias is {}'.format(correct.__add__(bias)))

if __name__ == "__main__":
    tf.test.main()
