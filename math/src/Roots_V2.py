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
        f       -   An function whos input is n-dimensional and output is
                        m-dimensional.
        Jf      -   Essentially, the Jacobian of the function, "f"; basically,
                        the derivative with respect to "z". Read more here:
                        https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant
    """
    def __init__(self):
        pass
    
    def Define_Function(self, f):
        self.f = f
    
    def Define_Jacobian_Function(self, Jf):
        self.Jf = Jf
        
    def NewtonMethod(self, x_start, des_y, eps, debug=True):
        '''
        '''
        if debug:
            print("Newton Method starts NOW!\n")
    
        x_vals = [x_start]
        y_vals = [self.f(x_vals[-1])]
        
        Jf_x = self.Jf(x_vals[-1])
        inv_Jf = np.linalg.pinv(Jf_x)
        
        if debug:
            print("Zeroeth approximation:\n",
                  f"\tx: {x_vals[-1]:.2f}, y: {y_vals[-1]:.2f}\n\n")
            print("First iteration of Jacobian and its inverse:\n",
                  f"\tJacobian: {Jf_x:.2f}, Inv Jacobian: {inv_Jf:.2f}")
        
        x_vals.append(x_vals[-1] - invJf@(y_vals[-1] - des_y))
        y_vals.append(self.f(x_vals[-1]))
        
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
