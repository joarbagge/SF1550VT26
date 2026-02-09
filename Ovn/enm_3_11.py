import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def picard():
    print('== Picarditeration ==')
    np.set_printoptions(precision=16) # visa alla decimaler

    A = np.array([[10, -1, 0],
                  [1, 10, -1],
                  [1, 0, 3]])
    b = lambda x: np.array([x[0]**2 + x[1]**2, 2 - x[1]**3, 1 - x[2]**3])

    # Startgissning
    x = np.array([0.0230, 0.2303, 0.3257])

    tol = 0.5e-7 # sju korrekta decimaler
    i = 0
    delta = [np.inf] # stort tal för att komma in i slingan
    while np.linalg.norm(delta, np.inf) > tol:
        xnew = np.linalg.solve(A, b(x)) # lös A*xnew = b(x)
        delta = xnew - x
        x = xnew
        i += 1
        print(i, x)

def gauss_seidel():
    print('== Gauss-Seidel ==')
    np.set_printoptions(precision=16) # visa alla decimaler

    # Startgissning
    x = np.array([0.0230, 0.2303, 0.3257])

    tol = 0.5e-7 # sju korrekta decimaler
    i = 0
    delta = [np.inf] # stort tal för att komma in i slingan
    while np.linalg.norm(delta, np.inf) > tol:
        xold = x.copy()
        x[0] = (1/10)*(x[1]  + x[0]**2 + x[1]**2)
        x[1] = (1/10)*(-x[0] + x[2] + 2 - x[1]**3)
        x[2] = (1/3) *(-x[0] + 1 - x[2]**3)
        delta = x - xold
        i += 1
        print(i, x)

def newton():
    print('== Newton ==')
    np.set_printoptions(precision=16) # visa alla decimaler

    A = np.array([[10, -1, 0],
                  [1, 10, -1],
                  [1, 0, 3]])
    b = lambda x: np.array([x[0]**2 + x[1]**2, 2 - x[1]**3, 1 - x[2]**3])
    F = lambda x: A @ x - b(x)
    J = lambda x: A - np.array([[2*x[0], 2*x[1], 0],
                                [0, -3*x[1]**2, 0],
                                [0, 0, -3*x[2]**2]])

    # Startgissning
    x = np.array([0.0230, 0.2303, 0.3257])

    tol = 0.5e-7 # sju korrekta decimaler
    i = 0
    delta = [np.inf] # stort tal för att komma in i slingan
    while np.linalg.norm(delta, np.inf) > tol:
        delta = -np.linalg.solve(J(x), F(x))
        x += delta
        i += 1
        print(i, x)

if __name__ == '__main__':
    picard()
    gauss_seidel()
    newton()
    plt.show()
