import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

tol = 1e-10
alpha = 1.1

F = lambda X: np.array([
    np.cos(X[0]) - np.sin(X[1]),
    np.sin(X[0]) + alpha*np.sin(2*X[0]) + alpha*np.cos(2*X[1]),
])
J = lambda X: np.array([
    [-np.sin(X[0]), -np.cos(X[1])],
    [np.cos(X[0]) + 2*alpha*np.cos(2*X[0]), -2*alpha*np.sin(2*X[1])],
])

d = np.inf # dummy
X = np.array([3*np.pi/2, 0]) # startgissning

while np.max(np.abs(d)) > tol:
    d = -np.linalg.solve(J(X), F(X))
    X += d

r0 = np.array([np.cos(X[0]), np.sin(X[0]) + alpha*np.sin(2*X[0])])
print(X)
print(r0)

if __name__ == '__main__':
    plt.show()
