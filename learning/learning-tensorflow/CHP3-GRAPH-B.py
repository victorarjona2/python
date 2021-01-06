#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:23:55 2019

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import tensorflow as tf
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
#   1 CONSTANTS
a = tf.constant(5.0)
b = tf.constant(3.0)

#   2 OPERATORS
c = tf.multiply(a, b)
d = tf.sin(c)
e = tf.divide(d, b)

#   3 CREATE SESSION
sess = tf.Session()

#   4 RUN AND CLOSE SESSION
outs = sess.run(e)
sess.close()

#   5 PRINT SOLUTION
print("outs = {}\n".format(outs))
