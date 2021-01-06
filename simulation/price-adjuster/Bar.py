#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:31:14 2020

@author: sysadmin
"""
# IMPORTS ------------------------------------------------------------------- #
BeerObject = importlib.import_module('BeerObject')
PersonObject = importlib.import_module('PersonObject')
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION
THIS SIMULATION IS A VERY SIMPLE ONE.
    FIRST, THE BAR HAS TO DEFINE ALL BEERS AVAILABLE, INCLUDING THE AMT FOR
    EACH. FOR A SIMPLE SIMULATION, THIS QTY CAN BE INFINITE.
    EACH BEER WILL HAVE AN ASSOCIATED STABLE POINT, MIN, MAX, AND NAME.

    EVERYONE THAT IS GENERATED WILL HAVE, UNLESS DEFINED, RANDOMLY CHOSEN:
        CAPITAL
        FAVORITE BEER
        TIME TO FINISH BEER
    ONCE SOMEONE DOESN'T HAVE MONEY THEY STOP BUYING.

    EVERYONE THAT IS GENERATED STARTS OUT NOT DRINKING.
    EVERYONE COMING IN WILL ALWAYS HAVE A BEER.

    TRANSACTION WILL BE MADE BY THE BAR. ESSENTIALLY, THE BAR SCRIPT WILL BE
    THE API BETWEEN THE PEOPLE AND THE BEERS AVAILABLE, TAKING IN MONEY (AND
    ACCOUNTING FOR IT), AND SUBTRACTING CAPITAL.

    THINGS TO CONSIDER FOR THE FUTURE:
        SORTED LIST OF FAV BEERS
        LIMITED SUPPLY OF BEER
        WAITERS (OR MORE LIKE BOTTLENECKS)
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
all_beers = 