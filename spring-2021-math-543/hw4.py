import numpy as np
import matplotlib.pyplot as plt

# Classical Gram-Schmidt
# def QR_CGS(A):
#     m, n = A.shape
#     Q = np.array([[] for ii in range(m)])
#     R = np.zeros((n, n))
#     v0 = A[:, 0].reshape((m, 1))
#     R[0, 0] = np.linalg.norm(v0)
#     Q = np.append(Q, v0 / R[0, 0], axis=1)
#     for jj in range(1, n):
#         vj = A[:, jj].reshape((m, 1))
#         aj = vj.copy()
#         for ii in range(jj):
#             R[ii, jj] = np.dot(Q[:, ii].T, aj)
#             vj = vj - R[ii, jj] * Q[:, ii].reshape((m, 1))
#
#         R[jj, jj] = np.linalg.norm(vj)
#         Q = np.append(Q, vj / R[jj, jj], axis=1)
#     return Q, R

# Classical Gram-Schmidt
#   Copied from http://mlwiki.org/index.php/Gram-Schmidt_Process#Python
def QR_CGS(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for jj in range(n):
        v = A[:, jj]

        for ii in range(j - 1):
            q = Q[:, ii]
            R[ii ,jj] = q.dot(v)
            v -= R[ii, jj]*q
        Q[:, ii] = V[:, ii] / R[ii, ii]
        for jj in range(ii + 1, n):
            R[ii, jj] = np.dot(Q[:, ii].T, V[:, jj])
            V[:, jj] -= R[ii, jj]*Q[:, ii]

    return Q, R

# Modified Gram-Schmidt
def QR_MGS(A):
    m, n = A.shape
    V = np.matrix.copy(A)
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for ii in range(n):
        R[ii ,ii] = np.linalg.norm(V[:, ii])
        Q[:, ii] = V[:, ii] / R[ii, ii]
        for jj in range(ii + 1, n):
            R[ii, jj] = np.dot(Q[:, ii].T, V[:, jj])
            V[:, jj] -= R[ii, jj]*Q[:, ii]

    return Q, R

# Experiment 1
x = np.linspace(-128, 128, 257)/128
A = np.ones((257, 4))
for ii in range(1, 4):
    A[:, ii] = x**ii

Q, R = QR_MGS(A)
scale = Q[256, :]

Q = np.dot(Q, np.diag(1/scale))

lgnd = ["$x^{}$".format(ii) for ii in range(4)]
fig = plt.figure(figsize=(7, 7))
ax = plt.gca()

for ii in range(4):
    ax.plot(Q[:, ii], label=lgnd[ii])

ax.grid()
ax.legend()
plt.title('Experiment 1: Legendre Plot')
plt.show()

# Experiment 2
U, _ = np.linalg.qr(np.random.rand(80, 80))
V, _ = np.linalg.qr(np.random.rand(80, 80))
S = 2**np.linspace(-1, -80, 80)

A = U*S*V

cQ, cR = QR_CGS(A)
mQ, mR = QR_MGS(A)

diagCR =
diagMR =

eps = np.finfo(float).eps
sqrt_eps = np.sqrt(eps)

t = np.linspace(1, 80, 80)

fig = plt.figure(figsize=(7, 7))
ax = plt.gca()
ax.semilogy(t, S, label="$2^t$")
ax.semilogy(t, mR.diagonal(), label="Diagonal of R from MGS")
ax.semilogy(t, cR.diagonal(), label="Diagonal of R from CGS")
plt.axhline(eps, linestyle='-.', label="$\epsilon_{machine}$")
plt.axhline(sqrt_eps, linestyle='--', label="$\sqrt{\epsilon_{machine}}$")
plt.grid()
ax.legend()
plt.title('Experiment 2')
plt.xlabel('t')
plt.ylabel('Logplot')
plt.show()