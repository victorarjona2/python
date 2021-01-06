#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:00:15 2020

@author: victor
"""

import numpy as np

# A PERSON HAS AN AMT OF TIME PER BEER, AMT OF TIME THIS PERSON WILL STAY, AND
# FAVORITE BEER.
class Person1():
    def __init__(self,
                 money_in_wallet,
                 avg_tm_per_beer,
                 stdev_tm_per_beer,
                 fav_beer):
        # STARTING CAPITAL
        self.capital = money_in_wallet
        # FAVORITE BEER
        self.fav_beer = fav_beer
        # PERSON STARTS OUT NOT DRINKING
        self.is_drinking = False
        # TIME IN MINUTES BY BEER
        self.tm_per_beer = np.random.normal(avg_tm_per_beer,
                                            stdev_tm_per_beer)
    
    # EXECUTING Drinking IMPLIES Person HAS A DRINK.
    def Drinking(self):
        self.is_drinking = True
    
    # EXECUTING Done_Drinking IMPLIES Person NO LONGER HAS A DRINK.
    def Done_Drinking(self):
        self.is_drinking = False
        
    def BuyBeer(self, ):
        if self.capital > 0
        if self.is_drinking == False:
            self.money_atm