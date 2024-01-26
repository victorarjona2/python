#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:23:55 2019

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import numpy as np
import pandas as pd
import sys
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION

InsertioSort() IS A SORTING ALGORITHM THAT TAKES IN:
    someLst:    Literally, some one-dimensional list of values. For
                now, those values are all numeridal.
                TODO: Accept lists with other types of values. Might
                have to make up some metrics...!

DESCRIPTION
'''
# HELPER FUNCTIONS ---------------------------------------------------------- #
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


def InsertionSort(some_lst, bak_n_forth=False):
    cpy_lst = some_lst.copy()
    # It's always useful to know the size of the list.
    sz_lst = len(cpy_lst)
    # If the size of the list is less than 2, then why bother? We're done.
    if sz_lst < 2:
        sys.exit('Bruh, the list is literally already sorted.')
    # We need a boolean that says whether our list is sorted or not. While it
    # is NOT sorted (FALSE) then continue with the algorithm. For now, we
    # assume the list is NOT sorted!
    up_to = sz_lst
    dn_to = 0
    chk_srt = False
    # 1     - While we are NOT sorted...
    while not chk_srt:
        # 1.1   - For every index, save the last one, of the list...
        cntr = 0
        for ii in range(dn_to, up_to - 1):
            # 1.1.1     - If the (ii)th element is greater than the (ii + 1)th
            # element, then switch 'em!
            if cpy_lst[ii] > cpy_lst[ii + 1]:
                ii_hold = cpy_lst[ii + 1]
                cpy_lst[ii + 1] = cpy_lst[ii]
                cpy_lst[ii] = ii_hold
                cntr += 1
        up_to -= 1
        if bak_n_forth:
            for ii in range(up_to, dn_to, -1):
                if cpy_lst[ii] < cpy_lst[ii - 1]:
                    ii_hold = cpy_lst[ii - 1]
                    cpy_lst[ii - 1] = cpy_lst[ii]
                    cpy_lst[ii] = ii_hold
                    cntr += 1
            dn_to += 1
        if cntr == 0:
            chk_srt = True
    return cpy_lst


#def TestInsertionSort(kk):