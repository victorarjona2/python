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
    
    TODO: This description requires some revisiting...
    Explanation of variables:
        f   - An function whos input is n-dimensional and output is
                m-dimensional.
        Jf  - Essentially, the Jacobian of the function, "f"; basically, the
                derivative with respect to "z". Read more here:
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
        dict_init = {"x": [],
                    "f_x": [],
                    "dx": [],
                    "df_x":[],
                    "Jf_x":[]}
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
    def _Iterate(self):
        len_iter_df = len(self.iter_df.index)
        row_iter = []
        if self.debug:
            print(f"\nIteration number {len_iter_df}!")
        if len_iter_df == 0:
            nu_row = [self.x_start, self.Function(self.x_start), np.NAN,
                      np.NAN, self.Jacobian_Function(self.x_start)]
            
        elif len_iter_df >= 1:
            # Prep variables for use.
            pre_row = self.iter_df.iloc[-1]
            pre_x = pre_row["x"]
            pre_f_x = pre_row["f_x"]
            pre_dx = pre_row["dx"]
            pre_df_x = pre_row["df_x"]
            pre_Jf_x = pre_row["Jf_x"]
            try:
                pre_inv_Jf_x = np.linalg.inv(pre_Jf_x)
            except:
                pre_inv_Jf_x = 1/pre_Jf_x
            
            # Generate new values for new row.
            try:
                nu_x =  pre_x - pre_inv_Jf_x@(pre_f_x - self.des_y)
            except:
                nu_x =  pre_x - pre_inv_Jf_x*(pre_f_x - self.des_y)
                
            nu_f_x = self.Function(nu_x)
            nu_Jf_x = self.Jacobian_Function(nu_x)
            nu_dx = nu_x - pre_x
            nu_df_x = nu_f_x - pre_f_x
            
            # Make new row.
            nu_row = [nu_x, nu_f_x, nu_dx, nu_df_x, nu_Jf_x]

        nu_row = np.asarray(nu_row, dtype=object)
        if self.debug:
            print(nu_row)
        self.iter_df.loc[len_iter_df] = nu_row
        
    def Newton_Method(self, x_start = 0, des_y = 0, eps = np.finfo(float).eps,
                      debug = False):
        '''
        '''
        self.x_start = x_start
        self.des_y = des_y
        self.eps = eps
        self.debug = debug
        
        if self.debug:
            print("Newton Method starts NOW!", "Generating first row...",
                  sep = "\n")
        for ii in range(2):
            self._Iterate()

        while np.abs(self.iter_df.iloc[-1]["x"] - self.iter_df.iloc[-2]["x"]) > self.eps:
            self._Iterate()
        
        print(self.iter_df)
        
        # row_start = np.asarray([x_start, self.Function(x_start), np.NAN, np.NAN,
        #                         self.Jacobian_Function(x_start)])
        # self.iter_df.loc[len_iter_df] = row_start
        
def Demo_Funcs():
    def f(x):
        return x**2 + 7*x + 12
    
    def Jf(x):
        return 2*x + 7
    
    return [f, Jf]

if __name__ == "__main__":
    print("Starting demo!")
    [f, Jf] = Demo_Funcs()
        
    rooty = Roots()
    rooty.Define_Function(f)
    rooty.Define_Jacobian_Function(Jf)
    rooty.Newton_Method(eps = 0.0000001, x_start = -999)