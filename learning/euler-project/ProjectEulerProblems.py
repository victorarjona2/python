#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:00:30 2020

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import numpy as np
import importlib
import sys

sys.path.append('../../math/')
Prime = importlib.import_module('Prime')

# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION


DESCRIPTION
'''
# HELPER FUNCTIONS ---------------------------------------------------------- #
# TAKES IN A STRING
def IsPalindrome(num):
    num = int(num)
    print(num)
    if num < 10:
        return True
    for ii in range(int(num/2)):
        kk = str(num)
        if kk[ii] != kk[-ii - 1]:
            return False
    return True
# HELPER FUNCTIONS ---------------------------------------------------------- #

# TABLE OF CONTENTS --------------------------------------------------------- #
#   1
#       1.1
#       1.2

# TABLE OF CONTENTS --------------------------------------------------------- #

# CONTENT ------------------------------------------------------------------- #
#   1
#       1.1

# CONTENT ------------------------------------------------------------------- #

# PROBLEM 1
def MultiplesOfThreeAndFive():
    somme = sum(list(set([val for val in range(1000) if val % 3 == 0 or val % 5 == 0])))
    print(somme)
    return(somme)

# PROBLEM 2
def EvenFibonacciNumbers():
    fib_prev, fib_curr = 1, 2
    fibs = [2]
    while fib_prev + fib_curr < 4*10**6:
        nu_fib = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = nu_fib
        if nu_fib % 2 == 0:
            fibs.append(nu_fib)
    somme = sum(fibs)
    print(somme)
    return(somme)

# PROBLEM 3
def LargestPrimeFactor():
    lrg_num = 600851475143
    if Prime.PrimeCheck(lrg_num):
        return lrg_num
    mid = int(np.sqrt(lrg_num))
    clf = 3
    sol = -1
    while clf < mid:
        if lrg_num % clf == 0:
            if Prime.PrimeCheck(clf):
                sol = clf
                chf = int(lrg_num/clf)
                if Prime.PrimeCheck(chf):
                    sol = chf
                    break
        clf += 2
    return sol

# PROBLEM 4
def LargestPalindrome():
    highest_palindrome_so_far = 0
    for row in range(100, 1000):
        for col in range(100, 1000):
            pal_bool = IsPalindrome(col*row)
            if pal_bool:
                if col*row > highest_palindrome_so_far:
                    highest_palindrome_so_far = col*row