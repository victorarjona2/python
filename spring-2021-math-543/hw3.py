# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

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
    # For 1 all the way up to n-1 (columns)...
    for jj in range(1, n):
        # Collect the next column from A and reshape it as mx1
        # This is the column vector that we'll manipulate
        vj = A[:, jj].reshape((m, 1))

        # Store a copy in aj
        aj = vj.copy()

        # Every time we construct an element of R we have to use it on vj
        for ii in range(jj):
            # Construct R[ii, jj]
            R[ii, jj] = np.dot(Q[:, ii].T, aj)
            # Update vj by subtracting R[ii, jj]*Q[:, ii]
            vj = vj - R[ii, jj]*Q[:, ii].reshape((m, 1))
        # Construct the norm of vj and store it in R[jj, jj]
        R[jj, jj] = np.linalg.norm(vj)
        # Append the new vj
        Q = np.append(Q, vj/R[jj, jj], axis=1)

    # Return Q, R
    return Q, R

def TestMatrixWithQR(A):
    m, n = A.shape
    if m < n:
        print('We have more columns than rows! Exiting')
        return None

    Q, R = QR_CGS(A)
    npQ, npR = np.linalg.qr(A)

    is_R_ut = np.allclose(R, np.triu(R))
    is_npR_ut = np.allclose(npR, np.triu(npR))

    is_Q_unitary = np.allclose(np.eye(Q.shape[0]), Q.H * Q)
    is_npQ_unitary = np.allclose(np.eye(npQ.shape[0]), npQ.H * npQ)
    
    print('Testing the following Matrix:\n', A, '\n\n')

    print('This is Q using CGS algorithm:\n', Q, '\n')
    print('This is Q using Numpy:\n', npQ, '\n\n')

    print('This is R using CGS algorithm:\n', R, '\n')
    print('This is R using Numpy:\n', npR, '\n\n')

    print('This is A-QR using CGS algorithm:\n', A - Q * R, '\n')
    print('This is A-QR using Numpy:\n', A - npQ * npR, '\n\n')

    print('Is Q using CGS algorithm Unitary?: {}'.format(is_Q_unitary))
    print('Is Q using Numpy algorithm Unitary?: {}\n\n'.format(is_npQ_unitary))

    print('Is R using CGS algorithm Upper Triangular?: {}'.format(is_R_ut))
    print('Is R using Numpy algorithm Upper Triangular?: {}\n\n'.format(is_npR_ut))

# Example Matrix
A = np.matrix([[1, 2, 0],
               [0, 1, 1],
               [1, 0, 1]])

# More columns than rows
B = np.matrix([[1, 5, -3, 1],
               [3, -1, 0, -9],
               [2, 7, -3, -1]])

# Column vectors are not independent
C = np.matrix([[1, 2, 3],
               [0, 1, 1],
               [1, 0, 1]])

# Row vectors are not independent
D = np.matrix([[1, 2, 0],
               [0, 1, 1],
               [1, 3, 1]])

TestMatrixWithQR(A)
TestMatrixWithQR(B)
TestMatrixWithQR(C)
TestMatrixWithQR(D)