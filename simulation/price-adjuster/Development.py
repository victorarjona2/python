#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 03:37:20 2020

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import random
import numpy as np
import importlib
BeerObject = importlib.import_module('BeerObject')
PersonObject = importlib.import_module('PersonObject')
# IMPORTS ------------------------------------------------------------------- #

'''
THE ULTIMATE APPROACH ---------------------------------------------------------
BEER PRICE CHANGE SIMULATES A STOCK-MARKET-LIKE BEHAVIOR FOR THE PRICES OF
DRINKS: THE PRICE OF A DRINK DEPENDS ON THE VALUE/PURCHASES OF THE OTHER
DRINKS. WE'LL HAVE THE FOLLOWING:
    ENVIRONMENT-    THE ENVIRONMENT DICTATES:
                        HRS OF OPENING/CLOSING (TIME OF THE SIMULATION)
                        MAX NUMBER OF PEOPLE THAT CAN ENTER
                    MAYBE LATER:
                        ENVIRONMENT TIME-DENSITY BEHAVIOR
    PEOPLE-         RANDOMIZED PERSON OBJECT. TO START A SIMULATION WE NEED
                    EACH PERSON TO HAVE:
                        AMOUNT OF TIME OF STAY IN ENVIRONMENT
                        AVG TIME TO DRINK A BEER
    DRINK LIST-     THIS LIST CONTAINS THE NAMES OF THE BEERS THAT ARE
                    AVAILABLE.
-------------------------------------------------------------------------------

APPROACH 1: SUPER SIMPLE SIMULATION
    THERE WILL BE "n" PEOPLE.

    AFTER EACH DEFINED "dt" (TIME DELTA) EACH PERSON WILL HAVE A RANDOM CHOICE
    OF BEER FROM "beers" (USING "BeerObject.py").

    THE NUMBER OF SALES AFTER EACH "dt" WILL BE RECORDED FOR EACH BEER TYPE.

'''
# HELPER FUNCTIONS ---------------------------------------------------------- #
def DefaultFunction(mini, maxi, m, x_val):
    return mini + (maxi-mini)/(1+np.exp(m*x_val))
# HELPER FUNCTIONS ---------------------------------------------------------- #

def Approach1(n, dt = 1):
    # BEERS DATAFRAME - USED TO KEEP ALL GENERATED DATA IN A SINGLE LOCATION
    beers_df = BeerObject.CreateBeersDF2('test-data.csv')
    
    # NUMBER OF BEERS
    no_of_beers = len(beers_df.name)
    
    # GENERATE SALES LIST AND ADD IT AS A COLUMN TO THE DATA FRAME
    sales = [[] for ii in range(no_of_beers)]
    beers_df['sales_per_dt'] = sales
    
    # GENERATE CUSTOMERS
    # EACH CUSTOMER HAS AN AVG TIME THAT HE/SHE DRINKS BEER, A STDEV FOR THE
    # AVG TIME THAT HE/SHE DRINKS BEER, AND A FAVORITE BEER
    customers = [PersonObject.Person1(avg_tm_per_beer=20,
                                     stdev_tm_per_beer=2.5,
                                     fav_beer = random.choice(beers_df.name)) for ii in range(n)]
    
    # 