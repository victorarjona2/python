#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:55:48 2021

@author: victor
"""
# IMPORTS ------------------------------------------------------------------- #
import numpy as np
import matplotlib.pyplot as plt
# IMPORTS ------------------------------------------------------------------- #
'''
DESCRIPTION


DESCRIPTION
'''
# 24.3
#   Arrays to collect values
l2_exp_tA = []
exp_t_max_A = []

#   Array of values between 0 to 20
t = np.linspace(0, 20)

for ii in range(10):
    # 10x10 matrix of normally distributed values minus 2 times the identity
    # matrix.
    A = np.random.normal(0, 1, (10, 10)) - 2*np.identity(10)

    lst_to_appnd_to_l2 = []
    lst_to_appnd_to_exp = []

    for t_val in t:
        # L-2 norm of exp(t*A) and exp(t*max(A))
        lst_to_appnd_to_exp.append(np.exp(t_val*np.max(A)))
        lst_to_appnd_to_l2.append(np.linalg.norm(np.exp(t_val*A)))

    l2_exp_tA.append(lst_to_appnd_to_l2)
    exp_t_max_A.append(lst_to_appnd_to_exp)

l2_exp_tA = np.array(l2_exp_tA)
exp_t_max_A = np.array(exp_t_max_A)
diff_l2_exp = [np.abs(l2_exp_tA[ii] - exp_t_max_A[ii]) for ii in range(len(l2_exp_tA))]

fig, axs = plt.subplots(1, 3, figsize=(11, 5))
axs = axs.flatten()

for ii in range(len(l2_exp_tA)):
    axs[0].semilogy(t, l2_exp_tA[ii])

for ii in range(len(l2_exp_tA)):
    axs[1].semilogy(t, exp_t_max_A[ii])

for ii in range(len(diff_l2_exp)):
    axs[2].semilogy(t, diff_l2_exp[ii])

axs[0].grid()
axs[0].set(xlabel="Values of $t$", ylabel=r"$\|\|{e^{tA}}\|\|_{2}$")

axs[1].grid()
axs[1].set(xlabel="Values of $t$", ylabel=r"$e^{t\alpha(A)}$")

axs[2].grid()
axs[2].set(xlabel="Values of $t$", ylabel=r"Difference between plots")

fig.tight_layout()


# Implement and test Householder Reduction to Hessenberg form.
def Householder2Hessenberg(B):
    # Get shape of Matrix and make sure it is square.
    shape = B.shape
    dim = B.ndim

    if dim != 2:
        raise TypeError("Not a 2 dimensional matrix!")

    m = shape[0]

    A = np.copy(B)
    for kk in range(m - 1):
        x = A[kk+1:m, kk]

        e_1 = np.zeros(shape=x.shape)
        e_1[0] = 1

        v_k = np.sign(x[0])*np.linalg.norm(x)*e_1 + x
        v_k /= np.linalg.norm(v_k)

        # Fix this section of code        
        A[kk + 1:m, kk:m] -= 2*np.matmul(v_k.reshape(len(v_k), 1), np.matmul(v_k.reshape(1, len(v_k)), A[kk + 1:m, kk:m]))
        A[0:m, kk + 1:m] -= 2*np.matmul(np.matmul(A[0:m, kk + 1:m], v_k).reshape(len(v_k), 1), v_k.reshape(1, len(v_k)))

    return A

# Implemente the Rayleigh quotient.
#def RayleighQ(x):