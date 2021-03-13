# Code provided by Stevie Dickerson, modified by Victor Arjona
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt

DEBUG = False

fig, axs = plt.subplots(2, 3, figsize=(11, 7))
axs = axs.flatten()
lims = (-1.5, 1.5)

for n in range(3, 9):
    m = 2 ** n
    rho = np.array([])
    lam = np.array([])
    norms = np.array([])

    for i in range(1, 100):
        A = np.random.rand(m, m) / np.sqrt(m)
        eigs_tmp = la.eigvals(A)
        rho = np.append(rho, max(abs(eigs_tmp)))
        lam = np.append(lam, eigs_tmp)
        # In the solution it's like this
        # norms = np.append(la.norm(A, 2))
        norms = np.append(norms, la.norm(A, 2))

    if DEBUG == True:
        print("Size of 100 Matrixes: {}x{}\n".format(m, m),
              "Size of rho: {}\n".format(rho.size),
              "Size of lam: {}\n".format(lam.size),
              "Size of norms: {}\n".format(norms.size))
    real_lam = np.real(lam)
    imag_lam = np.imag(lam)
    axs[n - 3].plot(real_lam, imag_lam, 'o')
    #axs[n - 3].set(xlim=lims, ylim=lims)
