#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:49:57 2019

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import numpy as np
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION

f_0 = 1
f_1 = 1
f_n = f_{n - 1} + f_{n - 2} FOR ALL INTEGER VALUES OF n > 2.

THIS SEQUENCE LOOKS LIKE THIS: 1, 1, 2, 3, 5, 8, 11, ...
AD INFINITUM.

FibonacciNumberGenerator
    N - THIS INPUT VALUE IS AN INTEGER USED TO GENERATE THE Nth NUMBER. FOR
    EXAMPLE, IF N=3, THEN THE PROGRAM OUTPUTS 3.

FibonacciListGenerator
    SAME AS FibonacciNumberGenerator, EXCEPT WE GENERATE A LIST INSTEAD OF JUST
    RETURNING THE Nth VALUE.

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


# PRE-SET VARIABLE FOR TESTING PURPOSES
f0 = np.array([[1], [0]])


def FibonacciNumberGenerator(N):
    if N == 0:
        print("Bruh, you ain't going no where")
        return
    elif N <= 2:
        return 1
    f1 = 1
    f2 = 1
    nu = f2 + f1
    for ii in range(3, N):
        f1 = f2
        f2 = nu
        nu = f2 + f1
    return nu


def FibonacciListGenerator(N):
    if N == 0:
        print("Bruh, you ain't going no where")
        return
    elif N < 2:
        return [1]
    fibs = [1, 1]
    if N == 2:
        return fibs
    else:
        for ii in range(2, N):
            fibs.append(fibs[ii - 1] + fibs[ii - 2])
    return fibs


def FibonacciListGeneratorUpTo(up_to):
    if up_to < 1:
        print("Bruh, you ain't going no where")
        return
    fibs = [1, 1]
    while fibs[-1] != up_to:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def FibonacciLA1(fiV, n):
    fi_mx = np.matrix([[1, 1],
                       [1, 0]])
    for ii in range(n):
        fiV = fi_mx@fiV
    return fiV
