#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:23:55 2019

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION


DESCRIPTION
'''
# HELPER FUNCTIONS ---------------------------------------------------------- #
# HELPER FUNCTIONS ---------------------------------------------------------- #

# TABLE OF CONTENTS --------------------------------------------------------- #
#   1
#       1.1
#       1.2

# TABLE OF CONTENTS --------------------------------------------------------- #

# CONTENT ------------------------------------------------------------------- #
#   1
#       1.1

# CONTENT ------------------------------------------------------------------- #

# LOCATION WHERE DATA'S BEING DUMPED.
DATA_DIR = '/tmp/data'
#
NUM_STEPS = 1000
# BATCH SIZE FOR TRAINING
MINIBATCH_SIZE = 100

# DUMP DATA IN FOLDER
data = input_data.read_data_sets(DATA_DIR, one_hot=True)
# x IS THE PLACEHOLDER NODE. IT TAKES IN SOME NUMBER OF INPUTS, EACH THE SIZE
# OF 784 (28x28).
x = tf.placeholder(tf.float32, [None, 784])
# W IS THE MATRIX THAT WILL BE CONSTANTLY UPDATED EVERYTIME TO GET A BETTER
# ANSWER.
W = tf.Variable(tf.zeros([784, 10]))
# y_true IS A PLACEHOLDER NODE. IT TAKES IN SOME NUMBER OF INPUTS, EACH THE
# THE SIZE OF 10. WE USE THIS TO ADJUST OUR WEIGHTS.
y_true = tf.placeholder(tf.float32, [None, 10])
# y_pred WILL PERFORM THE ACTUAL CALCULATION OF x AND W
y_pred = tf.matmul(x, W)
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_pred, labels=y_true))
gd_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
correct_mask = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y_true, 1))
accuracy = tf.reduce_mean(tf.cast(correct_mask, tf.float32))
with tf.Session() as sess:
    # Train
    sess.run(tf.global_variables_initializer())
    for _ in range(NUM_STEPS):
        batch_xs, batch_ys = data.train.next_batch(MINIBATCH_SIZE)
        sess.run(gd_step, feed_dict={x: batch_xs, y_true: batch_ys})
    # Test
    ans = sess.run(accuracy, feed_dict={x: data.test.images,
                                        y_true: data.test.labels})
print("Accuracy: {:.4}%".format(ans*100))
