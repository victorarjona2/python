#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 4.1 Matrices
A = np.matrix([[3, 0],
               [0, -2]])

B = np.matrix([[2, 0],
               [0, 3]])

C = np.matrix([[0, 2],
               [0, 0],
               [0, 0]])

D = np.matrix([[1, 1],
               [0, 0]])

E = np.matrix([[1, 1],
               [1, 1]])

F = np.matrix([[1, 2],
               [0, 2]])

a_u, a_s, a_vh = np.linalg.svd(A)
a = {'u': a_u,
     's': a_s,
     'vh': a_vh,
     'prob_letter' : 'a',
     'matrix': A}

b_u, b_s, b_vh = np.linalg.svd(B)
b = {'u': b_u,
     's': b_s,
     'vh': b_vh,
     'prob_letter' : 'b',
     'matrix': B}

c_u, c_s, c_vh = np.linalg.svd(C)
c = {'u': c_u,
     's': c_s,
     'vh': c_vh,
     'prob_letter' : 'c',
     'matrix': C}

d_u, d_s, d_vh = np.linalg.svd(D)
d = {'u': d_u,
     's': d_s,
     'vh': d_vh,
     'prob_letter' : 'd',
     'matrix': D}

e_u, e_s, e_vh = np.linalg.svd(E)
e = {'u': e_u,
     's': e_s,
     'vh': e_vh,
     'prob_letter' : 'e',
     'matrix': E}

f_u, f_s, f_vh = np.linalg.svd(F)
f = {'u': f_u,
     's': f_s,
     'vh': f_vh,
     'prob_letter' : 'f',
     'matrix': F}

all_svds_meta = [a, b, c, d, e, f]

for svd in all_svds_meta:
    print("The SVD for problem {}\n".format(svd['prob_letter']),
          "\tU:\n{}\n\n".format(svd['u']),
          "\tS:\n{}\n\n".format(svd['s']),
          "\tVh:\n{}\n\n".format(svd['vh']))

# unit circle vectors
rads = np.linspace(0, 2*np.pi, 100)
x = np.cos(rads)
y = np.sin(rads)
v = np.matrix([x, y])

fig, axs = plt.subplots(5, 2, figsize=(10, 30), constrained_layout=True)

all_svds_meta = [a, b, d, e, f]
for ii in range(5):
    svd_meta = all_svds_meta[ii]
    if svd_meta['prob_letter'] == 'c':
        continue

    x1, y1 = svd_meta['vh'][0, 0], svd_meta['vh'][1, 0]
    x2, y2 = svd_meta['vh'][0, 1], svd_meta['vh'][1, 1]
    axs[ii, 0].plot(x, y, 'r-')
    axs[ii, 0].arrow(0, 0, x1, y1, width=0.01)
    axs[ii, 0].arrow(0, 0, x2, y2, width=0.01)
    t = 'Unit circle & column vector in V for {}'.format(svd_meta['prob_letter'])
    axs[ii, 0].set_title(t)
    axs[ii, 0].grid()

    s1, s2 = svd_meta['s'][0], svd_meta['s'][1]
    a1, b1 = svd_meta['u'][0, 0], svd_meta['u'][1, 0]
    a2, b2 = svd_meta['u'][0, 1], svd_meta['u'][1, 1]

    # Transformed circle
    v = svd_meta['matrix']@np.matrix([x, y])

    axs[ii, 1].plot(v[0].T, v[1].T, 'g-')
    axs[ii, 1].arrow(0, 0, s1*a1, s1*b1, width=0.01)
    if s2 != 0:
        axs[ii, 1].arrow(0, 0, s2*a2, s2*b2, width=0.01)
    axs[ii, 1].set_title('Hyperellipse & column vectors in U for {}'.format(svd_meta['prob_letter']))
    axs[ii, 1].grid()