# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

#def QR_CGS(A):
#    # To compare
#    numpy_sol = np.linalg.qr(A)
#    
#    # Dimension of A
#    m, n = A.shape
#        
#    # Q must be orthonormal and of dimension mxn
#    # R must be an upper triangular matrix and of dimension nxn
#    #   The first element 
#    q1 = A[:, 0]/np.linalg.norm(A[:, 0])
#    Q = np.array([[] for ii in range(m)])
#    Q = np.append(Q, q1, axis=1)
#    for ii in range(1, n):
#        q2 = A[:, ii] - q1

def QR_CGS(A):
    # Dimensions of A; because it's always nice to know, just in case
    m, n = A.shape
    
    # Q is, for now, an empty column vector
    # This is done so that we can append new elements to it that are column vectors
    # It should end up as te same np.shape as A!
    Q = np.array([[] for ii in range(m)])
    
    # R starts as a matrix of nxn zeroes
    R = np.zeros((n, n))

    # Construct first element of R and Q
    #   v0 is the first column vector of A, but it' s returned as an array, so we reshape it as an mx1 array
    v0 = A[:, 0].reshape((m, 1))
    #   R[0, 0] is equal to the norm of v0
    R[0, 0] = np.linalg.norm(v0)
    #   The first column vector of Q is the normalized first column vector of A
    Q = np.append(Q, v0/R[0, 0], axis=1)

    # So far, we have one column vector in Q, and one element filled up in the first row, first column position of R
    # For 1 all the way up to n-1 (columns)
    for jj in range(1, n):
        # Print out what column index we're on
        print("In column {}!\n".format(jj))

        # Collect the next column from A and reshape it as mx1
        # This is the column vector that we'll manipulate
        vj = A[:, jj].reshape((m, 1))

        # Store a copy in aj
        aj = vj.copy()

        # Every time we construct an element of R we have to use it on vj
        for ii in range(jj):
            # Construct R[ii, jj]
            R[ii, jj] = np.dot(Q[:, ii].T, aj)
            vj = vj - R[ii, jj]*Q[:, ii].reshape((m, 1))
        R[jj, jj] = np.linalg.norm(vj)
        Q = np.append(Q, vj/R[jj, jj], axis=1)

    return Q, R