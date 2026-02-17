'''
Exempel på Lagrange-polynom. Frl 8 (2026-02-17).
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    # Plotta två Lagrange-polynom
    plt.clf()
    xd = np.arange(0, 5+1)
    plotta_lagrange(0, xd)
    plotta_lagrange(2, xd)
    return

def plotta_lagrange(j, xd):
    '''
    Plotta Lagrange-polynomet L_j(x).
    '''
    x = np.linspace(xd[0], xd[-1], 200)
    y = lagrange_pol(j, x, xd)
    plt.plot(x, y)
    yd = np.zeros(xd.shape)
    yd[j] = 1
    plt.plot(xd, yd, 'k.')
    plt.grid(True)
    return

def lagrange_pol(j, x, xd):
    '''
    Evaluera Lagrange-polynom L_j(x).

    Indata:
    j -- Lagrange-polynomets index (0, ..., n)
    x -- evalueringspunkter
    xd -- datapunkterna (n+1 stycken)
    '''
    n = xd.size - 1
    val = 1
    for k in range(n+1):
        if k == j:
            continue # hoppa över denna iteration
        val *= (x - xd[k]) / (xd[j] - xd[k])
    return val

if __name__ == '__main__':
    main()
    plt.show()
