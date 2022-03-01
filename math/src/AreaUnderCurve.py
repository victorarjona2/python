#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:36:19 2022

@author: victorarjona
"""

import numpy as np
import matplotlib.pyplot as plt

def X_Values(xlo, xhi, num_seg, int_type):
    '''
    
    '''
    pass

def XInputs(x_lo, x_hi, no_rect, int_type='ms'):
    x_inp = np.linspace(x_lo, x_hi, no_rect + 1)
    if int_type == 'ms':
        return 0.5*(x_inp[:-1] + x_inp[1:])
    elif int_type == 'rs':
        return x_inp[1:]
    elif int_type == 'ls':
        return x_inp[0:-1]
    elif int_type == 'ts':
        return x_inp

def GetArea(dx, fx, int_type='ms'):
    if int_type == 'ts':
        area = []
        for ii in range(len(fx) - 1):
            f_lo = np.min(fx[ii:ii + 2])
            f_hi = np.max(fx[ii:ii + 2])
            area.append(f_lo + f_hi)
        return 0.5*dx*np.sum(area)
    else:
        return dx*np.sum(fx)

def ReimannApprox(f, x_lo, x_hi, tol=4, int_type='ms', plot=False):
    '''
    Description
        ReimannApprox makes an effort of approximating the integral (f) from
        some point (x_lo) to another  (x_hi). The integral approximates up to
        a tolerance (tol); this value defaults to 4 decimal points; if
        specifying tolerance then it must be given as an integer, else it will
        default back to 4 decimal points.
        
        There are many ways to approximate an integral (int_type). We can use
        the right-most ("rs"), the left-most ("ls"), or middle point ("ms") to
        generate a rectangle and add these together. A much better to do this
        is using the trapezoid rule ("ts"). Refer to the link below for an
        explanation of these different methods:
            https://www.khanacademy.org/math/ap-calculus-ab/ab-integration-new/ab-6-2/a/riemann-sums-review
        
        By default, there are no plots generated (plot). When invoked
        (plot=True), a graph of the approximation using 0 rectangles up to
        the number of rectangles needed to reach the tolerance is generated.
        
        In the end we get a list of the approximations of the integral
        (int_approx).
        
        Input variables:
            Required: 
                f:          The function used to calculate the integral, AKA, 
                            the integrand. It is assumed that the function is
                            continuous between the lower and upper limit.
                x_lo:       Lower limit.
                x_hi:       Upper limit.
            
            Optional:
                tol:        Tolerance defaults to 4 decimal points. Up to how
                            many decimal points should this approximation get
                            to? E.G., if tol=3 then the tolerance is 10**(-3)
                            (three decimal points).
                int_type:   By default, the trapezoid rule ("ts") is used.
                            Other options are right side ("rs"), left ("ls"),
                            and middle ("mid").
                plot:       Boolean. If true, a plot of the approximation is
                            generated.
        
        Output variables:
            int_approx:     List composed of the approximations. The last
                            element in the list is the approximation up to the
                            tolerance chosen.
    '''
    int_approx = []
    # Generate first two approximations, otherwise, we have nothing to compare
    # and, therefore, nothing to compare with our tolerance.
    print("Generating first two approximations...\n")
    for ii in range(2):
        dx = (x_hi - x_lo)/float((ii + 1))
        fx = f(XInputs(x_lo, x_hi, ii + 1, int_type))
        approx = GetArea(dx, fx, int_type)
        print(str(ii + 1) + " ---> " + str(approx) + '\n')
        int_approx.append(approx)
    # GENERATE THE Nth APPROXIMATION
    no_rects = 3
    print('GENERATING THE REST OF THE APPROXIMATIONS NOW:\n\n')
    while (np.abs((int_approx[-1] - int_approx[-2])) > 10**(-1*tol):
        dx = (x_hi - x_lo)/float((no_rects))
        fx = f(XInputs(x_lo, x_hi, no_rects, int_type))
        approx = GetArea(dx, fx, int_type)
        print(str(no_rects) + " ---> " + str(approx) + '\n')
        int_approx.append(approx)
        no_rects += 1
    no_rects -= 1
    # PLOT
    if plot:
        plt.plot(np.asarray([ii for ii in range(1, len(int_approx) + 1)]),
                 int_approx)
        plt.grid(1)
    return int_approx
# CONTENT ------------------------------------------------------------------- #
