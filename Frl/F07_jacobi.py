'''
Exempel på Jacobis metod. Frl 7 (2026-02-03).
'''

import numpy as np
import scipy as sp
import time

def main():
    # Skapa en stor slumpmässig matris
    N = 2000
    print('Skapar matrisen ...')
    A = np.random.randn(N,N)*0.1/np.sqrt(N) + np.diag(np.ones(N))
    print('Klart! Matrisens storlek:', A.shape)
    b = np.random.randn(N)
    print()

    # Lös direkt med vanlig solve, som referens
    tic = time.time()
    xref = np.linalg.solve(A, b)
    time1 = time.time() - tic
    print(f'Direkt lösning tog {time1} s.')

    # Jacobis metod med tolerans
    tic = time.time()
    tol = 1e-4
    p = np.diag(A)
    # Inversen av P kan konstrueras direkt eftersom det är en
    # diagonal matris:
    Pinv = sp.sparse.diags(1/p, 0, (N,N))
    B = np.diag(p) - A
    x = np.zeros(N) # startgissning för metoden
    diff = [np.inf] # för att komma in i slingan
    while np.linalg.norm(diff, np.inf) > tol:
        xnew = Pinv @ (B @ x + b) # Jacobi
        diff = xnew - x
        x = xnew
    time2 = time.time() - tic
    print(f'Jacobis metod tog {time2} s.')

    fel = np.linalg.norm(x - xref, np.inf)
    print(f'Felet blev: {fel}')
    return

if __name__ == '__main__':
    main()
