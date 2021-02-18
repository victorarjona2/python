#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:23:55 2019

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import matplotlib.pyplot as plt
import numpy as np
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION

    SAY YOU HAVE...

    g:X->Y
    y = g(x)

    ...AND YOU WANT TO MAKE IT EQUAL TO SOME VALUE, SAY

    y_*, THEN...

    g(x) = y_* ---> g(x) - y_* = 0

    NOW MAKE f(x) SUCH THAT...

    f:X->Y
    f(x) = g(x) - y_*

    NOW FIND WHEN f(x) = 0

    A TAYLOR SERIES EXPANSION GENERATES A LINEAR APPROXIMATION OF f(x) AT AN
    ARBITRARY VALUE OF X SUCH THAT...

    f(x) ~= f(k) + f_prime(k)*(x-k)
            ____   __________ _____
              |         |        +-------> APPROXIMATION CENTERED AT k
              |         +----------------> THE DERIVATIVE OF f EVALUATED AT k
              +--------------------------> f EVALUATED AT k

    ...THEREFORE APPROACHING THE VALUE OF x THAT MAKES THE TAYLOR SERIES
    EXPANSION EQUAL TO ZERO...

    f(k) + f_prime(k)*(x-k) = 0 --> x = k - f(k)/f_prime(k)
                                        _   ____ _________
        k element of X <----------------+     |      |
        f evaluated at k <--------------------+      |
        df/dx evaluated at k <-----------------------+

    ...YA-DAH, YA-DAH, WE CAN MAKE OUR APPROXIMATION DEPENDENT ON THE PREVIOUS
    APPROXIMATION. WE GET...

    x_{n} DEFINED AS THE nth APPROXIMATION...
    x_{n + 1} = x_{n} - f(x_{n})/f_prime(x_{n})

    OR...

    x_{n + 1} = x_{n} - inverse(f_prime(x_{n}))@f(x_{n})

DESCRIPTION
'''

# TODO:
#   1) FINISH MAKING A SECANT METHOD THAT CAN BE USED WITH VECTORS. REFER
#       TO THE LIMIT DEFINITION OF A DERIVATIVE.
#   2) FILL IN THE DESCRIPTION OF eps.
#   3) ADD COMMENTARY ON THE NEWTON METHOD'S WHILE LOOP.
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


def NewtonMethod(x_start, y, f, Jf, eps):
    '''          _______  _  _  __  ___
                    |     |  |   |   +------> TODO: FILL IN DESCRIPTION
                    |     |  |   +----------> THE JACOBIAN OF f
                    |     |  +--------------> f:X->Y
                    |     +-----------------> THE VALUE OF Y WE WANT TO APPROX
                    +-----------------------> OUR FIRST APPROXIMATION/GUESS
    '''
#   BANTER
    print("Newton Method starts NOW!")
#   START COLLECTING YOUR INPUT VALUES...
    x_vals = [x_start]
#   ... AND YOUR OUTPUT VALUES.
    y_vals = []
    fx = f(x_start)
    y_vals.append(fx)
#   BANTER
    print(str(x_start) + "\n")
#   USE YOUR PRE-DEFINED SQUARE JACOBIAN MATRIX TO GENERATE AN INVERSE MATRIX.
    invJf = np.linalg.pinv(Jf(x_start))
#   GENERATRE THE NEW VALUE.
    '''
     +-------------------------------> THE NEW APPROXIMATION
     |        +----------------------> THE PREVIOUS INPUT VALUE
     |        |        +-------------> THE INVERSE JACOBIAN SQUARE MATRIX
     |        |        |     +-------> f EVALUATED AT THE PREVIOUS INPUT VALUE
     |        |        |     |   +---> THE DESIRED OUTPUT
    _|__   ___|___   __|__  _|_ _|_
    '''
    nu_x = x_start - invJf@(fx - y)
#   EVALUATE f AT THE NEW INPUT VALUE...
    fx = f(nu_x)
#   ... STORE THE NEW INPUT VALUE...
    x_vals.append(nu_x)
#   ... AND DO THE SAME WITH THE NEW EVALUATION OF f.
    y_vals.append(fx)
#   THIS IS WHERE ALL THE MAGIC HAPPENS. TODO: ADD COMMENTS.
    while np.linalg.norm(x_vals[-1] - x_vals[-2]) > eps:
        pre_x = x_vals[-1]
        fx = f(pre_x)
        y_vals.append(fx)
        invJf = np.linalg.pinv(Jf(pre_x))
        x_vals.append(pre_x - invJf@(f(pre_x) - y))
        print(str(x_vals[-1]) + "\n")
    return [x_vals, y_vals]


def SecantMethod(f, x_1, x_2, eps):
    print("Secant Method starts NOW!")
    x_vals = [x_1, x_2]
    y_vals = [f(x_1), f(x_2)]
#   TODO: DO THE MATH! GO THROUGH THE LIMIT DEFINITION OF THE DERIVATIVE
#   AND APPROXIMATE THE JACOBIAN USING THE FIRST AND SECOND INPUT VALUE.
# CONTENT ------------------------------------------------------------------- #
