'''
Exempel på interpolation i Chebyshev-punkter. Frl 8 (2026-02-17).
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    # Plotta polynominterpolationer med olika antal punkter
    plt.clf()
    chebyshev(4)
    chebyshev(8)
    chebyshev(16)
    chebyshev(32)
    return

def chebyshev(n):
    '''
    Polynominterpolation med n+1 Chebyshev-punkter.
    Plotta både funktionen, polynomet och felet.
    '''
    f = lambda x: 1 / (1 + 25*x**2)
    t = np.linspace(0, np.pi, n+1)
    x = np.cos(np.pi - t)
    y = f(x)
    p = np.polynomial.Polynomial.fit(x, y, n)

    xfin = np.linspace(-1, 1, 200)
    ffin = f(xfin)
    pfin = p(xfin)
    fel = pfin - ffin

    plt.subplot(2, 1, 1)
    plt.plot(xfin, pfin, label=f'n={n}')
    plt.plot(xfin, ffin, 'k--', linewidth=1)
    plt.plot(x, y, '.k')
    plt.title('Polynom')
    plt.ylim([-0.5, 1.5])
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(xfin, fel)
    plt.title('Fel')
    plt.ylim([-1, 1])
    plt.tight_layout()
    return

if __name__ == '__main__':
    main()
    plt.show()
