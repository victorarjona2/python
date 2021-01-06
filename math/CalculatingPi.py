#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:23:55 2019

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import numpy as np
import sys
folder_loc = '~/Documents/GitHub/CODE/PYTHON/MATH/'
sys.path.insert(0, folder_loc)
from Prime import PrimeCheck
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION


DESCRIPTION
'''
# HELPER FUNCTIONS ---------------------------------------------------------- #


def Simplify(num1, num2):
    # GET THE SMALLEST OF THE TWO.
    smol = int(min([num1, num2]))

    nnum1, nnum2 = num1, num2

    for ii in range(2, smol + 1):
        while nnum1 % ii == 0 and nnum2 % ii == 0:
            nnum1, nnum2 = nnum1/ii, nnum2/ii

    return [nnum1, nnum2]


def DistanceLessThan1(npVec):
    return sum(npVec**2)
# HELPER FUNCTIONS ---------------------------------------------------------- #

# TABLE OF CONTENTS --------------------------------------------------------- #
#   1
#       1.1
#       1.2

# TABLE OF CONTENTS --------------------------------------------------------- #

# CONTENT ------------------------------------------------------------------- #
#   1
#       1.1


def ApproxPi(n, prime_bool=False):
    # IN THIS FUNCTION, "n" REPRESENTS THE NUMBER OF POINTS THAT WE'RE GOING TO
    # BE GENERATING. THE LIST OF "allPts" WILL CONTAIN ALL OF THE POINTS
    # GENERATED. THE CONTAINER OF "cirPts" WILL CONTAIN ALL OF THE POINTS THAT
    # ARE AT MOST LENGTH OF ONE.
    #   all_pts     :   ALL POINTS GENERATED RANDOMLY.
    #   cirPts      :   ALL POINTS THAT ARE AT MOST LENGTH OF 1 THAT ARE
    #                   GENERATED RANDOMLY.

    # CREATE POINTS
    if prime_bool:
        for ii in range(n, 1, -1):
            if PrimeCheck(ii):
                nth_p = ii
                break
        print('Generating a random list \n',
              'of {} points.\n'.format(nth_p))
        all_pts = np.random.random((nth_p, 2))
    else:
        print('Generating a random list \n',
              'of {} points.\n'.format(n))
        all_pts = np.random.random(n, 2)
    in_cir_bool = np.sum(all_pts**2, 1) <= 1
    len_in_cir = len(all_pts[in_cir_bool])
    print('{} points located inside the circle.'.format(len_in_cir))
    len_all_pts = len(all_pts[:, 1])
    if prime_bool:
        return 4.0*float(len_in_cir)/len_all_pts
    else:
        sol = Simplify(4.0*float(len_in_cir), (len_all_pts))
        return sol[0]/sol[1]


# CONTENT ------------------------------------------------------------------- #
