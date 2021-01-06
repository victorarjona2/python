#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 13:39:58 2019

CLEAN THIS FILE UP! IMPOSE THE FORMAT AND SIMPLIFY THE SCRIPT.

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import matplotlib.pyplot as plt
import pandas as pd
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION


DESCRIPTION
'''
# HELPER FUNCTIONS ---------------------------------------------------------- #


def TimeTransformation(tm):
    return float(tm.hour) + float(tm.minute)/60.0


def TimeTransformationList(tm_list):
    lst_to_rtrn = []
    tms = list(tm_list.tStamp)
    qtys = list(tm_list.qty)
    for idx in range(len(tms)):
        tm = TimeTransformation(tms[idx])
        for q in range(qtys[idx]):
            lst_to_rtrn.append(tm)
    return lst_to_rtrn


# HELPER FUNCTIONS ---------------------------------------------------------- #

# TABLE OF CONTENTS --------------------------------------------------------- #
#   1 TAKE IN CSV FILES THROUGH PANDAS
#   2 CLEAN data VARIABLE
#       2.1 TURN tStamp INTO A PANDAS TIME
#       2.2 GET RID OF EVERYTHING THAT HAPPENED BEFORE 06 OCT 2018
#       2.3 CLEAN UP bType
#   3 PREPARE TO HAVE THE INFORMATION READILY AVAILABLE TO START GRAPHS
#       3.1 MAKE A b_type_vals VARIABLE WITH ALL THE bType VALUES
#       3.2 MAKE A LISTb OF all_sales AS THE FREQUENCY OF SALES
#   4 GRAPHS AND HISTOGRAMS
#       4.1 allSales HISTOGRAM WITH LEGENDS (b_type_vals)
#       3.1 MAKE A bTypeVals VARIABLE WITH ALL THE bType VALUES
#       3.2 MAKE A LIST OF allSales AS THE FREQUENCY OF TOTAL SALES
#   4 GRAPHS AND HISTOGRAMS
#       4.1 allSales HISTOGRAM
#       4.2 all_sales STACKED HISTOGRAM BY TYPE
#       4.3 all_sales PIE CHART BY TYPE
# TABLE OF CONTENTS --------------------------------------------------------- #

# CONTENT ------------------------------------------------------------------- #
#   1 TAKE IN CSV FILES THROUGH PANDAS
fl = "../../../data/ArmorOktoberfest.csv"
data = pd.read_csv(fl, index_col=False)

#   2 CLEAN data VARIABLE
#       2.1 TURN tStamp INTO A PANDAS TIME
data.loc[:, 'tStamp'] = pd.to_datetime(data.tStamp)

#       2.2 GET RID OF EVERYTHING THAT HAPPENED BEFORE 06 OCT 2018
up_to_date = pd.to_datetime("2018/10/6 13:59:59")
mask = data.tStamp > up_to_date
data = data.loc[mask, :]

#       2.3 CLEAN UP "bType"
data.loc[data.bType == "Blonde", "bType"] = "Blonde 12oz"

#   3 PREPARE TO HAVE THE INFORMATION READILY AVAILABLE TO START GRAPHS
#       3.1 MAKE A bTypeVals VARIABLE WITH ALL THE bType VALUES
b_type_vals = list(set(data.bType))

#       3.2 MAKE A LIST OF all_sales AS THE FREQUENCY OF SALES
#       3.2 MAKE A LIST OF allSales AS THE FREQUENCY OF TOTAL SALES
#           THIS IS A LIST COMPOSED OF NUMBERS THAT REPRESENT TIME, EG,
#           14.1 WOULD BE 2:06PM. WE CAN MAKE A HISTOGRAM SHOWING THE FREQUENCY
#           OF PURCHASES.
all_sales = []
tStamp_n_qty = data.loc[:, ["tStamp", "qty"]]

for idx in range(len(tStamp_n_qty)):
    t = TimeTransformation(tStamp_n_qty.tStamp.iloc[idx])
    for ii in range(tStamp_n_qty.qty.iloc[idx]):
        all_sales.append(t)

len_all_sales = len(all_sales)

#       3.3 MAKE A DICTIONARY OF ALL SALES BY TYPE, sales_by_type
sales_by_type = {'blonde': data.loc[data.bType.str.contains("Blonde"),
                                    ['tStamp', 'qty']],
                 'chai': data.loc[data.bType.str.contains("Chai"),
                                  ['tStamp', 'qty']],
                 'stout': data.loc[data.bType.str.contains("Stout"),
                                   ['tStamp', 'qty']],
                 'kolsch': data.loc[data.bType.str.contains("Kolsch"),
                                    ['tStamp', 'qty']],
                 'ipa': data.loc[data.bType.str.contains("IPA"),
                                 ['tStamp', 'qty']],
                 'pale': data.loc[data.bType.str.contains("Pale"),
                                  ['tStamp', 'qty']]}
for tp in sales_by_type:
    sales_by_type[tp] = TimeTransformationList(sales_by_type[tp])

sales_by_type_values = list(sales_by_type.values())
sales_by_type_keys = list(sales_by_type.keys())
sales_by_type_sizes = [len(ss) for ss in sales_by_type.values()]

#   4 GRAPHS AND HISTOGRAMS
#       4.1 all_sales HISTOGRAM
output_dir = './06OCT2018ArmorOktoberfestOUT/'
str_4_1 = "Hubo un total de {} ventas en el transcurso de {} horas."
print(str_4_1.format(len_all_sales, 10))
print()

fig = plt.figure()
#           +-- LIST OF VALUES.
#           |
#           |           +-- THE NUMBER OF BINS THAT YOUR HISTOGRAM WILL MAKE.
#           |           |   THERE ARE 10 HOURS BETWEEN 2PM AND MIDNIGHT. AND
#           |           |   WE WANT 3MIN INTERVALS.
#           |           |
#           |           |       +-- STARTING AND ENDING FREQUENCY VALUES
#           v           v       v
#        ___|_____  ____|__  ___|__________
plt.hist(all_sales, bins=20, range=(14, 24))
plt.title("Frecuencia de ventas por intervalos de 30min")
plt.xlabel('Hora')
plt.ylabel("Frecuencia de venta")
plt.grid()
plt.xlim(13.75, 24.25)
plt.ylim(0, 26.5)
fig.savefig(output_dir + 'TotalSales30Min.pdf')

#       4.2 all_sales STACKED HISTOGRAM BY TYPE
for kk in sales_by_type:
    print("Hubo {} ventas de {}.".format(len(sales_by_type[kk]), kk))
print()

fig = plt.figure()
plt.hist(sales_by_type_values,
         bins=20, histtype='barstacked',
         range=(14, 24), label=sales_by_type_keys)
plt.title('Frecuencia de ventas por intervalos de 30min')
plt.ylabel('Frecuencia de venta por estilo')
plt.xlabel('Hora')
plt.grid()
plt.xlim(13.75, 24.25)
plt.ylim(0, 26.5)
plt.legend()
fig.savefig(output_dir + 'TotalSales30MinStacked.pdf')

#       4.3 all_sales PIE CHART BY TYPE
for kk in sales_by_type:
    prntg = "{0:.2f}".format(len(sales_by_type[kk])/len(all_sales)*100.0)
    print("El {}% de las ventas fueron de {}.".format(prntg, kk))
print()

fig = plt.figure()
plt.pie(sales_by_type_sizes,
        explode=[0.05*ii for ii in range(len(sales_by_type))],
        labels=[ss.capitalize() for ss in sales_by_type_keys],
        shadow=True,
        autopct='%1.1f%%')
plt.title('Porcentage vendido')
fig.savefig(output_dir + 'TotalSalesPieChart.pdf')

#       4.4 all_sales CUMULATIVE.
fig = plt.figure()
plt.hist(all_sales,
         bins=20,
         range=(14, 24),
         cumulative=True)
plt.title('Frecuencia cumulativa de todas las ventas')
plt.xlabel('Hora')
plt.ylabel('Frecuencia')
plt.grid()
fig.savefig(output_dir + 'TotalSalesCumulative.pdf')

#       4.5 CUMULATIVE BY TYPE.
fig = plt.figure()
plt.hist(sales_by_type_values,
         label=sales_by_type_keys,
         bins=20,
         range=(14, 24),
         cumulative=True)
plt.title('Frecuencia cumulativa de todas las ventas por tipo')
plt.xlabel('Hora')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid()
fig.savefig(output_dir + 'TotalSalesCumulativeByType.pdf')

#       4.6 all_sales CUMULATIVE BY TYPE STACKED
fig = plt.figure()
plt.hist(sales_by_type_values,
         label=sales_by_type_keys,
         bins=20,
         range=(14, 24),
         cumulative=True,
         stacked=True)
plt.title('Frecuencia cumulativa de todas las ventas encimado')
plt.xlabel('Hora')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid()
fig.savefig(output_dir + 'TotalSalesCumulativeStacked.pdf')
# CONTENT ------------------------------------------------------------------- #
