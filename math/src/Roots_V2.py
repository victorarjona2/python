#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:23:55 2019

@author: victor
"""
# TODO: fix NM and SM to be part of class
#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
    
    Notes to users:
    For the time being, everything is defined manually until a proper way of
    initializing things is defined.
    Current procedure:
      1) Define Function
      2) Define Jacobian (derivative)
       2a) TODO: check if we're using proper terminology!
      3) Use Newton Method. Newton Method should default to Secant Method
       if no Jacobian is defined!
    """

    def __init__(self):
        pass
    
    # Define the class instance's function.
    def Define_Function(self, f):
        self.f = f
    
    # Define the class instance's Jacobian function.
    def Define_Jacobian_Function(self, Jf):
        self.Jf = Jf
    
    # Call a class instance's function to use.
    def Function(self, x):
        return self.f(x)
    
    # Call a class instance's Jacobian to use.
    def Jacobian_Function(self, x):
        return self.Jf(x)
    
    def _Define_Lists(self):
        x_vals = [self.x_start]
        y_vals = [self.f(x_vals[-1])]
        Jf_x_vals = [self.Jf(x_vals[-1])]
        
        # Figure out what the inverse of the jacobian is.
        if self.debug:
            print("Getting the inverse of the Jacobian!",
            "Figuring out if it is zero...")
        if np.abs(Jf_x_vals[-1]) > np.finfo(float).eps:
            if self.debug:
                print("The Absolute Value of the Jacobian is NOT zero!")
                try:
                    inv_Jf_x = np.linalg.pinv(Jf_x_vals[-1])
                except:
                    if self.debug:
                        print("I dunno, man... this ain't no matrix!",
                        "Treating as a floating number...",
                        sep = "\n")
                    inv_Jf_x = 1/Jf_x_vals[-1]
        else:
            if self.debug:
                print("The Jacobian IS zero! Beep boop bap, program ENDED!")
            exit()
            
        inv_Jf_x_vals = [inv_Jf_x]
            
        if self.debug:
            print(f"\nStarting x value: {x_vals[-1]:.2f}",
            f"Starting y value: {y_vals[-1]:.2f}",
            f"Starting Jf_x value: {Jf_x_vals[-1]:.2f}",
            f"Starting inv_Jf_x value: {inv_Jf_x_vals[-1]:.2f}",
            sep = "\n")
            
        return [x_vals, y_vals, Jf_x_vals, inv_Jf_x_vals]
            
    # Start iteration!
    def Newton_Method(self, x_start, des_y, eps, debug=True):
        '''
        '''
        self.x_start = x_start
        self.des_y = des_y
        self.eps = eps
        self.debug = debug
        
        if self.debug:
            print("Newton Method starts NOW!\n")
        
        # Define initial collection lists for...
        #   x value so far
        #   related y value list
        #   current Jacobian
        #   current inverse jacobian
        # ... and make it available to the instance.
        [x_vals, y_vals, Jf_x_vals, inv_Jf_x_vals] = self._Define_Lists()
        self.x_vals = x_vals
        self.x_vals = y_vals
        self.Jf_x_vals = Jf_x_vals
        self.inv_Jf_x_vals = inv_Jf_x_vals

if __name__ == "__main__":
    print("Starting demo!")
    def f(x):
        return x**2 + 7*x + 12
    
    def Jf(x):
        return 2*x + 7
        
    rooty = Roots()
    rooty.Define_Function(f)
    rooty.Define_Jacobian_Function(Jf)
    rooty.Newton_Method(0, 0, 0.0001)