'''
Exempel på styckvis linjär interpolation. Frl 8 (2026-02-17).
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    # Plotta polynominterpolationer med olika antal punkter
    plt.clf()
    styckvis(4)
    styckvis(8)
    styckvis(16)
    styckvis(32)
    return

def styckvis(n):
    '''
    Styckvis linjär interpolation med n+1 ekvidistanta punkter.
    Plotta både funktionen, polynomet och felet.
    '''
    f = lambda x: 1 / (1 + 25*x**2)
    x = np.linspace(-1, 1, n+1)
    y = f(x)
    p = lambda xv: np.interp(xv, x, y)

    xfin = np.linspace(-1, 1, 200)
    ffin = f(xfin)
    pfin = p(xfin)
    fel = pfin - ffin

    plt.subplot(2, 1, 1)
    plt.plot(xfin, pfin, label=f'n={n}')
    plt.plot(xfin, ffin, 'k--', linewidth=1)
    plt.plot(x, y, '.k')
    plt.title('Styckvis polynom')
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
