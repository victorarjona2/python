#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:23:55 2019

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import numpy as np
import matplotlib.pyplot as plt
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION

HELPER FUNCTIONS
    XInputs

AS THE NAME SUGGESTS, THE POINT OF THIS SCRIPT IS TO FIND THE AREA UNDER THE
CURVE OF A FUNCTION. THE ENTIRE FILE IS DIVIDED INTO HELPER FUNCTIONS AND THE
CONTENT OF THE SCRIPT.

HELPER FUNCTIONS:
    XInputs - TAKES IN THE EDGES OF THE INTERVAL (x_lo, x_hi), THE NUMBER OF
    RECTANGLES THAT WE WANT TO IMPOSE (no_rect), AND THE TYPE OF REIMANN
    INTEGRAL THAT WE WANT TO USE (int_type, OPTIONAL, SET TO 'ms'). FOR THE
    int_type, WE HAVE A COUPLE OF OPTIONS:
        'ms' - MIDDLE SUM.
        'rs' - RIGHT SUM.
        'ls' - LEFT SUM.
        'ts' - TRAPEZOID SUM.
    RETURNS THE INPUT VALUES FOR OUR FUNCTION (f).
    EXAMPLE 1:
        WE WANT THE INPUT VALUES FOR THE MIDDLE SUM OF THE INTERVAL [0, 1] WITH
        2 RECTANGLES. THE FUNCTION WILL OUTPUT:
            [0.25, 0.75]
    EXAMPLE 2:
        WE WANT THE INPUT VALUES FOR THE TRAPEZOID SUM OF THE INTERVAL [0, 1]
        WITH 3 RECTANGLES. THE FUNCTION WILL OUTPUT:
            [0, 1/3, 2/3, 1]

    GetArea - TAKES IN THE LENGTH OF THE BASE OF THE RECTANGLE/TRAPEZOID
    (dx), THE HEIGHT OF THE EDGES (fx), AND THE TYPE OF REIMANN INTEGRAL WE
    WANT TO DO (int_type, ALSO OPTIONAL, SAME AS ABOVE).
    EXAMPLE 1:
        SUPPOSE WE WANT THE APPROXIMATED AREA UNDER A PARABOLA (f(x) = x^2)
        WITH 2 RECTANGLES FROM THE INTERVAL [0, 1]. THAT WOULD MEAN THAT OUR
        dx = 0.5. SAY THIS APPROXIMATION'S THE LEFT SUM. THEN OUR
        fx = [0, 0.25], REPRESENTATIVE OF THE HEIGHT ON THE LEFT-HAND EDGES OF
        OUR XInput VALUES. THE TOTAL APPROXIMATION WOULD THEN BE THE SUM OF
        EVERY ELEMENT OF fx MULTIPLIED BY dx, 0.125.
    EXAMPLE 2:
        ASSUME THE SAME SITUATION EXCEPT WE HAVE THE MIDDLE SUM. THEN OUR
        fx = [0.0625, 0.5625]. THE TOTAL APPROXIMATION WOULD THEN BE THE SUM
        OF EVERY ELEMENT OF fx MULTIPLIED BY dx, 0.3125.

MAIN FUNCTION:
    ReimannApprox - TAKES IN f (FUNCTION), x_lo AND x_hi (INTERVAL VALUES), tol
    (TOLERANCE FOR OUR APPROXIMATION, OPTIONAL, SET TO 0.0001), int_type
    (OPTIONAL, SET TO 'ms' BY DEFAULT), plot (SET TO False BY DEFAULT, WILL
    PLOT IF TRUE). APPROXIMATES THE AREA UNDER THE CURVE OF A FUNCTION.

TODO:
    1) FIX ts OPTION! THERE IS SOMETHING WRONG WITH THE FIRST TWO
    APPROXIMATIONS.
        ~DONE

    2) ADD A REIMANN SUM FUNCTION THAT DOES THE APPROXIMATION BY THE NUMBER OF
    RECTANGLES WE WANT.

    3) FIX DESCRIPTION.
        ~KIND OF DONE

    4) PRINT NUMBER OF RECTANGLES AND THEIR APPROXIMATION IN A "PRETTY" FORMAT.
        ~KIND OF DONE

DESCRIPTION
'''
# HELPER FUNCTIONS ---------------------------------------------------------- #


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


#def ReimannByRectangle(f, x_lo, x_hi, no_rect):


# HELPER FUNCTIONS ---------------------------------------------------------- #

# TABLE OF CONTENTS --------------------------------------------------------- #
#   1
#       1.1
#       1.2

# TABLE OF CONTENTS --------------------------------------------------------- #

# CONTENT ------------------------------------------------------------------- #
#   1
#       1.1


def ReimannApprox(f, x_lo, x_hi, tol=0.0001, int_type='ms', plot=False):
    # APPROXIMATIONS CONTAINER. THE FIRST ELEMENT IS ONE SQUARE... THE
    # SECOND IS TWO... IN OTHER WORDS:
    # INDEX         NO. RECT
    # 0             1
    # 1             2
    # .             .
    # .             .
    # .             .
    # N             N + 1
    int_approx = []
    # GENERATE FIRST TWO APPROXIMATIONS TO HAVE SOMETHING TO COMPARE TO
    print('GENERATING FIRST TWO APPROXIMATIONS NOW:\n\n')
    for ii in range(2):
        dx = (x_hi - x_lo)/float((ii + 1))
        fx = f(XInputs(x_lo, x_hi, ii + 1, int_type))
        approx = GetArea(dx, fx, int_type)
        print(str(ii + 1) + " ---> " + str(approx) + '\n')
        int_approx.append(approx)
    # GENERATE THE Nth APPROXIMATION
    no_rects = 3
    print('GENERATING THE REST OF THE APPROXIMATIONS NOW:\n\n')
    while (np.abs((int_approx[-1] - int_approx[-2])) > tol):
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
