# TODO: RE-ORGANIZE THIS SCRIPT TO FIT THE SET FORMAT! MAKE AN EFFORT TO USE
# PANDA'S DATAFRAMES!

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# FIRST, OPEN THE CSV FILE. FOR THAT YOU NEED THE UNICODECSV LIBRARY!
import csv
import matplotlib.pyplot as plt
import numpy as np

# DOCUMENTATION ON THE IMPORTS ARE AS FOLLOWS:
# unicodecsv:
#    https://pypi.org/project/unicodecsv/
#
# maplotlib.pyplot:
#    https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

# numpy:
#    https://docs.scipy.org/doc/

"""
Created on Tue Aug 14 23:24:39 2018

@author: victor
"""

'''
THIS IS THE START OF A MULTILINE COMMENT.

DESC:
    THIS SCRIPT WILL TAKE IN A CSV FILE, FOUND IN :
        GITHUB/CODE/DATA/IRIS.CSV
    IN VICTOR'S COMPUTER.

    THE IRIS CSV FILE IS COMPOSED OF 5 COLUMNS. THE ROWS REPRESENT INDIVIDUAL
    SAMPLINGS. THE COLUMNS ARE:
        sepal_length   sepal_width   petal_length   petal_width   species

THIS IS THE END OF A MULTILINE COMMENT.
'''

# THE IRIS CSV FILE WILL BE OPENED AS 'f'. IT WILL BE STORED AS A LIST OF
# collection.OrderedDict OBJECT. GO TO THE FOLLOWING PAGE TO READ MORE
# ABOUT IT:
#
# https://docs.python.org/3/library/collections.html

# FIRST, OPEN THE FILE. IT IS TWO FOLDERS UP FROM WHERE THIS FILE IS, INTO
# THE 'DATA' FOLDER. OPEN THE 'iris.csv' FILE.
with open('../../DATA/iris.csv', 'rb') as f:
    # OPEN IT AND READ IT IN. THEN, MAKE IT INTO A LIST.
    reader = csv.DictReader(f)
    data = list(reader)
# PRINT OUT THE FIRST 10 ELEMENTS OF OUR 'data' LIST.
# data[:10]

# IT'S ALWAYS USEFUL TO NOW THE LENGTH OF YOUR DATA!
lenData = len(data)

# STORE ALL THE KEYS OF ANY ELEMENT OF OUR LIST, 'data'.
keys = list(data[0].keys())

# PRINT THE 'key'. CHECK OUT WHAT IT IS. UNCOMMENT TO SEE.
# print(keys)

# EVERYTHING'S A STRING IN 'data'. TURN THE STRINGS THAT ARE ONLY NUMBERS
# INTO FLOATS!
# FOR EACH DATA POINT 'dtPnt' IN OUR LIST, 'data'...
for dtPnt in data:

    # FOR EACH 'kk' IN OUR LIST OF 'keys'...
    for kk in keys:

        # SO LONG AS THE KEY IS NOT 'species'...
        if kk != keys[-1]:

            # TURN THAT VALUE INTO A FLOAT!
            dtPnt[kk] = float(dtPnt[kk])

# data[x][y] IS NOW A 2-D ARRAY WHERE...
#   x IS A: INTEGER NUMBER THAT REPRESENTS THE ROW...
#   y IS A: STRING, IN THIS CASE, 'sepal_length', 'sepal_width', ETC ETC...
# HERE'S AN EXAMPLE, THOUGH YOU'LL NEED TO TAKE OUT THE COMMENTS:

# testStr = 'The length of the sepal of this particular specimen is {}'
# testPnt = data[0]['sepal_length']
# print(testStr.format(testPnt))

# MAKE A DICTIONARY! EACH COLUMN NAME WILL BE A KEY, AND IT'S VALUE WILL BE
# A LIST COMPOSED OF IT'S RESPECTIVE ROWS.
#   "sepal_length" : [ 2, 7, 2, 1, 8, ... ]
#   "sepal_width"  : [ 4, 9, 1, 4, 9, ... ]
#   ...
# ESSENTIALLY, OUR NEW DICTIONARY WILL BE THE TRANSPOSE OF 'data'. HOWEVER,
# 'data' IS A SPECIAL KIND OF DATA DRAME! CHECK IT OUT. UNCOMMENT TO SEE.
# print(type(data[0]))

# MAKE A DICTIONARY FIRST.
data2 = {}

# THERE'S NOTHING IN THIS DICTIONARY YET! UNCOMMENT TO SEE.
# print(data2)

# FOR EVERY 'kk' KEY IN 'keys'...
for kk in keys:

    # WHAT ARE WE LOOKING AT?
    print(kk)

    # THAT KEY WILL HOLD A LIST IN OUR NEW DICTIONARY, 'data2'...
    data2[kk] = []

    # AND FOR ALL OF THE ELEMENTS IN THE CSV FILE THAT ARE IN THE COLUMN OF
    # THAT KEY...
    for xx in range(lenData):

        # TAKE THAT VALUE AND STORE IT IN A VARIABLE...
        dtPnt = data[xx][kk]
        data2[kk].append(dtPnt)

# LET'S MAKE 4 PLOTS IN THE SAME FIGURE.
# FIRST PLOT IN OUR FIGURE WILL BE A HISTOGRAM OF ALL THE LENGTHS.
# SECOND PLOT WILL BE OF SETOSA.
# THIRD WILL BE OF VERSICOLOR.
# FOURTH WILL BE OF VIRGINICA.

# GET THE DATA YOU CARE ABOUT!
# LIST COMPREHENSION'S AN AWESOME THING!

# GET ALL OF THE SEPAL LENGTHS.
allLen = data2['sepal_length'][:]

# GET ALL OF THE SEPAL LENGTHS THAT ARE OF THE SPECIES SETOSA.
setosaLen = [data[xx]['sepal_length'] for xx in range(lenData) if
             data[xx]['species'] == 'setosa']
# GET ALL THE SEPAL LENGTHS THAT ARE OF THE SPECIES VERSICOLOR.
versicolorLen = [data[xx]['sepal_length'] for xx in range(lenData) if
                 data[xx]['species'] == 'versicolor']

# GET ALL THE SEPAL LENGTHS THAT ARE OF THE SPECIES VIRGINICA.
# Get ALL the sepal lengths that are of the species Virginica.
virginicaLen = [data[xx]['sepal_length'] for xx in range(lenData) if
                data[xx]['species'] == 'virginica']

# MAKE TWO LISTS. WE'LL NEED THEM LATER TO GENERATEA PRETTY HISTOGRAM.
colors = ['purple', 'orange', 'green']
labels = list(set(data2['species']))

# CLEAR CURRENT FIGURE, IF THERE IS ONE.
plt.clf()

# MAKE FIGURE FONT BIGGER. UNCOMMENT IF YOU WANT.
# plt.rcParams.update({'font.size': 19})

# INVOKE A FIGURE THAT CONTAINS THE AXES AND MAKE IT NICE AND LONG.
plt.figure(figsize=(15, 5))

# GENREATE A SUBPLOT AND MANAGE THE FRIST ELEMENT OF A 1X2 SUBPLOT.
plt.subplot(1, 2, 1)

# MAKE A LIST OF THE LISTS OF SEPAL LENGTHS.
histThis = [setosaLen, versicolorLen, virginicaLen]

# IN SUBPLOI 1, MAKE A HISTOGRAM OF 'histThis', STACKED. GIVE IT AN
# X- AND Y- LABEL!
#
#            + THIS IS A LIST OF WHAT WE WANT TO PLOT.
#            |         + THIS MAKES THIS A STACKED TYPE OF HISTOGRAM.
#            |         |                     + THIS IS THE LIST OF COLORS.
#            |         |                     |            + LIST OF LABELS.
#            |         |                     |            |
#            V         V                     V            V
#        --------  ---------------------  ------------  ------------
plt.hist(histThis, histtype='barstacked', color=colors, label=labels)

# GENERATE AN X- AND Y- LABEL.
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')

# ADD A SUBPLOT TITLE.
plt.title('Stacked Histogram')

# ADD OUR LABELS. THEY CAN BE INVOKED LIKE THIS. IT PICKS UP ON THE LABELS
# YOU PREVIOUSLY ADDED IN plt.hist().
plt.legend()

# MANAGE THE SECOND ELEMENT IN THE SUBPLOT.
plt.subplot(1, 2, 2)

# MAKE ALL LENGTHS LIST INTO A HISTOGRAM. DON'T FORGET THE LABELS!
plt.hist(allLen, label='All species')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')

# ADD A LEGEND.
plt.legend()

# GIVE IT A TITLE.
plt.title('All lengths')

# GIVE THE ENTIRE FIGURE A TITLE.
plt.suptitle('Sepal Length Histograms')

# MAKE ANOTHER SUBPLOT FIGURE. MAKE IT 1X3, MAKING A HUSTOGRAM OF EACH
# SPECIES INDEPENDENTLY. DO THEY LOOK THE SAME AS THE STACKED HISTOGRAM?
plt.figure(figsize=(17, 5))
for ii in range(1, 4):
    plt.subplot(1, 3, ii)
    indx = int(ii - 1)
    plt.hist(histThis[indx], color=colors[indx], label=labels[indx])
    plt.xlabel('Sepal Length: {}'.format(labels[indx]))
    plt.ylabel('FrequencY')

# GIVE THE ENTIRE FIGURE A TITLE.
plt.suptitle('Sepal Lengths')

# NOW, MAKE A SCATTER PLOT OUR (X, Y) POINTS BEING 'sepal_length'
# AND 'sepal_width'.
plt.figure()
plt.grid(which='both')
plt.scatter(data2['sepal_length'], data2['sepal_width'])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

# MAKE ANOTHER SCATTER PLOT JUST LIKE THE PREVIOUS ONE, BUT THIS TIME
# THE COLOR DEPENDS ON THE SPECIES.
# FIRST, COLLECT THE DATA THAT YOU WANT TO SCATTER.
virLW = {'Length': [], 'Width': []}
setLW = {'Length': [], 'Width': []}
verLW = {'Length': [], 'Width': []}

for row in data:
    if row['species'] == labels[0]:
        setLW['Length'].append(row['sepal_length'])
        setLW['Width'].append(row['sepal_width'])
    elif row['species'] == labels[1]:
        virLW['Length'].append(row['sepal_length'])
        virLW['Width'].append(row['sepal_width'])
    elif row['species'] == labels[2]:
        verLW['Length'].append(row['sepal_length'])
        verLW['Width'].append(row['sepal_width'])

fig = plt.figure(figsize=(7, 7))
ax1 = fig.add_subplot(1, 1, 1)
ax1.scatter(virLW['Length'], virLW['Width'], c='r', label=labels[0])
ax1.scatter(setLW['Length'], setLW['Width'], c='b', label=labels[1])
ax1.scatter(verLW['Length'], verLW['Width'], c='g', label=labels[2])
plt.grid()
ax1.legend()
