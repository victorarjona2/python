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
        """
        """
        dict_init = {"x": [],   # Approximations to x
                    "f_x": [],  # Outpus of approximation to x
                    "dx": [],   # Differential between approximations of x
                    "df_x":[],  # Differential between approximations of f(x)
                    "Jf_x":[]}  # Jacobian/Derivative (if available) of f(x)
        self.iter_df = pd.DataFrame(dict_init)
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
    
    # Iteration function
    def Iterate(self):
        len_iter_df = len(self.iter_df.index)
        if self.debug:
            print(f"\nIteration number {len_iter_df}!")
        
        # If this is the first iteration, then populate values for first row!
        if len_iter_df == 0:
            nu_row = [self.x_start,                         # First guess
                      self.Function(self.x_start),          # First output
                      np.NAN,                               # Change fox xs
                      np.NAN,                               # Change for ys
                      self.Jacobian_Function(self.x_start)] # Actual Jacobian
        
        # If this is the first or later iteration, then...
        elif len_iter_df >= 1:
            # Prep variables for use...
            pre_row = self.iter_df.iloc[-1]
            pre_x = pre_row["x"]
            pre_f_x = pre_row["f_x"]
            pre_Jf_x = pre_row["Jf_x"]
            
            # Generate new values for new row...
            try:
                pre_inv_Jf_x = np.linalg.inv(pre_Jf_x)
                nu_x =  pre_x - pre_inv_Jf_x@(pre_f_x - self.des_y)
            except:
                pre_inv_Jf_x = 1/pre_Jf_x
                nu_x =  pre_x - pre_inv_Jf_x*(pre_f_x - self.des_y)
            nu_f_x = self.Function(nu_x)
            nu_Jf_x = self.Jacobian_Function(nu_x)
            nu_dx = nu_x - pre_x
            nu_df_x = nu_f_x - pre_f_x
            
            # Make new row...
            nu_row = [nu_x, nu_f_x, nu_dx, nu_df_x, nu_Jf_x]

        # nu_row = np.asarray(nu_row, dtype=object)
        if self.debug:
            print(nu_row)
        
        # Add row to DataFrame.
        self.iter_df.loc[len_iter_df] = nu_row
        
    def Newton_Method(self,
                      x_start = 0,
                      des_y = 0,
                      eps = np.finfo(float).eps,
                      debug = False):
        '''
        '''
        self.x_start = x_start
        self.des_y = des_y
        self.eps = eps
        self.debug = debug
        
        if self.debug:
            print("Newton Method starts NOW!",
                  "Generating first row...",
                  sep = "\n")
        
        # Generate the first two approximations. Need at least two to have
        # differentials available.
        for ii in range(2):
            self.Iterate()
        
        curr_x = self.iter_df.iloc[-1]["x"]
        prev_x = self.iter_df.iloc[-2]["x"]
        while np.linalg.norm(curr_x - prev_x) > self.eps:
            self.Iterate()
            curr_x = self.iter_df.iloc[-1]["x"]
            prev_x = self.iter_df.iloc[-2]["x"]
        
        if self.debug:
            print(self.iter_df)
    
    def Secant_Method(self):
        pass
        
def Demo_Funcs():
    
    def f(x):
        return x**2 + 7*x + 12
    
    def Jf(x):
        return 2*x + 7
    
    return [f, Jf]

def Demo_Funcs2():
    def f(x):
        x0 = x[0]
        x1 = x[1]
        
        y0 = np.power(x1, x0**2 + 7*x0 + 12)
        y1 = x0 + x1
        
        return np.array([y0, y1])
    
    def Jf(x):
        x0 = x[0]
        x1 = x[1]
        
        a = np.power(x1, x0**2 + 7*x0 + 12)
        b = np.power(x1, x0**2 + 7*x0 + 11)
        
        row0_Jf_x0_x1 = [(2*x0 + 7)*a*np.log(x1), (x0**2 + 7*x0 + 12)*b]
        row1_Jf_x0_x1 = [1, 1]
        
        Jf_x = np.array([row0_Jf_x0_x1, row1_Jf_x0_x1])
        
        return Jf_x
    
    return [f, Jf]

if __name__ == "__main__":
    print("Starting quadratic demo!")
    [f, Jf] = Demo_Funcs()
    
    quad_rooty = Roots()
    quad_rooty.Define_Function(f)
    quad_rooty.Define_Jacobian_Function(Jf)
    quad_rooty.Newton_Method(eps = 0.0000001, 
                             x_start = -999)
    
    print("Starting non-linear system of equations demo 1!")
    non_linear_sys_eq_rooty = Roots()
    [f, Jf] = Demo_Funcs2()
    
    non_linear_sys_eq_rooty.Define_Function(f)
    non_linear_sys_eq_rooty.Define_Jacobian_Function(Jf)
    dest_y = np.array([1, 6])
    start_x = np.array([3.8, 1.9])
    non_linear_sys_eq_rooty.Newton_Method(x_start = start_x,
                                          des_y = dest_y,
                                          eps = 0.0000001)
    
    print("Starting non-linear system of equations demo 2!")
    non_linear_sys_eq_rooty2 = Roots()
    [f, Jf] = Demo_Funcs2()
    
    non_linear_sys_eq_rooty2.Define_Function(f)
    non_linear_sys_eq_rooty2.Define_Jacobian_Function(Jf)
    dest_y = np.array([1, 6])
    start_x = np.array([-10, 5])
    non_linear_sys_eq_rooty2.Newton_Method(x_start = start_x,
                                           des_y = dest_y,
                                           eps = 0.0000001)