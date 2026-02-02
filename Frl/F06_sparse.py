'''
Exempel med gles matris. Frl 6 (2026-02-02).
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def main():
    # Skapa en tridiagonal matris
    N = 10
    D1 = np.diag(np.ones(N-1), -1)
    D2 = np.diag(-2*np.ones(N), 0)
    D3 = np.diag(np.ones(N-1), 1)
    A = D1 + D2 + D3

    # Plotta de nollskilda elemented i A
    plt.clf()
    plt.spy(A)

    # Konvertera matrisen till glest format och lös
    As = sp.sparse.csc_matrix(A)
    print(As)
    b = np.random.randn(N)
    x = sp.sparse.linalg.spsolve(As, b)
    print(x)

    # Lösningen blir samma med vanliga solve, fast det tar mycket
    # längre tid för stora N
    xref = np.linalg.solve(A, b)
    print(xref)
    return

if __name__ == '__main__':
    main()
    plt.show()
