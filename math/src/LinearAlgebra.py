# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 23:39:48 2019

@author: vargo
"""
import numpy as np


def Rotation2D(theta, vector):
    A = np.matrix([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    return A@vector
