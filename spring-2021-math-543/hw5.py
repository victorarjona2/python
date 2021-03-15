# This code is a product of collaboration with Stevie Dickerson
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt

# For debugging purposes. If set True the size of the current 100 matrices and the size of rho/lambda/norms
#   is printed.
DEBUG = False

# Generate the figure that's going to have the values of lambda plotted.
# FYI, lambda list will contain all the Eigen values
fig, axs = plt.subplots(2, 3, figsize=(11, 7))
fig.tight_layout()
axs = axs.flatten()
lims = (-1.5, 1.5)
plt_title = "Matrix size = {}\nAverage Spectral Radius = {:.2f}\nAverage norm = {:.2f}"

m_vals = []
mean_max_rho_vals = []
mean_norms = []

for n in range(3, 9):
    m = 2 ** n
    rho = np.array([])
    lam = np.array([])
    norms = np.array([])

    for i in range(1, 100):
        # THIS DOESN'T WORK, STEVIE!
        # A = np.random.rand(m, m) / np.sqrt(m)
        A = np.random.normal(loc=0,                 # Mean
                             scale=1/np.sqrt(m),    # Standard Deviation
                             size=(m, m))           # Dimensions of matrix
        eigs_tmp = la.eigvals(A)
        rho = np.append(rho, max(abs(eigs_tmp)))
        lam = np.append(lam, eigs_tmp)
        # In the solution it's like this
        # norms = np.append(la.norm(A, 2))
        norms = np.append(norms, la.norm(A, 2))

    if DEBUG:
        print("Size of 100 Matrixes: {}x{}\n".format(m, m),
              "Size of rho: {}\n".format(rho.size),
              "Size of lam: {}\n".format(lam.size),
              "Size of norms: {}\n".format(norms.size))

    m_vals.append(m)
    mean_max_rho_vals.append(np.mean(rho))
    mean_norms.append(np.mean(norms))

    real_lam = np.real(lam)
    imag_lam = np.imag(lam)
    plt.tight_layout()
    axs[n - 3].plot(real_lam, imag_lam, 'o', mfc='none')
    axs[n - 3].set(xlim=lims, ylim=lims)
    axs[n - 3].grid()
    axs[n - 3].set(xlabel='Real values of $\lambda$', ylabel='Imag values of $\lambda$')
    axs[n - 3].set_title(plt_title.format(m,
                                          mean_max_rho_vals[-1],
                                          mean_norms[-1]))

fig, axs = plt.subplots(1, 2, figsize=(7, 5))
fig.tight_layout()
axs = axs.flatten()

axs[0].semilogx(m_vals, mean_max_rho_vals)
axs[0].grid()
axs[0].set(xlabel='Values of m', ylabel='Mean Spectral Radius')

axs[1].semilogx(m_vals, mean_norms)
axs[1].grid()
axs[1].set(xlabel='Values of m', ylabel='Mean Norms')