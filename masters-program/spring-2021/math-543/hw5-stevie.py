# Stevie Dickerson - Math 543, Homework 5
# I, Stevie Dickerson, pledge that this program is completely my own work, and that I did not take, borrow or steal code from any other person, and that I did not allow any other person to use, have, borrow or steal portions of my code. I understand that if I violate this honesty pledge, I am subject to disciplinary action pursuant to the appropriate sections of the San Diego State University Policies.
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
# Part a
    # Looking at the plots, most eigenvalues seem to fill the unit circle.
    # It's safe to say that the spectral radius (rho) is close to unity but slight >1.
    # Plotting mutltple m's suggests that the larger the matrix, the better fit to the unit circle.
# Part b
    # As m approaches infinity, the 2-norm approaches 2 (larger than the spectral radius).
    # Hence,  rho(A) <= norm(A, 2) is confirmed but the inequality does not approach an equality.

DEBUG = False # To debug, set to true to print size of 100 matrices and the lambda/rho/norms

fig, axs = plt.subplots(2, 3, figsize=(11, 7))
fig.tight_layout()

axs = axs.flatten()
lims = (-1.5, 1.5)
plt_title = "Matrix size = {}\nAverage Spectral Radius = {:.2f}\nAverage norm = {:.2f}"

m_vals = [] # Placeholder for m values
mean_max_rho_vals = [] # Placeholder for means of max rho values
mean_norms = [] # Placeholder for means of norms

for n in range(3, 9):
    m = 2**n # Compute m=2^n to get m=8,16,32,64,...
    lam = np.array([]) # Placeholder for Lambda values
    rho = np.array([]) # Placeholder for Rho values
    norms = np.array([]) # Placeholder fo Norms

    for i in range(100): # Superimpose 100 random matrices
        # Define random matrix size mxm whose entries are independent samples
        # from the real normal dist with mean=0 and std_dev=m^(-1/2)
        A = np.random.normal(loc=0,              # Mean
                             scale=1/np.sqrt(m), # Std Deviation
                             size=(m, m))        # Dimension of matrix
        eigs = la.eigvals(A) # Compute eigenvalues of A (aka Lambdas)
        lam = np.append(lam, eigs)
        rho = np.append(rho, max(abs(eigs))) # Compute spectral radius rho(A) = max(|eigval_i|) & append in single array
        norms = np.append(norms, la.norm(A)) # Compute the 2-norm of A

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

# Plot a, b
fig, axs = plt.subplots(1, 2, figsize=(7, 5))
fig.tight_layout()

axs = axs.flatten()
axs[0].semilogx(m_vals, mean_max_rho_vals)
axs[0].grid()
axs[0].set(xlabel='Values of m', ylabel='Mean Spectral Radius')
axs[1].semilogx(m_vals, mean_norms)
axs[1].grid()
axs[1].set(xlabel='Values of m', ylabel='Mean Norms')
plt.show()

# Part c
    # INSERT FINDINGS: The clusters change with the lrgr matrix, tend to cluster closer to zero
min_sing = np.array([])
datas = np.array([])
bounds = np.array([])
ns = []
jj = 1

for nn in range(3, 7):
    mm = 2 ** nn    # Compute m=2^n to get m=8,16,32,64,...
    for ii in range(1000):
        A = np.random.normal(loc=0,                 # Mean
                             scale=1 / np.sqrt(m),  # Std Deviation
                             size=(mm, mm))         # Dimension of matrix
        U, S, V = np.linalg.svd(A)
        min_sing = np.append(min_sing, np.min(S))
    data = np.array([])
    bound = np.array([])
    for jj in range(2, 13):
        bound = np.append(bound, 2**(-jj))
        min_sing_filter = min_sing <= 2**(-jj)
        min_sing_less_than_2_neg_jj = min_sing[min_sing_filter]
        data = np.append(data, min_sing_less_than_2_neg_jj/min_sing.size)
    bounds = np.append(bound, axis=1)
    datas = np.append(data, axis=1)
fig, axs = plt.subplots(1, 1, figsize=(5, 5))
fig.tight_layout()
axs = axs.flatten()
axs[0].plot(bounds, datas)
axs[0].grid()
plt.show()