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

THE Turtle_Walk PROGRAM TAKES IN THE FOLLOWING PARAMETERS:
    n - THIS IS AN INTEGER AND IT'S THE VALUE THAT GENERATES A THUE-MORSE
        SEQUENCE OF SIZE 2^n USING THE HELPER FUNCTION Thue_Morse_Seq.

    delta_theta_deg - THIS PARAMETER'S DEFAULT IS AT 60 DEGREES, WHERE A KOCH
        CURVE IS GENERATED. DIFFERENT DEGREES GENERATES DIFFERENT CURVES!

    koch_dev - TBD. THIS IS A BOOLEAN VALUE. IF TRUE, THEN THE PROGRAM PROMPTS
        YOU TO GIVE A MAX DEVIATION. THE INTENT IS TO THROW IN SOME RANDOM
        BEHAVIOR TO SEE HOW THE CURVE WILL LOOK LIKE.

https://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence

DESCRIPTION
'''
# HELPER FUNCTIONS ---------------------------------------------------------- #


def Thue_Morse_Seq(n):
    tm_array = [0]
    for ii in range(1, n):
        nu = [(1 + tm) % 2 for tm in tm_array]
        tm_array = tm_array + nu
    return tm_array


def Step_Forward(v, theta):
    for_stp = np.array([[1], [0]])
    M = np.matrix([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    nu = M@for_stp + v
    return nu.item(0), nu.item(1)

# HELPER FUNCTIONS ---------------------------------------------------------- #

# TABLE OF CONTENTS --------------------------------------------------------- #
#   1
#       1.1

# TABLE OF CONTENTS --------------------------------------------------------- #

# CONTENT ------------------------------------------------------------------- #
#   1
#       1.1


def Turtle_Walk(n, delta_theta_deg=60, koch_dev=False):
    # GENERATE SEQUENCE.
    seq = Thue_Morse_Seq(n)
    print('Thue-Morse sequence generated... it is {} long.\n'.format(len(seq)))
    # STARTING POSITION
    x_vals = [0]
    y_vals = [0]
    print('Starting position is at (0, 0)...\n')
    # ANGLE THAT WE'RE CURRENTLY POINTING AT. NUMPY'S TRIG FUNCTIONS ONLY TAKE
    # RADIANS, SO WE'LL USE theta_deg FOR THIS.
    theta_deg = 0
    theta_rad = 0
    for ss in seq:
        if ss == 0:
            theta_deg = (theta_deg + delta_theta_deg) % 360
            theta_rad = theta_deg*(np.pi)/180
        else:
            pos_v = np.array([[x_vals[-1]], [y_vals[-1]]])
            nu_x, nu_y = Step_Forward(pos_v, theta_rad)
            x_vals.append(nu_x), y_vals.append(nu_y)
    plt.plot(x_vals, y_vals)
    return np.array([x_vals, y_vals])
# CONTENT ------------------------------------------------------------------- #
    