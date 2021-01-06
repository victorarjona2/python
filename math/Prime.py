#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:50:27 2018

@author: victor
"""
import numpy as np
import matplotlib.pyplot as plt

'''
DESCRIPTION

PrimeGen TAKES IN A POSITIVE NUMBER, n, AND GENERATES ALL THE PRIMES BETWEEN 1
AND n, INCLUDING n, AND CHECKS IF IT IS A PRIME USING PrimeCheck1. PrimeGen2
DOES THE SAME BUT WITH PrimeCheck2.

PrimeCheck1 TAKES IN A REAL NUMBER, someN, AND CHECKS IF IT IS A PRIME BY BRUTE
FORCE. PrimeCheck2 DOES THE SAME BUT UP TO THE SQUARE ROOT OF someN. HERE'S
THE PROOF:

https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-
square-root-of-a-prime-number-to-determine-if-it-is-pr

PARAMETERS FOR...

PrimeCheck
    someN - LITERALLY SOME INTEGER. IT TAKES ANY INTEGER AND CHECKS WHETHER
    IT IS A PRIME OR NOT. SINCE WE ALREADY CHECK IF SAID NUMBER'S BIGGER THAN 1

    opt_p_check - THIS IS A BOOLEAN. IF IT'S TRUE, OR NOT IN AT ALL, THEN IT'LL
    USE THE OPTIMIZED METHOD. OTHERWISE, IT USES THE REGULAR METHOD.

PrimeGen
    n - THIS NUMBER IS OUR UP-TO VALUE TO CHECK FOR PRIMES.

    opt_p_check - THIS IS A BOOLEAN INPUT. TRUE BY DEFAULT, IT'LL USE
    PrimeCheck2. ELSE, IT'LL USE PrimeCheck1.

PrimePlot
    SAME AS PrimeGen

DESCRIPTION
'''

# HELPER FUNCTIONS


def PrimeCheck(someN, opt_p_check=True):
    if opt_p_check:
        up_to = int(np.sqrt(someN)) + 1
    else:
        up_to = someN
    for kk in range(2, up_to):
        if someN % kk == 0:
            return False
    return True


# HELPER FUNCTIONS

# TABLE OF CONTENTS --------------------------------------------------------- #
#   1
#       1.1
#       1.2

# TABLE OF CONTENTS --------------------------------------------------------- #

# CONTENT ------------------------------------------------------------------- #
#   1
#       1.1

# CONTENT ------------------------------------------------------------------- #


def PrimeGen(n, opt_p_check=True):
    if n < 2:
        strg = 'Prime numbers are natural numbers greater than 1.'
        print(strg)
        return 0
    if n == 2:
        return [2]
    primeLst = [2]
    for ii in range(3, n + 1, 2):
        if PrimeCheck(ii, opt_p_check):
            primeLst.append(ii)
    return primeLst


def PrimePlot(n, opt_p_check=True, rtrn_bool=False):
    primeLst = PrimeGen(n, opt_p_check)
#                        +--> FROM THE VALUE 1...
#                        |           +--> TO SIZE OF LIST...
#                       _|_ _________|________
    nthPrime = np.arange(1, len(primeLst) + 1)
    plt.plot(nthPrime, primeLst)
    plt.grid()
    plt.ylabel('Prime')
    plt.xlabel('Index of prime')
    plt.title('Prime plot')
    if rtrn_bool:
        return primeLst
