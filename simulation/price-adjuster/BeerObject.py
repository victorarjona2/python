
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:10:48 2020

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import pandas as pd
import numpy as np
# IMPORTS ------------------------------------------------------------------- #

# THIS IS THE BASIC DEFINITION OF WHAT A BEER IS IN THIS SCRIPT. 
# A BEER IS COMPOSED OF ATTRIBUTES (INIT VARIABLES) AND PROCESSES (FUNCTIONS
# THAT DO THINGS WITH THE INIT VARIABLES). THIS ATTRIBUTES MUST BE DEFINED
# SINCE THE BEGINNING. A BEER HOLDS THE FOLLOWING:
# ============ Inputs ============
#   name:           A string of the name of the beer.
#   stable_point:   A reference to a stable point. Should be a float.
#   mini:           The least Peso/Dollar amount this beer will sell for.
#   maxi:           The most Peso/Dollar amount this beer will sell for.
#   p_func:         A function that turns the current point to a Peso/Dollar
#                   val.
# ========== Processes ==========

#class Beer():
#    def __init__(self,
#                 name,
#                 stable_point,
#                 mini,
#                 maxi,
#                 p_func=DefaultFunction)
#        # INIT VARS:
#        #   NAME
#        #   STABLE POINT (p-vals)
#        #   LOWEST f-val
#        #   HIGHEST f-val
#        #   CURRENT p-val (INITIALIZED AT STABLE POINT)
#        self.name = name
#        self.mini = mini
#        self.maxi = maxi
#        self.pnt_lst = [stable_point]
#        self.sale_lst = []

# THIS FUNCTION TAKES IN A CSV FILE NAME AND GENERATES A DICTIONARY OF BEER
# OBJECTS.


# def CreateBeersDF(data_loc):
#     # WE'RE EXPECTING A CSV FILE WHERE EACH ROW HAS INFORMATION ABOUT
#     #   SOME BEER. HERE ARE THE COLUMNS:
#     #   NAME  STABLE PT  MIN    MAX
#     #     |       |       |      |
#     #     |       |       |      +-------> MAX VALUE OF BEER
#     #     |       |       +--------------> MIN VALUE OF BEER
#     #     |       +----------------------> PT TO ALWAYS HEAD TO
#     #     +------------------------------> NAME OF THE BEER
#     beer_data = pd.read_csv(data_loc, index_col=False)
#     beers = {}
#     for nm in beer_data.NAME:
#         stb_pt = beer_data.loc[beer_data.NAME == nm, "STABLE_POINT"]
#         mini = beer_data.loc[beer_data.NAME == nm, "MIN"]
#         maxi = beer_data.loc[beer_data.NAME == nm, "MAX"]
#         beers[nm] = Beer(nm, stb_pt, mini, maxi)
#     return beers


# THIS FUNCTION TAKES IN A CSV FILE NAME AND GENERATES A DATAFRAME OF BEER
# OBJECTS.


def CreateBeersDF2(data_loc):
    # WE'RE EXPECTING A CSV FILE WHERE EACH ROW HAS INFORMATION ABOUT
    #   SOME BEER. HERE ARE THE COLUMNS:
    #   NAME  STABLE PT  MIN    MAX
    #     |       |       |      |
    #     |       |       |      +-------> MAX VALUE OF BEER
    #     |       |       +--------------> MIN VALUE OF BEER
    #     |       +----------------------> PT TO ALWAYS HEAD TO
    #     +------------------------------> NAME OF THE BEER
    return pd.read_csv(data_loc, index_col=False)