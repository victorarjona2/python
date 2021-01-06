#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:33:18 2020

@author: sysadmin
"""
# IMPORTS ------------------------------------------------------------------- #
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import tensorflow as tf
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION
BOOK: DEEP LEARNING WITH PYTHON
CHAPTER2.1 - A FIRST LOOK AT A NEURAL NETWORK

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

# LISTING 2.1   LOADING THE MNIST DATASET IN KERAS
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# DEBUG: SHAPE AND LENGTH OF ELEMENTS ABOVE
# train_images.shape
# len(train_labels)
# train_labels
# test_images.shape
# len(test_labels)
# test_labels

# LISTING 2.2   THE NETWORK ARCHITECTURE
network = models.Sequential()
network.add(layers.Dense(512,
                         activation='relu',
                         input_shape=(28*28,)
                         ))
network.add(layers.Dense(10,
                         activation='softmax'
                         ))

# LISTING 2.3   THE COMPILATION STEP
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# LISTING 2.4   PREPARING THE IMAGE DATA
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32')/255
test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32')/255

# LISTING 2.5   PREPARING THE LABELS
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# TRAINING
network.fit(train_images,
            train_labels,
            epochs=5,
            batch_size=128)

# EVALUATE ACCURACY AND LOSS
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('\nTest acc: {}\nTest loss: {}'.format(test_acc, test_loss))
