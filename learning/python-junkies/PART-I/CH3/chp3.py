#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:56:06 2020

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
from math import sqrt
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION


DESCRIPTION
'''
# HELPER FUNCTIONS ---------------------------------------------------------- #
def BabylonianAlgorithmLst(des_sqrt, guess, sig_figs):
    approxs = [guess]
    approxs.append((guess + des_sqrt/guess)/2.0)
    while abs(approxs[-2] - approxs[-1]) > 10**(-sig_figs):
        approxs.append((approxs[-1] + des_sqrt/approxs[-1])/2.0)
    return
    
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:53:29 2018

@author: victor
"""

#   