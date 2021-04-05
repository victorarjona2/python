# Stevie Dickerson - Math 543, Homework 6
#I, Stevie Dickerson, pledge that this program is completely my own work, and that I did not take, borrow or steal code from any other person, and that I did not allow any other person to use, have, borrow or steal portions of my code. I understand that if I violate this honesty pledge, I am subject to disciplinary action pursuant to the appropriate sections of the San Diego State University Policies.
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt

# TB-18.1
# Note: Matrix A has full rank (for non-square nxm matrix where n<m, determine that columns of matrix are linearly independent (Ax=0))
A = np.matrix([[1, 1],
               [1, 1.0001],
               [1, 1.0001]])

b = np.matrix([[2],
               [0.0001],
               [4.0001]])
print("A = \n", A)
print("b = \nS", b)

# Part a
pinv = la.pinv(A) # To test: pseudoinverse of A (A^+)

# If the columns of A are linearly independent, then  A^+ = [(A^T) * A ^(-1)] * A^T
A_pinv = la.inv((np.transpose(A) * A)) * np.transpose(A) # Manually compute the psuedoinverse of A (A^+)
P = A * A_pinv # Orthogonal projector onto range(A), P = A * A^+
print("Pseudoinverse = ", pinv)
print("A^+ = ", A_pinv)
print("P = ", P)

# Part b - Least Squares problem: Ax~b
# Note: x is unique IFF A has full rank
x = A_pinv * b # x = A^+ * b
y = P * b # y = P * b
print("x = ", x)
print("y = ", y)

# Part c
# Condition is the measure of sensitivity of solutions to perturbations in the data
k = la.cond(A) # To test: condition number of matrix
k_A = la.norm(A, 2) * la.norm(la.pinv(A), 2) # Manually compute condition number of matrix: k(A) = ||A||*||A^+||
theta = np.arccos(la.norm(y,2 ) / la.norm(b, 2)) # Angle theta measures the closeness of the fit
n = (la.norm(A, 2) * la.norm(x, 2)) / la.norm(y, 2) # eta = Measure of how much ||y|| falls short of its max possible value
print("Condition Number = ", k)
print("k(A) = ", k_A)
print("theta = ", theta)
print("eta = ", n)

# Part d - 2-norm Relative condition numbers of Thm 18.1
b_y = 1 / np.cos(theta)
b_x = k_A / (n * np.cos(theta))
A_y = k_A / np.cos(theta)
A_x = k_A + ((k_A ** 2) * np.tan(theta)) / n
print("Theorom 18.1 - Four condition numbers:")
print("b*y = ", b_y)
print("b*x = ", b_x)
print("A*y = ", A_y)
print("A*x = ", A_x)

# Part e
O_eps = np.finfo(float).eps # Machine epsilon (O_eps = errors)

# Conditioning pertains to the perturbation behavior of a mathematical problem.
# Stability pertains to the perturbation behavior of an algorithm used to solve that problem.
# A problem is ill-conditions if k(A) is found to be large.
# An ill-conditioned problem means that a small perturbation results in a large change.
# Per pg.131: The four numbers from Thm 18.1 describe the sensitivities of y and x
# to perturbations in b and A, where b*y & b*x are obtained from delta_b.
# Using formula 16.3, we can say norm(delta_A) = norm(A)*O_eps, where O_eps = errors.
# And QR = A + delta_A
# Perturbation delta*b:
# Perturbation delta*A:
print("delta_b = ")
print("delta_A = ")

# PB-14.1
# Per the logplot, the higher degree polynomial, the more inconsistent the least-squares fit.
# If the problem is ill-conditioned, you can expect to lose log(k(A)) digits
x = np.linspace(0, 1, 101)
c_k = []

for k in range(1, 1000):
    A_k = np.vander(x, N=(k+1))
    c = la.cond(A_k)
    c_k = np.append(c_k, c)

#print("c_k = ", c_k)

#print("Number of elements in c_k", len(c_k))

# Plot c using a log scale
fig = plt.figure(figsize=(7, 7))
ax = plt.gca()
plt.plot(c_k)
plt.yscale("log")
plt.grid()
plt.title("Collection of Condition Numbers")
plt.xlabel("k")
plt.ylabel("Logplot")
plt.show()
