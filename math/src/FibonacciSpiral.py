#!/usr/bin/env python5
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:23:25 2020

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

def ContinuousFibonacci(nth_val):
    fib_n = np.complex(np.power((1+np.sqrt(5))/2, nth_val))
    weird_phi = np.complex((1-np.sqrt(5))/2)
    fib_n -= np.power(weird_phi, nth_val)
    return fib_n/np.sqrt(5)

def FibonacciSpiralPlot(up_to, res = 100):
    t_vals = np.linspace(1, up_to, res)
    f_vals = [ContinuousFibonacci(tt) for tt in t_vals]
    
    reals = np.real(f_vals)
    imags = np.imag(f_vals)
    
    fig = plt.figure(figsize=(11, 7))
    
    ax1 = fig.add_subplot(131, projection='3d')
    plt.grid()
    ax1.set_xlabel("t vals")
    ax1.set_ylabel("imaginary fibonacci vals")
    ax1.set_zlabel("fibonacci vals")
    plt.plot(t_vals, imags, reals)
    
    ax2 = fig.add_subplot(132)
    plt.grid()
    plt.plot(t_vals, imags)
    
    ax3 = fig.add_subplot(133)
    plt.grid()
    plt.plot(t_vals, reals)