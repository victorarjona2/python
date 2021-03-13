# Code provided by Stevie Dickerson, modified by Victor Arjona
import numpy as np
from numpy import linalg as la

DEBUG = FALSE

for n in range(3, 8):
    m = 2**n
    rho = np.array([])
    lam = np.array([])
    norms = np.array([])

    for i in range(1, 100):
        A = np.random.rand(m, m) / np.sqrt(m)
        eigs_tmp = la.eigvals(A)
        rho = np.append(rho, max(abs(eigs_tmp)))
        lam = np.append(lam, eigs_tmp)
        norms = np.append(la.norm(A, 2))

    if DEBUG == True:
        print("Size of 100 Matrixes: {}x{}\n".format(m),
              "Size of rho: {}\n".format(rho.size)))