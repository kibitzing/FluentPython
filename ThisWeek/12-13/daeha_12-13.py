#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Tensorflow generator example
    I'm refer below link:
    https://gist.github.com/elgehelge/6c7cd65bd08b71b898fb54eb13ed6f98

"""

import tensorflow as tf
print('tensorflow version is {}'.format(tf.__version__))

def data_generator(start, end):
    for x, y in zip(range(start, end), range(start, end)):
        print(x, y)
        yield x, y
        

def input_fn(data_getter):
    dataset = (tf.data.Dataset.from_generator(
            generator=lambda: data_getter,
            output_types=(tf.float32),
            )
    .repeat()
    .make_one_shot_iterator().get_next()
    )
    
    return dataset[0], dataset[1]


def model_fn(features, labels, mode):
    var = tf.Variable(0, dtype=tf.float32)
    prediction = features + var
    loss = prediction - labels
    loss.set_shape([])
    
    return tf.estimator.EstimatorSpec(
            mode=mode,
            predictions=prediction,
            loss=loss,
            train_op=tf.contrib.layers.optimize_loss(
                    loss=loss,
                    global_step=tf.train.get_global_step(),
                    optimizer=tf.train.AdamOptimizer,
                    learning_rate=0.01
            ),
    )

         
def run():
    tf.logging.set_verbosity(tf.logging.DEBUG)
    
    train_data_gen = data_generator(start=0, end=5)
    eval_data_gen = data_generator(start=100, end=105)
    
    estimator = tf.estimator.Estimator(model_fn=model_fn)
    train_spec = tf.estimator.TrainSpec(
            input_fn=lambda: input_fn(train_data_gen))
    eval_spec = tf.estimator.EvalSpec(
            input_fn=lambda: input_fn(eval_data_gen), start_delay_secs=0)
    tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)
    
    
if __name__ == '__main__':
    run()