#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:23:55 2019

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION


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

data_f = pd.read_csv('../../DATA/iris.csv')

# LIST OF NAME OF COLUMNS
col_names = list(data_f.columns)
# LIST OF SPECIES
species = list(set(data_f.species))
# COLORS FOR PLOTTING
colors = ['purple', 'orange', 'green']
# HISTOGRAM
plt.hist([data_f.loc[data_f.species == species[0], 'sepal_length'],
          data_f.loc[data_f.species == species[1], 'sepal_length'],
          data_f.loc[data_f.species == species[2], 'sepal_length']],
         color=colors,
         histtype='barstacked',
         bins=20,
         label=species)
plt.legend()
