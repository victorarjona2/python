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
    # Dimension of A
    m, n = A.shape
    
    # Q is, for now, an empty column vector
    Q = np.array([[] for ii in range(m)])
    
    # R is a matrix of nxn zeroes
    R = np.zeros((n, n))
    a0 = A[:, 0].reshape((m, 1))
    
    # Construct first element of R and Q
    R[0, 0] = np.linalg.norm(a0)
    Q = np.append(Q, a0/R[0, 0], axis=1)
    
    for jj in range(1, n):
        print("In column {}!\n".format(jj))
        aj = A[:, jj].reshape((m, 1))
        vj = aj
        for ii in range(jj-1):
            print("\tIn row {}!\n".format(ii))
            R[ii, jj] = np.dot(Q[:, ii], aj)
            vj = vj - R[ii, jj]*Q[:, ii]
        R[jj, jj] = np.linalg.norm(vj)
        Q = np.append(Q, vj/R[jj, jj])

    return Q, R