'''
Exempel: tre kvadraturmetoder. Frl 10 (2026-03-24).
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def main():
    f = lambda x: np.cos(x)**2 * np.exp(x)
    a = 0
    b = 2*np.pi

    # Referenslösning
    Iref = sp.integrate.quad(f, a, b, epsabs=1e-13, epsrel=1e-13)[0]

    N = 2 ** np.arange(2, 20)
    T = np.zeros(N.shape)
    S = np.zeros(N.shape)
    MC = np.zeros(N.shape)
    for i in range(N.size):
        # Trapetsregeln
        L = b - a
        h = L/N[i]
        x = np.linspace(a, b, N[i]+1)
        fx = f(x)
        T[i] = h * (np.sum(fx) - 0.5*fx[0] - 0.5*fx[-1])

        # Simpson
        # h och x och fx är som för trapetsregeln
        S[i] = (h/3) * (fx[0] + 4*np.sum(fx[1:-1:2])
                        + 2*np.sum(fx[2:-1:2])
                        + fx[-1])

        # Monte Carlo
        # |Omega| = L från tidigare
        X = L * np.random.rand(N[i]) # tal mellan 0 och 2*pi
        fX = f(X)
        MC[i] = L * np.sum(fX) / N[i]

        print(T[i], S[i], MC[i])

    plt.figure(1)
    plt.clf()
    plt.loglog(N, np.abs(T - Iref), '.-', label='Trapets')
    plt.loglog(N, 1e3*np.float64(N) ** (-2), 'k--')
    plt.loglog(N, np.abs(S - Iref), '.-', label='Simpson')
    plt.loglog(N, 1e3*np.float64(N) ** (-4), 'k:')
    plt.loglog(N, np.abs(MC - Iref), '.-', label='Monte Carlo')
    plt.loglog(N, 1e3*np.float64(N) ** (-1/2), 'k-')
    plt.legend()
    plt.xlabel('$N$')
    plt.title('Fel för olika kvadraturmetoder')

    # Prova att köra flera gånger! Monte Carlo ger lite olika
    # resultat varje gång.

    return

if __name__ == '__main__':
    main()
    plt.show()
