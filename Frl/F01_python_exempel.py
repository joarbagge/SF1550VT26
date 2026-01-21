'''
Exempel från Föreläsning 1 (2026-01-14)
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def main():
    # Plotta en funktion
    N = 100
    x = np.linspace(-2*np.pi, 2*np.pi, N)
    f = lambda x: np.sin(x)
    y = f(x)
    plt.figure(1)
    plt.clf()
    plt.plot(x, y)

    # Prova matrismultiplikation
    A = np.random.randn(N, N)
    b = A @ y
    plt.plot(x, b)

    # Räkna ut en fakultet (n!)
    n = np.arange(100)
    n_fac = sp.special.factorial(n)
    # För stora värden på n får vi overflow eftersom resultatet
    # blir större än ~1e308. Funktionen returnerar np.inf för
    # sådana värden. Detta händer då n >= 171.
    plt.figure(2)
    plt.clf()
    plt.semilogy(n, n_fac, '*-')
    return

if __name__ == '__main__':
    main()
    plt.show()
