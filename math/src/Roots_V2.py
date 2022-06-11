#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:23:55 2019

@author: victor
"""
# TODO: fix NM and SM to be part of class
import matplotlib.pyplot as plt
import numpy as np

class Roots():
    """
    The Roots class is a tool that provides a way to handle mathematical
    functions (preferably continuous) to find out what input value will
    provide the desired output.
    
    Initialization variables:
        fz      -   An function whos input is n-dimensional and output is
                    m-dimensional
        df_dz   - 
    """
    def __init__(self, fz, df_dz = None):
        self.fz = fz
        self.df_dz = df_dz

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
